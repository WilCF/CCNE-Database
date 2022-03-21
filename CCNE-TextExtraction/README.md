# CCNE-TextExtractor
A program designed to extract specific data from the CCNE website (Accredited University, City, State, Degree-Types)

Link: https://directory.ccnecommunity.org/reports/accprog.asp

# Usage
Program used to quickly update our local database of accredited CCNE schools across the United States

# How it works
The program pulls information from the website's HTML file and changes the extension to a .txt file. Changing the extension allows us to read the file normally and begin finding specific points of interest. We're concerned with finding the following information of each CCNE Accredited school:
1. University Name
2. City
3. State
4. Degree type offered

We will also need the Latitude and Longitude of each CCNE Accredited school, but that information is not found on the CCNE website. We tackle this problem in a later phase of our operations through the Google Geocoding API (Look at Geocoding.py for more information). 
## 1. Identifying "University Name"
To pull out "University Name" from the HTML code, we simply iterate throughout the HTML.txt file for a line that contains the following code:
* ```<td valign="top" style="width: 50%;padding-right:15px">```

Once our program detects this line, we can start to break the HTML code apart to isolate our information. 
The format of the code for the "University Name" is always found in this form:
* [INSERT CODE FORM EXAMPLE]

(Notice, how the code that we're looking for always comes before the University name.)

