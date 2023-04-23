# val = -1 if NOT found. Else, returns index of position on the line
def hasString(segment, text):
    val = segment.find(text)
    return val


# grabs next line from file
def nextLine(doc):
    txt = doc.readline()
    return txt


# removes text up until//after 2nd <BR>
def cleanCityState(sentence):
    # Parse sentence by "<BR>"
    x = sentence.split("<BR>")

    # INFO contains "INFO<br>Extra_Stuff", parse & remove
    print("     PARSE-Line: ", x)
    x[2] = x[2].split("<br>")
    sentence = x[2][0]

    # Separate City Name (many word name poss.) from State & Zip-Code
    x = sentence.split(",")
    # Separate State and Zip-Code by Space
    x[1] = x[1].split(" ")

    # Putting it all together... (State is ALWAYS the last item in sentence!)
    sentence = x[0] + " " + x[1][1]
    return sentence


# grabs degrees from a single school
def getDegreeTypes(file):
    degreeTypes = ["0", "0", "0", "0"]
    degree = file.readline()
    # Iterate unless we hit end of school description (DO NOT CHOP!)
    while degree.find('<td valign="top" colspan="6"><hr align="left" width="100%"></td>') == -1:
        # If school degree-type line found (not -1) -> Parse info
        if degree.find("<table><tr><td><span class='blue b'>") != -1:
            # Parse to see what degree it is
            degree = degree.split(">")[4].split("</span")[0]

            # Remove "</span"
            print("**", degree)

            # Figure out what degree type we just parsed
            if degree.find("Baccalaureate") != -1:
                degreeTypes[0] = "1"
            elif degree.find("Master") != -1:  # Avoids Encoding error when "Master" instead of "Master's"
                degreeTypes[1] = "1"
            elif degree.find("Doctor of Nursing Practice") != -1:
                degreeTypes[2] = "1"
            elif degree.find("Post-Graduate APRN Certificate") != -1:
                degreeTypes[3] = "1"

        # get new line and start again
        degree = file.readline()
    return degreeTypes


# Opens text file
with open("rawHTML.txt", "r") as file, open("localDatabase.txt", "w") as dataBase:
    # Locations where INFO is kept, use SINGLE QUOTES!! (interferes with text)
    textBreak = ['<td valign="top" style="width: 50%;padding-right:15px">']

    # Array -> Send to Database. Form: [uni,city,state, 0, 0,0BSN,MSN,DNP]
    storage = ["uni", "city", "state", "0", "0", "0", "0", "0", "0"]

    finishedIterating = False

    while not finishedIterating:
        # EOF = "</html>" -> This is our final breakpoint!
        line = nextLine(file)
        contains = hasString(line, textBreak[0])

        # Iterates until we match with a textbreak
        while contains == -1 & line.find("</html>") == -1:
            line = nextLine(file)
            contains = hasString(line, textBreak[0])

        # Match found! -> Check if not EOF -> Start school process
        if line.find("</html>") == -1:
            # Get next line (SCHOOL NAME!)
            line = nextLine(file)

            # Remove unwanted strings (first & last elements) FORM: <br> INFO
            # </br>
            x = line.split(" ")
            del x[0]
            del x[len(x) - 1]
            line = " ".join(x)
            print("University: ", line)

            # Send to storage (later inserted to local database)
            storage[0] = line

            # Get next 2 lines (CITY, STATE!)
            # line = nextLine(file)
            # line = nextLine(file)
            line = nextLine(file)
            while line.find("href=") == -1:
                line = nextLine(file)
            print(line)
            countBR = 1  # Unused VAR, remove.

            # Remove unwanted strings (ONLY need 3rd index from line)
            # FORM: X<br>X<br>INFO<br>X<br>
            line = cleanCityState(line)

            # Get City & State (State ALWAYS last item in line!)
            line = line.split(" ")
            state = line[len(line) - 1]
            del line[len(line) - 1]
            city = " ".join(line)

            # Send to storage (later inserted to database)
            storage[1] = city
            storage[2] = state

            print("City: ", storage[1])
            print("State: ", storage[2])

            # TODO: Algorithm to find each degree type offered by each school
            accreditations = getDegreeTypes(file)
            storage[5] = accreditations[0]
            storage[6] = accreditations[1]
            storage[7] = accreditations[2]
            storage[8] = accreditations[3]
            print("     Baccalaureate: ", storage[5])
            print("     Master's: ", storage[6])
            print("     Doctor of Nursing Practice: ", storage[7])
            print("     Post-Graduate APRN Certificate: ", storage[8])

            # Writes to local database
            dataBase.write(storage[0]+";"+storage[1]+";"+storage[2]+";")
            dataBase.write(storage[3]+";"+storage[4]+";"+storage[5]+";")
            dataBase.write(storage[6]+";"+storage[7]+";"+storage[8])

            dataBase.write("\n")

            # Restore defaults & start again
            storage = ["uni", "city", "state", "0", "0", "0", "0", "0", "0"]

            print("\n")
        else:
            print("\nEOF Reached")
            finishedIterating = True

    print("\nFinished Reading HTML file")
    dataBase.close()
    file.close()
