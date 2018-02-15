import fml

# 2017, QUARTER 4, WEEK 12 #

PRICES_RAW = """FRI - BLACK PANTHER - FRI ONLY
+FB$501
UNAVAILABLE

SCREENS LOCKED

SAT - BLACK PANTHER - SAT ONLY
+FB$451
UNAVAILABLE

SCREENS LOCKED

SUN - BLACK PANTHER - SUN ONLY
+FB$348
UNAVAILABLE

SCREENS LOCKED

MON - BLACK PANTHER - MON ONLY
+FB$220
UNAVAILABLE

SCREENS LOCKED

PETER RABBIT
+FB$186
UNAVAILABLE

SCREENS LOCKED

FIFTY SHADES FREED
+FB$155
UNAVAILABLE

SCREENS LOCKED

JUMANJI: WELCOME TO THE JUNGLE
+FB$87
UNAVAILABLE

SCREENS LOCKED

THE 15:17 TO PARIS
+FB$68
UNAVAILABLE

SCREENS LOCKED

THE GREATEST SHOWMAN
+FB$51
UNAVAILABLE

SCREENS LOCKED

EARLY MAN
+FB$49
UNAVAILABLE

SCREENS LOCKED

MAZE RUNNER: THE DEATH CURE
+FB$39
UNAVAILABLE

SCREENS LOCKED

SAMSON
+FB$32
UNAVAILABLE

SCREENS LOCKED

WINCHESTER
+FB$31
UNAVAILABLE

SCREENS LOCKED

THE POST
+FB$26
UNAVAILABLE

SCREENS LOCKED

THE SHAPE OF WATER
+FB$25"""

FML_RAW = """"Black Panther" (Friday) - $58.1 million

"Black Panther" (Saturday) - $51.1 million

"Black Panther" (Sunday) - $38.2 million

"Black Panther" (Monday) - $21.4 million

"Peter Rabbit" - $20.9 million

"Fifty Shades Freed" - $18 million

"Jumanji: Welcome to the Jungle" - $9.6 million

"The 15:17 to Paris" - $7.9 million

"The Greatest Showman" - $6 million

"Early Man" - $5.4 million

"Maze Runner: The Death Cure" - $3.6 million

"Winchester" - $2.9 million

"The Post" - $2.4 million

"The Shape of Water" - $2.4 million

"Samson" - $2.2 million"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Black Panther (Disney)	$185.0 M	$185.0 M	NEW	1
2	Peter Rabbit (Sony / Columbia)	$22.5 M	$54.5 M	-10%	2
3	Fifty Shades Freed (Universal)	$17.5 M	$76.0 M	-55%	2
4	Jumanji: Welcome to the Jungle
(Sony / Columbia)	$9.5 M	$379.5 M	-5%	9
5	The 15:17 to Paris (Warner Bros.)	$7.8 M	$26.7 M	-38%	2
6	The Greatest Showman (Fox)	$6.3 M	$156.3 M	-2%	9
7	Early Man (Lionsgate)	$5.8 M	$5.8 M	NEW	1
8	Maze Runner: The Death Cure (Fox)	$3.7 M	$55.5 M	-41%	4
9	Samson (Pure Flix)	$3.5 M	$3.5 M	NEW	1
10	Winchester (Lionsgate / CBS Films)	$2.7 M	$22.7 M	-48%	3
11	The Post (Fox / DreamWorks)	$2.6 M	$77.5 M	-28%	9
12	The Shape of Water (Fox Searchlight)	$2.4 M	$54.3 M	-24%	12"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(12, PRICES_RAW, BOR_RAW, FML_RAW)

