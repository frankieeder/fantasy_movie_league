import fml

# 2017, QUARTER q4, WEEK 11 #

PRICES_RAW = """FIFTY SHADES FREED
+FB$556
UNAVAILABLE

SCREENS LOCKED

PETER RABBIT
+FB$276
UNAVAILABLE

SCREENS LOCKED

THE 15:17 TO PARIS
+FB$221
UNAVAILABLE

SCREENS LOCKED

JUMANJI: WELCOME TO THE JUNGLE
+FB$126
UNAVAILABLE

SCREENS LOCKED

THE GREATEST SHOWMAN
+FB$101
UNAVAILABLE

SCREENS LOCKED

MAZE RUNNER: THE DEATH CURE
+FB$83
UNAVAILABLE

SCREENS LOCKED

WINCHESTER
+FB$66
UNAVAILABLE

SCREENS LOCKED

THE SHAPE OF WATER
+FB$51
UNAVAILABLE

SCREENS LOCKED

THE POST
+FB$50
UNAVAILABLE

SCREENS LOCKED

HOSTILES
+FB$46
UNAVAILABLE

SCREENS LOCKED

12 STRONG
+FB$43
UNAVAILABLE

SCREENS LOCKED

DEN OF THIEVES
+FB$40
UNAVAILABLE

SCREENS LOCKED

THREE BILLBOARDS OUTSIDE EBBING, MISSOURI
+FB$35
UNAVAILABLE

SCREENS LOCKED

I, TONYA
+FB$30
UNAVAILABLE

SCREENS LOCKED

DARKEST HOUR
+FB$29"""

FML_RAW = """"Fifty Shades Freed" - $38.4 million

"Peter Rabbit" - $18.7 million

"The 15:17 to Paris" - $15.1 million

"Jumanji: Welcome to the Jungle" - $7.2 million

"The Greatest Showman" - $6 million

"Maze Runner: The Death Cure" - $5.1 million

"Winchester" - $4 million

"The Shape of Water" - $3.3 million

"The Post" - $3.2 million

"Hostiles" - $2.7 million

"12 Strong" - $2.6 million

"Den of Thieves" - $2.3 million

"Three Billboards Outside Ebbing, Missouri" - $2.2 million

"I, Tonya" - $1.8 million

"Darkest Hour" - $1.7 million"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Fifty Shades Freed (Universal)	$40.0 M	$40.0 M	NEW	1
2	Peter Rabbit (Sony / Columbia)	$20.0 M	$20.0 M	NEW	1
3	The 15:17 to Paris (Warner Bros.)	$12.0 M	$12.0 M	NEW	1
4	Jumanji: Welcome to the Jungle
(Sony / Columbia)	$9.3 M	$365.0 M	-15%	8
5	The Greatest Showman (Fox)	$6.5 M	$146.5 M	-16%	8
6	Maze Runner: The Death Cure (Fox)	$5.5 M	$48.5 M	-47%	3
7	Winchester (Lionsgate / CBS Films)	$5.0 M	$17.1 M	-46%	2
8	The Post (Fox / DreamWorks)	$3.8 M	$73.1 M	-27%	8
9	The Shape of Water (Fox Searchlight)	$3.7 M	$50.5 M	-17%	11
10	Hostiles (Entertainment Studios)	$3.3 M	$26.4 M	-35%	8
11	Den of Thieves (STXfilms)	$2.8 M	$40.9 M	-38%	4
12	12 Strong (Warner Bros.)	$2.6 M	$41.8 M	-45%	4
13	Three Billboards Outside
Ebbing, Missouri (Fox Searchlight)	$2.5 M	$45.6 M	-17%	14"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(11, PRICES_RAW, BOR_RAW, FML_RAW)

