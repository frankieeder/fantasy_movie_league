import fml

# 2017, QUARTER 4, WEEK 13 #

PRICES_RAW = """SAT - BLACK PANTHER - SAT ONLY
+FB$534
UNAVAILABLE

SCREENS LOCKED

SUN - BLACK PANTHER - SUN ONLY
+FB$395
UNAVAILABLE

SCREENS LOCKED

FRI - BLACK PANTHER - FRI ONLY
+FB$334
UNAVAILABLE

SCREENS LOCKED

GAME NIGHT
+FB$201
UNAVAILABLE

SCREENS LOCKED

PETER RABBIT
+FB$167
UNAVAILABLE

SCREENS LOCKED

ANNIHILATION
+FB$154
UNAVAILABLE

SCREENS LOCKED

FIFTY SHADES FREED
+FB$100
UNAVAILABLE

SCREENS LOCKED

JUMANJI: WELCOME TO THE JUNGLE
+FB$87
UNAVAILABLE

SCREENS LOCKED

THE 15:17 TO PARIS
+FB$62
UNAVAILABLE

SCREENS LOCKED

THE GREATEST SHOWMAN
+FB$55
UNAVAILABLE

SCREENS LOCKED

EVERY DAY
+FB$45
UNAVAILABLE

SCREENS LOCKED

EARLY MAN
+FB$26
UNAVAILABLE

SCREENS LOCKED

MAZE RUNNER: THE DEATH CURE
+FB$17
UNAVAILABLE

SCREENS LOCKED

THE POST
+FB$16
UNAVAILABLE

SCREENS LOCKED

THE SHAPE OF WATER
+FB$15
UNAVAILABLE

SCREENS LOCKED
"""

FML_RAW = """"Black Panther" (Saturday) - $42.8 million

"Black Panther" (Sunday) - $30.8 million

"Black Panther" (Friday) - $28.2 million

"Game Night" - $16.3 million

"Peter Rabbit" - $11.6 million

"Annihilation" - $10.4 million

"Fifty Shades Freed" - $6.9 million

"Jumanji: Welcome to the Jungle" - $5.2 million

"The 15:17 to Paris" - $4.5 million

"The Greatest Showman" - $3.9 million

"Every Day" - $2.9 million

"Early Man" - $2.15 million

"Maze Runner: The Death Cure" - $1.2 million

"The Post" - $1.2 million

"The Shape of Water" - $1.1 million"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Black Panther (Disney)	$108.0 M	$400.0 M	-47%	2
2	Game Night (Warner / New Line)	$15.0 M	$15.0 M	NEW	1
3	Peter Rabbit (Sony / Columbia)	$12.0 M	$70.7 M	-31%	3
4	Annihilation (Paramount)	$11.0 M	$11.0 M	NEW	1
5	Fifty Shades Freed (Universal)	$7.0 M	$89.5 M	-60%	3
6	Jumanji: Welcome to the Jungle
(Sony / Columbia)	$6.0 M	$387.5 M	-24%	10
7	The 15:17 to Paris (Warner Bros.)	$4.7 M	$33.4 M	-38%	3
8	The Greatest Showman (Fox)	$4.0 M	$161.3 M	-21%	10
9	Every Day (Orion Pictures)	$3.2 M	$3.2 M	NEW	1
10	Early Man (Lionsgate)	$2.1 M	$7.2 M	-34%	2"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(13, PRICES_RAW, BOR_RAW, FML_RAW)
