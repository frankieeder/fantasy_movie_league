import fml

# 12/28/2018 - 12/30/2018 #

PRICES_RAW = """AQUAMAN
+$558
UNAVAILABLE

SCREENS LOCKED

MARY POPPINS RETURNS
+$357
UNAVAILABLE

SCREENS LOCKED

BUMBLEBEE
+$274
UNAVAILABLE

SCREENS LOCKED

SPIDER-MAN: INTO THE SPIDER-VERSE
+$223
UNAVAILABLE

SCREENS LOCKED

THE MULE
+$144
UNAVAILABLE

SCREENS LOCKED

HOLMES & WATSON
+$143
UNAVAILABLE

SCREENS LOCKED

THE GRINCH
+$132
UNAVAILABLE

SCREENS LOCKED

VICE
+$104
UNAVAILABLE

SCREENS LOCKED

SECOND ACT
+$81
UNAVAILABLE

SCREENS LOCKED

RALPH BREAKS THE INTERNET
+$71
UNAVAILABLE

SCREENS LOCKED

MARY QUEEN OF SCOTS
+$35
UNAVAILABLE

SCREENS LOCKED

THE FAVOURITE
+$31
UNAVAILABLE

SCREENS LOCKED

WELCOME TO MARWEN
+$25
UNAVAILABLE

SCREENS LOCKED

BOHEMIAN RHAPSODY
+$22
UNAVAILABLE

SCREENS LOCKED

GREEN BOOK
+$19"""

FML_RAW = """"Aquaman" - $51.8 million 
"Mary Poppins Returns" - $31.4 million 
"Bumblebee" - $26.3 million 
"Spider-Man: Into the Spider-Verse" - $22 million
"The Mule" - $12.4 million 
"Holmes & Watson" - $11.3 million 
"The Grinch" - $11.2 million 
"Second Act" - $8.1 million 
"Vice" - $7.2 million 
"Ralph Breaks the Internet" - $5.8 million 
"Mary Queen of Scots" - $2.7 million 
"The Favourite" - $2.5 million 
"Welcome to Marwen" - $2.2 million 
"Bohemian Rhapsody" - $1.8 million 
"Green Book" - $1.6 million"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Aquaman (Warner Bros.)	$52.0 M	$187.0 M	-24%	2
2	Mary Poppins Returns (Disney)	$29.0 M	$98.0 M	+23%	2
3	Bumblebee (Paramount)	$19.0 M	$62.5 M	-12%	2
4	Spider-Man: Into the Spider-Verse
(Sony / Columbia)	$18.5 M	$103.5 M	+11%	3
5	Holmes & Watson (Sony / Columbia)	$12.5 M	$27.0 M	NEW	1
6	The Mule (Warner Bros.)	$11.5 M	$59.5 M	+21%	3
7	Vice (Annapurna Pictures)	$9.7 M	$21.5 M	NEW	1
8	Second Act (STXfilms)	$7.9 M	$21.8 M	+22%	2
9	Dr. Seuss' The Grinch (Universal)	$7.1 M	$270.8 M	-17%	8
10	Ralph Breaks the Internet (Disney)	$5.5 M	$175.0 M	+17%	6"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(20181228, PRICES_RAW, BOR_RAW, FML_RAW)

