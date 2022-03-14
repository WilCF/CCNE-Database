# CCNE-Database
A program designed to extract specific data from the CCNE website (Accredited University, City, State, Degree-Types) as well as the latitude and longitude of each school. 

Link: https://directory.ccnecommunity.org/reports/accprog.asp

## Format of Database
Format of database:
* 1 School per line
* "1" = true // has degree
* "0" = false // does not offer degree
* Latitude and Longitude with values = 0, school not identified on google maps (rare)
* "NLN AD" & "NLN BSN" columns will always be zero, as information is ONLY checked for CCNE accreditation, not NLN
* Format of "noCoord": university;city;state;NLN_AD;NLN_BSN;CCNE_BSN;CCNE_MSN;CCNE_DNP
* Format of "Coord": latitude;longitude;university;city;state;NLN_AD;NLN_BSN;CCNE_BSN;CCNE_MSN;CCNE_DNP

Database "CollegeOfNursingDatabasev2.0" (Coord and noCoord) last updated: 3/14/2022
