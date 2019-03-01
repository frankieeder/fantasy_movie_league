import fml

# 2/1/2019 - 2/3/2019 #

PRICES_RAW = """GLASS
+$215
UNAVAILABLE

SCREENS LOCKED

THE UPSIDE
+$203
UNAVAILABLE

SCREENS LOCKED

MISS BALA
+$158
UNAVAILABLE

SCREENS LOCKED

AQUAMAN
+$103
UNAVAILABLE

SCREENS LOCKED

GREEN BOOK
+$102
UNAVAILABLE

SCREENS LOCKED

SPIDER-MAN: INTO THE SPIDER-VERSE
+$99
UNAVAILABLE

SCREENS LOCKED

THE KID WHO WOULD BE KING
+$93
UNAVAILABLE

SCREENS LOCKED

A DOG'S WAY HOME
+$72
UNAVAILABLE

SCREENS LOCKED

ESCAPE ROOM
+$59
UNAVAILABLE

SCREENS LOCKED

THE FAVOURITE
+$50
UNAVAILABLE

SCREENS LOCKED

SERENITY
+$43
UNAVAILABLE

SCREENS LOCKED

MARY POPPINS RETURNS
+$41
UNAVAILABLE

SCREENS LOCKED

BOHEMIAN RHAPSODY
+$38
UNAVAILABLE

SCREENS LOCKED

BUMBLEBEE
+$38
UNAVAILABLE

SCREENS LOCKED

VICE
+$30"""

FML_RAW = """"Glass" - $9.8 million 
"The Upside" - $9.1 million 
"Miss Bala" - $5.8 million 
"Aquaman" - $5 million 
"Spider-Man: Into the Spider-Verse" - $4.6 million 
"Green Book" - $4.6 million 
"The Kid Who Would Be King" - $4.2 million 
"A Dog's Way Home" - $3.5 million 
"Escape Room" - $2.7 million
"The Favourite" - $2.2 million 
"Serenity" - $2.1 million 
"Mary Poppins Returns" - $2 million 
"Bohemian Rhapsody" - $1.9 million 
"Bumblebee" - $1.8 million 
"Vice" - $1.3 million"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Miss Bala (Sony / Columbia)	$10.0 M	$10.0 M	NEW	1
2	Glass (Universal)	$9.8 M	$88.7 M	-48%	3
3	The Upside (STXfilms)	$8.0 M	$74.5 M	-33%	4
4	Spider-Man: Into the Spider-Verse
(Sony / Columbia)	$4.6 M	$175.4 M	-25%	8
5	Aquaman (Warner Bros.)	$4.5 M	$323.1 M	-38%	7
6	Green Book (Universal / DreamWorks)	$4.4 M	$55.9 M	-20%	12
7	The Kid Who Would Be King (Fox)	$4.3 M	$13.2 M	-40%	2
8	They Shall Not Grow Old (Warner Bros.)	$4.0 M	$12.3 M	NEW	1
9	A Dog's Way Home (Sony / Columbia)	$3.5 M	$35.7 M	-31%	4
10	Escape Room (Sony / Columbia)	$2.7 M	$51.8 M	-35%	5
11	Mary Poppins Returns (Disney)	$2.0 M	$168.2 M	-40%	7"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(201921, PRICES_RAW, BOR_RAW, FML_RAW)

