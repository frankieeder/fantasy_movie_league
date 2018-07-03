import fml

# 2017, QUARTER 4, WEEK 10 #

PRICES_RAW = """WINCHESTER
+FB$274
UNAVAILABLE

SCREENS LOCKED

JUMANJI: WELCOME TO THE JUNGLE
+FB$261
UNAVAILABLE

SCREENS LOCKED

MAZE RUNNER: THE DEATH CURE
+FB$230
UNAVAILABLE

SCREENS LOCKED

THE GREATEST SHOWMAN
+FB$167
UNAVAILABLE

SCREENS LOCKED

THE POST
+FB$126
UNAVAILABLE

SCREENS LOCKED

THE SHAPE OF WATER
+FB$114
UNAVAILABLE

SCREENS LOCKED

HOSTILES
+FB$113
UNAVAILABLE

SCREENS LOCKED

DEN OF THIEVES
+FB$90
UNAVAILABLE

SCREENS LOCKED

12 STRONG
+FB$89
UNAVAILABLE

SCREENS LOCKED

PADDINGTON 2
+FB$75
UNAVAILABLE

SCREENS LOCKED

THREE BILLBOARDS OUTSIDE EBBING, MISSOURI
+FB$71
UNAVAILABLE

SCREENS LOCKED

I, TONYA
+FB$61
UNAVAILABLE

SCREENS LOCKED

PHANTOM THREAD
+FB$56
UNAVAILABLE

SCREENS LOCKED

STAR WARS: THE LAST JEDI
+FB$46
UNAVAILABLE

SCREENS LOCKED

FOREVER MY GIRL
+FB$45"""

FML_RAW = """"Winchester" - $14.1 million

"Jumanji: Welcome to the Jungle" - $12.9 million

"Maze Runner: The Death Cure" - $10.6 million

"The Greatest Showman" - $7.9 million

"Hostiles" - $5.8 million

"The Post" - $5.7 million

"Den of Thieves" - $4.8 million

"The Shape of Water" - $4.8 million

"12 Strong" - $4.6 million

"Paddington 2" - $3.8 million

"Three Billboards Outside Ebbing, Missouri" - $3 million

"I, Tonya" - $2.5 million

"Star Wars: The Last Jedi" - $2.4 million

"Phantom Thread" - $2.2 million

"Forever My Girl" - $2 million"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Jumanji: Welcome to the Jungle
(Sony / Columbia)	$11.8 M	$353.5 M	-27%	7
2	Maze Runner: The Death Cure (Fox)	$11.5 M	$41.5 M	-52%	2
3	Winchester (Lionsgate / CBS Films)	$11.0 M	$11.0 M	NEW	1
4	The Greatest Showman (Fox)	$8.5 M	$138.2 M	-11%	7
5	Hostiles (Entertainment Studios)	$5.7 M	$21.4 M	-44%	7
6	The Post (Fox / DreamWorks)	$5.6 M	$67.6 M	-39%	7
7	The Shape of Water (Fox Searchlight)	$5.0 M	$45.4 M	-16%	10
8	Den of Thieves (STXfilms)	$4.4 M	$35.9 M	-49%	3
9	12 Strong (Warner Bros.)	$4.3 M	$36.8 M	-50%	3
10	Paddington 2 (Warner Bros.)	$3.8 M	$37.0 M	-33%	4
11	Three Billboards Outside
Ebbing, Missouri (Fox Searchlight)	$3.0 M	$41.8 M	-22%	13
12	I, Tonya (NEON / 30West)	$2.9 M	$23.0 M	-4%	9
13	Forever My Girl (Roadside)	$2.4 M	$12.7 M	-33%	3
14	Star Wars: The Last Jedi (Disney)	$2.3 M	$614.4 M	-46%	8
15	Coco (Disney)	$2.2 M	$205.3 M	+53%	11"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(10, PRICES_RAW, BOR_RAW, FML_RAW)

