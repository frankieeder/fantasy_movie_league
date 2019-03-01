import fml

# 12/21/2018 - 12/23/2018 #

PRICES_RAW = """AQUAMAN
+$669
UNAVAILABLE

SCREENS LOCKED

MARY POPPINS RETURNS
+$334
UNAVAILABLE

SCREENS LOCKED

BUMBLEBEE
+$222
UNAVAILABLE

SCREENS LOCKED

SPIDER-MAN: INTO THE SPIDER-VERSE
+$164
UNAVAILABLE

SCREENS LOCKED

THE MULE
+$82
UNAVAILABLE

SCREENS LOCKED

THE GRINCH
+$75
UNAVAILABLE

SCREENS LOCKED

SECOND ACT
+$58
UNAVAILABLE

SCREENS LOCKED

RALPH BREAKS THE INTERNET
+$43
UNAVAILABLE

SCREENS LOCKED

WELCOME TO MARWEN
+$32
UNAVAILABLE

SCREENS LOCKED

MORTAL ENGINES
+$31
UNAVAILABLE

SCREENS LOCKED

MARY QUEEN OF SCOTS
+$25
UNAVAILABLE

SCREENS LOCKED

BOHEMIAN RHAPSODY
+$24
UNAVAILABLE

SCREENS LOCKED

CREED II
+$24
UNAVAILABLE

SCREENS LOCKED

THE FAVOURITE
+$23
UNAVAILABLE

SCREENS LOCKED

INSTANT FAMILY
+$19"""

FML_RAW = """"Aquaman" - $74.3 million 
"Mary Poppins Returns" - $39.8 million 
"Bumblebee" - $26.2 million 
"Spider-Man: Into the Spider-Verse" - $19.8 million 
"The Mule" - $10.2 million 
"The Grinch" - $8.9 million 
"Second Act" - $7.2 million 
"Ralph Breaks the Internet" - $5 million 
"Welcome to Marwen" - $3.8 million 
"Mortal Engines" - $3.5 million 
"Mary Queen of Scots" - $3 million
"Bohemian Rhapsody" - $2.9 million 
"Creed II" - $2.8 million 
"The Favourite" - $2.7 million 
"Instant Family" - $2.3 million"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Aquaman (Warner Bros.)	$75.0 M	$75.0 M	NEW	1
2	Mary Poppins Returns (Disney)	$36.0 M	$52.0 M	NEW	1
3	Bumblebee (Paramount)	$20.0 M	$20.0 M	NEW	1
4	Spider-Man: Into the Spider-Verse
(Sony / Columbia)	$17.5 M	$66.0 M	-51%	2
5	The Mule (Warner Bros.)	$10.5 M	$36.8 M	-40%	2
6	Dr. Seuss' The Grinch (Universal)	$9.0 M	$253.7 M	-23%	7
7	Second Act (STXfilms)	$7.0 M	$7.0 M	NEW	1
8	Ralph Breaks the Internet (Disney)	$5.5 M	$162.7 M	-41%	5
9	Welcome to Marwen (Universal / DreamWorks)	$4.4 M	$4.4 M	NEW	1
10	Mortal Engines (Universal)	$3.2 M	$13.7 M	-58%	2
11	The Favourite (Fox Searchlight)	$2.9 M	$11.0 M	+11%	5
12	Mary Queen of Scots (Focus)	$2.7 M	$4.0 M	+286%	3"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(20181221, PRICES_RAW, BOR_RAW, FML_RAW)

