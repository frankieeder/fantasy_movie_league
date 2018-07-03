import fml

# 3/9/2018 - 3/11/2018 #

PRICES_RAW = """A WRINKLE IN TIME
+FB$641
UNAVAILABLE

SCREENS LOCKED

BLACK PANTHER
+FB$575
UNAVAILABLE

SCREENS LOCKED

THE STRANGERS: PREY AT NIGHT
+FB$126
UNAVAILABLE

SCREENS LOCKED

RED SPARROW
+FB$121
UNAVAILABLE

SCREENS LOCKED

PETER RABBIT
+FB$107
UNAVAILABLE

SCREENS LOCKED

GAME NIGHT
+FB$97
UNAVAILABLE

SCREENS LOCKED

DEATH WISH
+FB$85
UNAVAILABLE

SCREENS LOCKED

THE HURRICANE HEIST
+FB$78
UNAVAILABLE

SCREENS LOCKED

THE SHAPE OF WATER
+FB$48
UNAVAILABLE

SCREENS LOCKED

GRINGO
+FB$48
UNAVAILABLE

SCREENS LOCKED

JUMANJI: WELCOME TO THE JUNGLE
+FB$47
UNAVAILABLE

SCREENS LOCKED

THOROUGHBREDS
+FB$47
UNAVAILABLE

SCREENS LOCKED

ANNIHILATION
+FB$44
UNAVAILABLE

SCREENS LOCKED

THE GREATEST SHOWMAN
+FB$29
UNAVAILABLE

SCREENS LOCKED

FIFTY SHADES FREED
+FB$25"""

FML_RAW = """"A Wrinkle in Time" - $42.8 million

"Black Panther" - $40.2 million

"Red Sparrow" - $8.1 million

"The Strangers: Prey at Night" - $7.9 million

"Peter Rabbit" - $7.5 million

"Game Night" - $7.2 million

"Death Wish" - $6.1 million

"The Hurricane Heist" - $5.6 million

"The Shape of Water" - $3.4 million

"Jumanji: Welcome to the Jungle" - $3.1 million

"Annihilation" - $3.1 million

"Gringo" - $3.1 million

"Thoroughbreds" - $2.6 million

"The Greatest Showman" - $2.1 million

"Fifty Shades Freed" - $1.6 million"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	A Wrinkle in Time (Disney)	$43.0 M	$43.0 M	NEW	1
2	Black Panther (Disney)	$38.5 M	$559.7 M	-42%	4
3	The Strangers: Prey at Night
(Aviron Pictures)	$8.5 M	$8.5 M	NEW	1
4	Red Sparrow (Fox)	$8.0 M	$31.0 M	-53%	2
5	Peter Rabbit (Sony / Columbia)	$7.0 M	$93.6 M	-30%	5
6	Game Night (Warner / New Line)	$6.8 M	$43.8 M	-35%	3
7	Death Wish (MGM)	$6.5 M	$23.9 M	-50%	2
8	The Hurricane Heist (Entertainment Studios)	$4.0 M	$4.0 M	NEW	1
9	Gringo (STXfilms / Amazon)	$3.8 M	$3.8 M	NEW	1
10	Jumanji: Welcome to the Jungle
(Sony / Columbia)	$3.2 M	$397.7 M	-28%	12
11	The Shape of Water (Fox Searchlight)	$3.1 M	$61.7 M	+112%	15
12	Annihilation (Paramount)	$3.0 M	$25.9 M	-47%	3"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(201839, PRICES_RAW, BOR_RAW, FML_RAW)
