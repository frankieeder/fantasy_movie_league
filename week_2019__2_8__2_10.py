import fml

# 2/8/2019 - 2/10/2019 #

PRICES_RAW = """THE LEGO MOVIE 2: THE SECOND PART
+$703
UNAVAILABLE

SCREENS LOCKED

WHAT MEN WANT
+$342
UNAVAILABLE

SCREENS LOCKED

COLD PURSUIT
+$186
UNAVAILABLE

SCREENS LOCKED

THE PRODIGY
+$126
UNAVAILABLE

SCREENS LOCKED

THE UPSIDE
+$88
UNAVAILABLE

SCREENS LOCKED

GLASS
+$80
UNAVAILABLE

SCREENS LOCKED

GREEN BOOK
+$48
UNAVAILABLE

SCREENS LOCKED

SPIDER-MAN: INTO THE SPIDER-VERSE
+$47
UNAVAILABLE

SCREENS LOCKED

MISS BALA
+$47
UNAVAILABLE

SCREENS LOCKED

AQUAMAN
+$46
UNAVAILABLE

SCREENS LOCKED

A DOG'S WAY HOME
+$34
UNAVAILABLE

SCREENS LOCKED

THE KID WHO WOULD BE KING
+$34
UNAVAILABLE

SCREENS LOCKED

ESCAPE ROOM
+$29
UNAVAILABLE

SCREENS LOCKED

BOHEMIAN RHAPSODY
+$18
UNAVAILABLE

SCREENS LOCKED

MARY POPPINS RETURNS
+$17"""

FML_RAW = """"The Lego Movie 2: The Second Part" - $48.6 million 
"What Men Want" - $26.4 million 
"Cold Pursuit" - $12.8 million 
"The Prodigy" - $6.1 million 
"The Upside" - $5.8 million 
"Glass" - $4.9 million 
"Green Book" - $3.3 million 
"Miss Bala" - $3.2 million 
"Spider-Man: Into the Spider-Verse" - $3.1 million 
"Aquaman" - $3 million 
"A Dog's Way Home" - $2.5 million 
"The Kid Who Would Be King" - $2.3 million 
"Escape Room" - $1.8 million 
"Bohemian Rhapsody" - $1.3 million 
"Mary Poppins Returns" - $1.2 million
"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	The LEGO Movie 2: The Second Part
(Warner Bros.)	$52.5 M	$52.5 M	NEW	1
2	What Men Want (Paramount)	$25.0 M	$25.0 M	NEW	1
3	Cold Pursuit (Lionsgate / Summit)	$12.7 M	$12.7 M	NEW	1
4	The Prodigy (Orion Films)	$7.5 M	$7.5 M	NEW	1
5	The Upside (STXfilms)	$6.7 M	$85.5 M	-23%	5
6	Glass (Universal)	$5.5 M	$97.6 M	-42%	4
7	Green Book (Universal / DreamWorks)	$3.6 M	$61.6 M	-17%	13
8	Miss Bala (Sony / Columbia)	$3.5 M	$12.8 M	-49%	2
9	Aquaman (Warner Bros.)	$3.4 M	$328.7 M	-30%	8
10	Spider-Man: Into the Spider-Verse
(Sony / Columbia)	$3.0 M	$179.9 M	-34%	9
11	The Kid Who Would Be King (Fox)	$2.4 M	$16.7 M	-43%	3
12	A Dog's Way Home (Sony / Columbia)	$2.3 M	$39.4 M	-36%	5"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(201928, PRICES_RAW, BOR_RAW, FML_RAW)

