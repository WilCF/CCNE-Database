import time
import requests

# base_url = "https://maps.googleapis.com/maps/api/geocode/json?address=University%20of%20new%20mexico&key=AIzaSyCiyYyM1C0QSwpkxUPH_mSEDFZnteFrrMk"


# Response from Google contains ALL details of school location...
# But we only want coordinates, parse info to get this only.
def parsePackage(response):
    # 2 Main Types: Error or OK
    response.keys()
    if response['status'] == "OK":
        # Dictionary of items -> 'Results' -> 1 item -> 'Geometry' description
        geometry = response['results'][0]['geometry']

        # Within geometry descriptions we can find lat & lng of our address
        latitude = geometry['location']['lat']
        longitude = geometry['location']['lng']

        location = str(latitude) + ";" + str(longitude)
        # print("Response Location: ", location)
    else:
        # print("[SERVER RESPONSE ERROR: ", response['status'], "]")
        location = "SERVER RESPONSE ERROR"

    return location


# appends school name & API_KEY to base_url (to send to api)
def appendSchool(base_url, address):
    API_KEY = "AIzaSyCiyYyM1C0QSwpkxUPH_mSEDFZnteFrrMk"

    # API requires spaces to be replaced with "%20"
    address = address.split(" ")
    address = "%20".join(address)

    # Append Address & API_KEY
    base_url = base_url + "address=" + address + "&key=" + API_KEY
    return base_url


# gets a pair of coordinates, given a location
def getCoordinates(schoolName):
    base_url = "https://maps.googleapis.com/maps/api/geocode/json?"
    modified_url = appendSchool(base_url, schoolName)

    # Send package to google
    response = requests.get(modified_url).json()

    # Get Coordinates of school ONLY, removes all the other stuff & return data
    response = parsePackage(response)
    return response


# Update our dataline from the database with lat & lng coordinates
def updateDataLine(data, latitude, longitude):
    latLng = latitude + ";" + longitude
    data = latLng + ";" + data
    return data


# Open local database to retrieve school names
with open("localDatabase - Copy.txt", 'r') as database, open("updatedLocalDatabase.txt", 'a') as updatedDatabase:
    finishedIterating = False
    while not finishedIterating:
        # Read in next line in database
        dataLine = database.readline()

        # Get school name
        school = dataLine.split(";").pop(0)

        # Get coordinates of school (url link to send to google)
        coordinates = getCoordinates(school)

        # Check to see if our packages returned valid coordinates
        if coordinates.find("SERVER RESPONSE ERROR") == -1:
            # Split coordinates into latitude & longitude
            coordinates = coordinates.split(";")
            latitude = coordinates[0]
            longitude = coordinates[1]

            # TODO: Write to database
            print("School: ", school)
            print("Latitude: ", latitude)
            print("Longitude: ", longitude)

            data = updateDataLine(dataLine, latitude, longitude)
            print("Updated Dataline: ", data)
            print()
            updatedDatabase.write(data)

            time.sleep(1)
        else:
            # If school exception found -> VOID finishedIterating
            exceptions = ["Adelphi University", "AdventHealth University",
                          "American National University",
                          "American Public University System",
                          "Anderson University - IN", "Baker College",
                          "Bryant & Stratton College-Online Education",
                          "Bryant & Stratton College-Parma",
                          "Bryant & Stratton College-Wauwatosa", "Citadel, The",
                          "Georgia Intercollegiate Consortium for Graduate Nursing Education",
                          "Grantham University", "Intercollegiate Consortium for a Master of Science in Nursing",
                          "New York Institute of Technology",
                          "Pasco-Hernando State College", "South College",
                          "South University",
                          "Southern California CSU DNP Consortium",
                          "Stevenson University", "Unitek College",
                          "University of California, San Francisco",
                          "University of Miami", "University of Puerto Rico",
                          "University of Washington"]
            for e in exceptions:
                if school.find(e) != -1:
                    finishedIterating = False
                    print("School: ", school)
                    print("Latitude: **N/A**")
                    print("Longitude: **N/A**")

                    data = updateDataLine(dataLine, "**N/A**", "**N/A**")
                    updatedDatabase.write(data)
                    break
                else:
                    finishedIterating = True
print("\nFinished Iterating...")

# Close data flow
database.close()
updatedDatabase.close()
print("Database closed.")
