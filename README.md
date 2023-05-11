# CCNE-Database
A program designed to extract specific data from the CCNE website (Accredited University, City, State, Degree-Types) as well as the latitude and longitude of each school through Google's Geocoding API.

Link: https://directory.ccnecommunity.org/reports/accprog.asp

## Format of Database
Databases last updated: 5/10/2022

Format of database:
* 1 School per line
* "1" = true // has degree
* "0" = false // does not offer degree
* Latitude and Longitude with values = 0, school not identified on google maps (rare)
* Contains CCNE accredited schools only, not NLN accreditations.
* Format of "noCoord": university;city;state;CCNE_BSN;CCNE_MSN;CCNE_DNP
* Format of "Coord": latitude;longitude;university;city;state;CCNE_BSN;CCNE_MSN;CCNE_DNP

## Databases
1. CSV spreadsheet (w/ no Coordinates): [CollegesOfNursing_noCoord.csv](https://github.com/FerminRamos/CCNE-Database/blob/main/CollegesOfNursing_noCoord.csv)
2. CSV spreadsheet (w/ Coordinates): TBD
