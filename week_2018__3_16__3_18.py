import fml

# 3/16/2018 - 3/18/2018 #

PRICES_RAW = """TOMB RAIDER
+FB$407
UNAVAILABLE

SCREENS LOCKED

BLACK PANTHER
+FB$391
UNAVAILABLE

SCREENS LOCKED

A WRINKLE IN TIME
+FB$241
UNAVAILABLE

SCREENS LOCKED

LOVE, SIMON
+FB$217
UNAVAILABLE

SCREENS LOCKED

GAME NIGHT
+FB$82
UNAVAILABLE

SCREENS LOCKED

THE STRANGERS: PREY AT NIGHT
+FB$78
UNAVAILABLE

SCREENS LOCKED

PETER RABBIT
+FB$71
UNAVAILABLE

SCREENS LOCKED

RED SPARROW
+FB$67
UNAVAILABLE

SCREENS LOCKED

DEATH WISH
+FB$54
UNAVAILABLE

SCREENS LOCKED

I CAN ONLY IMAGINE
+FB$41
UNAVAILABLE

SCREENS LOCKED

ANNIHILATION
+FB$29
UNAVAILABLE

SCREENS LOCKED

7 DAYS IN ENTEBBE
+FB$29
UNAVAILABLE

SCREENS LOCKED

JUMANJI: WELCOME TO THE JUNGLE
+FB$23
UNAVAILABLE

SCREENS LOCKED

GRINGO
+FB$21
UNAVAILABLE

SCREENS LOCKED

THE HURRICANE HEIST
+FB$19"""

FML_RAW = """"Tomb Raider" - $27.8 million

"Black Panther" - $25.7 million

"A Wrinkle in Time" - $16.4 million

"Love, Simon" - $13.3 million

"Game Night" - $5.6 million

"The Strangers: Prey at Night" - $4.6 million

"Peter Rabbit" - $4.5 million

"Red Sparrow" - $4.3 million

"Death Wish" - $3.3 million

"I Can Only Imagine" - $2.8 million

"Annihilation" - $2 million

"Jumanji: Welcome to the Jungle" - $1.5 million

"Gringo" - $1.3 million

"The Hurricane Heist" - $1.2 million

"7 Days in Entebbe" - $972,000"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Black Panther (Disney)	$27.0 M	$604.5 M	-34%	5
2	Tomb Raider (Warner / MGM)	$23.0 M	$23.0 M	NEW	1
3	A Wrinkle in Time (Disney)	$17.0 M	$61.7 M	-49%	2
4	Love, Simon (Fox)	$13.0 M	$13.0 M	NEW	1
5	I Can Only Imagine (Roadside)	$8.5 M	$8.5 M	NEW	1
6	Game Night (Warner / New Line)	$6.2 M	$54.9 M	-21%	4
7	Peter Rabbit (Sony / Columbia)	$5.3 M	$102.4 M	-22%	6
8	The Strangers: Prey at Night
(Aviron Pictures)	$4.4 M	$18.0 M	-58%	2
9	Red Sparrow (Fox)	$4.3 M	$39.4 M	-49%	3
10	Death Wish (MGM)	$3.5 M	$30.0 M	-47%	3"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(2018316, PRICES_RAW, BOR_RAW, FML_RAW)

