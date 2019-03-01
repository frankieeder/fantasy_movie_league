import fml

# 1/4/2019 - 1/6/2019 #

PRICES_RAW = """AQUAMAN
+$402
UNAVAILABLE

SCREENS LOCKED

MARY POPPINS RETURNS
+$251
UNAVAILABLE

SCREENS LOCKED

ESCAPE ROOM
+$201
UNAVAILABLE

SCREENS LOCKED

BUMBLEBEE
+$167
UNAVAILABLE

SCREENS LOCKED

SPIDER-MAN: INTO THE SPIDER-VERSE
+$157
UNAVAILABLE

SCREENS LOCKED

THE MULE
+$116
UNAVAILABLE

SCREENS LOCKED

VICE
+$66
UNAVAILABLE

SCREENS LOCKED

SECOND ACT
+$55
UNAVAILABLE

SCREENS LOCKED

RALPH BREAKS THE INTERNET
+$54
UNAVAILABLE

SCREENS LOCKED

HOLMES & WATSON
+$54
UNAVAILABLE

SCREENS LOCKED

THE GRINCH
+$24
UNAVAILABLE

SCREENS LOCKED

GREEN BOOK
+$23
UNAVAILABLE

SCREENS LOCKED

MARY QUEEN OF SCOTS
+$23
UNAVAILABLE

SCREENS LOCKED

BOHEMIAN RHAPSODY
+$22
UNAVAILABLE

SCREENS LOCKED

THE FAVOURITE
+$20"""

FML_RAW = """"Aquaman" - $27.9 million 
"Mary Poppins Returns" - $18.7 million 
"Escape Room" - $13.8 million 
"Bumblebee" - $12.2 million 
"Spider-Man: Into the Spider-Verse" - $10.9 million 
"The Mule" - $8.3 million 
"Vice" - $4.4 million 
"Second Act" - $4.2 million 
"Ralph Breaks the Internet" - $4 million 
"Holmes & Watson" - $3.2 million 
"The Grinch" - $1.6 million 
"Mary Queen of Scots" - $1.6 million 
"Bohemian Rhapsody" - $1.5 million 
"The Favourite" - $1.5 million 
"Green Book" - $1.4 million"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Aquaman (Warner Bros.)	$30.5 M	$260.0 M	-41%	3
2	Mary Poppins Returns (Disney)	$18.0 M	$140.5 M	-37%	3
3	Bumblebee (Paramount)	$13.7 M	$98.7 M	-34%	3
4	Escape Room (Sony / Columbia)	$13.5 M	$13.5 M	NEW	1
5	Spider-Man: Into the Spider-Verse
(Sony / Columbia)	$12.7 M	$132.8 M	-32%	4
6	The Mule (Warner Bros.)	$8.5 M	$80.8 M	-30%	4
7	Vice (Annapurna Pictures)	$4.9 M	$28.9 M	-37%	2
8	Second Act (STXfilms)	$4.8 M	$32.8 M	-35%	3
9	Ralph Breaks the Internet (Disney)	$4.7 M	$186.8 M	-30%	7
10	Holmes & Watson (Sony / Columbia)	$3.7 M	$28.7 M	-50%	2"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(201914, PRICES_RAW, BOR_RAW, FML_RAW)

