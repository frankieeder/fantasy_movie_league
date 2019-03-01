import fml

# 1/25/2019 - 1/27/2019 #

PRICES_RAW = """GLASS
+$337
UNAVAILABLE

SCREENS LOCKED

THE KID WHO WOULD BE KING
+$204
UNAVAILABLE

SCREENS LOCKED

THE UPSIDE
+$183
UNAVAILABLE

SCREENS LOCKED

DRAGON BALL SUPER: BROLY
+$126
UNAVAILABLE

SCREENS LOCKED

AQUAMAN
+$113
UNAVAILABLE

SCREENS LOCKED

SPIDER-MAN: INTO THE SPIDER-VERSE
+$109
UNAVAILABLE

SCREENS LOCKED

SERENITY
+$105
UNAVAILABLE

SCREENS LOCKED

A DOG'S WAY HOME
+$76
UNAVAILABLE

SCREENS LOCKED

GREEN BOOK
+$71
UNAVAILABLE

SCREENS LOCKED

BOHEMIAN RHAPSODY
+$57
UNAVAILABLE

SCREENS LOCKED

ESCAPE ROOM
+$57
UNAVAILABLE

SCREENS LOCKED

THE FAVOURITE
+$56
UNAVAILABLE

SCREENS LOCKED

MARY POPPINS RETURNS
+$54
UNAVAILABLE

SCREENS LOCKED

BUMBLEBEE
+$48
UNAVAILABLE

SCREENS LOCKED

ON THE BASIS OF SEX
+$41"""

FML_RAW = """"Glass" - $19.5 million 
"The Kid Who Would Be King" - $10.8 million 
"The Upside" - $9.8 million 
"Aquaman" - $6.4 million 
"Spider-Man: Into the Spider-Verse" - $5.2 million 
"Serenity" - $5.1 million 
"Dragon Ball Super: Broly" - $4.5 million 
"A Dog's Way Home" - $4.2 million 
"Green Book" - $3.4 million 
"Bohemian Rhapsody" - $3.1 million 
"Escape Room" - $2.8 million 
"Bumblebee" - $2.7 million 
"Mary Poppins Returns" - $2.5 million 
"On the Basis of Sex" - $2.2 million 
"The Favourite" - $1.9 million"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Glass (Universal)	$18.0 M	$73.0 M	-55%	2
2	The Upside (STXfilms)	$10.2 M	$61.0 M	-32%	3
3	The Kid Who Would Be King (Fox)	$9.5 M	$9.5 M	NEW	1
4	Aquaman (Warner Bros.)	$7.0 M	$316.3 M	-31%	6
5	Serenity (Aviron Pictures)	$6.7 M	$6.7 M	NEW	1
6	Spider-Man: Into the Spider-Verse
(Sony / Columbia)	$6.3 M	$169.3 M	-17%	7
7	A Dog's Way Home (Sony / Columbia)	$5.0 M	$30.6 M	-30%	3
8	Green Book (Universal / DreamWorks)	$4.8 M	$48.4 M	+122%	11
9	Dragon Ball Super: Broly
(Funimation Films)	$4.5 M	$29.8 M	-54%	2
10	Escape Room (Sony / Columbia)	$3.4 M	$46.9 M	-39%	4
11	Mary Poppins Returns (Disney)	$3.3 M	$165.2 M	-37%	6"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(2019125, PRICES_RAW, BOR_RAW, FML_RAW)

