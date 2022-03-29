# CCNE-TextExtractor
A program designed to extract specific data from the CCNE website (Accredited University, City, State, Degree-Types)

Link: https://directory.ccnecommunity.org/reports/accprog.asp

# Usage
Program used to quickly update our local database of CCNE accredited schools across the United States

# How it works
The program pulls information from the website's HTML file and changes the extension to a .txt file. Changing the extension allows us to read the file normally and begin finding specific points of interest. We're concerned with finding the following information of each CCNE Accredited school:
1. University Name
2. City
3. State
4. Degree type offered

We will also need the Latitude and Longitude of each CCNE Accredited school, but that information is not found on the CCNE website. We tackle this problem in a later phase of our operations through the Google Geocoding API (Look at Geocoding.py for more information). 

## 1. Identifying "University Name"
The University's name always comes 1 line after this code snippet. To pull out "University Name" from the HTML code, we simply iterate throughout the HTML.txt file for a line that contains the following code:

```<td valign="top" style="width: 50%;padding-right:15px">```

Once our program detects this line, we can start to break the HTML code apart to isolate our information. The format of the code for the "University Name" is always found in this form:

```<h3> Generic University Name </h3>```

## 2/3. Identifying "City" & "State"
After finding the University Name, we can skip 2 lines to find the school's address, including it's city and state locations. We can break this line into an array, separated by ```<BR>```, and then pull the array element with the City and State information. Once we do this, we can remove the website link by breaking this array element by ```<br>```, and removing the second element (website link). After all of this, we will be left with the string ```City, State Zip-Code```. We can pull our information by turning it into an array that's separated by spaces. The format of the code for the "City" and "State" is always found in this form:

```School of Nursing<BR>Generic Building Address, ACU Box 28035<BR>City, State Zip-Code <br><a href=http://www.genericschoolwebsite.com>Link to Website</a><br>```

## 4. Identifying "Degree type offered"
At this point in our code, we should have the University Name, City, and State. Now, all we need are the degree types offered by each institution. To obtain this, we have to look for a code snippet that holds this information. Regardless of the degree type, all degrees will begin with this code:

```<table><tr><td><span class='blue b'>```

This is how the full line looks like (including the code snippet in the beginning):
```<table><tr><td><span class='blue b'>Degree Type</span></td></tr><tr><td>November 5, 2014</td></tr><tr><td>November 20, 2019</td></tr><tr><td>June 30, 2030</td></tr><tr><td>November 2019</td></tr><tr><td>Fall 2029</td></tr></table>```

To isolate our degree type, we can pop the code snippet ```<table><tr><td><span class='blue b'>```out from our line and turn our remaining information into an array that's separated by ```</span>```. If we follow this methodology, our degree type should always be the first element in our array. 

We repeat this process of finding the degree type until we encounter one of two things:
1. The next university
2. The end of our html code (```</html>```)


