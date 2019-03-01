import fml

# 1/18/2019 - 1/21/2019 #

PRICES_RAW = """RI-SAT: GLASS
+$586
UNAVAILABLE

SCREENS LOCKED

SUN-MON: GLASS
+$336
UNAVAILABLE

SCREENS LOCKED

THE UPSIDE
+$212
UNAVAILABLE

SCREENS LOCKED

AQUAMAN
+$190
UNAVAILABLE

SCREENS LOCKED

A DOG'S WAY HOME
+$128
UNAVAILABLE

SCREENS LOCKED

SPIDER-MAN: INTO THE SPIDER-VERSE
+$126
UNAVAILABLE

SCREENS LOCKED

DRAGON BALL SUPER: BROLY
+$87
UNAVAILABLE

SCREENS LOCKED

MARY POPPINS RETURNS
+$73
UNAVAILABLE

SCREENS LOCKED

BUMBLEBEE
+$70
UNAVAILABLE

SCREENS LOCKED

ESCAPE ROOM
+$67
UNAVAILABLE

SCREENS LOCKED

BOHEMIAN RHAPSODY
+$62
UNAVAILABLE

SCREENS LOCKED

THE MULE
+$56
UNAVAILABLE

SCREENS LOCKED

ON THE BASIS OF SEX
+$56
UNAVAILABLE

SCREENS LOCKED

IF BEALE STREET COULD TALK
+$51
UNAVAILABLE

SCREENS LOCKED

GREEN BOOK
+$39"""

FML_RAW = """"Glass" (Friday-Saturday) - $46.4 million
"Glass" (Sunday-Monday) - $25.7 million
"The Upside" - $15.4 million
"Aquaman" - $13.8 million
"A Dog's Way Home" - $9.1 million
"Spider-Man: Into the Spider-Verse" - $8.3 million
"Dragon Ball Super: Broly" - $5.6 million
"Mary Poppins Returns" - $5.2 million
"Bumblebee" - $4.8 million
"Escape Room" - $4.7 million
"On the Basis of Sex" - $4.2 million
"The Mule" - $4.1 million
"Bohemian Rhapsody" - $4.1 million
"If Beale Street Could Talk" - $3.4 million
"Green Book" - $3 million"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Glass (Universal)	$57.0 M	$57.0 M	NEW	1
2	The Upside (STXfilms)	$18.5 M	$46.8 M	-9%	2
3	Aquaman (Warner Bros.)	$13.7 M	$307.8 M	-21%	5
4	A Dog's Way Home (Sony / Columbia)	$10.7 M	$25.0 M	-5%	2
5	Spider-Man: Into the Spider-Verse
(Sony / Columbia)	$9.2 M	$160.2 M	+2%	6
6	Dragon Ball Super: Broly
(Funimation Films)	$6.3 M	$15.0 M	NEW	1
7	Mary Poppins Returns (Disney)	$6.2 M	$159.7 M	-19%	5
8	Escape Room (Sony / Columbia)	$6.1 M	$41.5 M	-32%	3
9	Bumblebee (Paramount)	$5.9 M	$117.2 M	-18%	5
10	On the Basis of Sex (Focus)	$4.8 M	$17.7 M	-21%	4
11	The Mule (Warner Bros.)	$4.4 M	$97.9 M	-22%	6"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(2018118, PRICES_RAW, BOR_RAW, FML_RAW)
