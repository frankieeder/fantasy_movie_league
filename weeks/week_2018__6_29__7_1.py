import fml

# 6/29/2018 - 7/1/2018 #

PRICES_RAW = """INCREDIBLES 2
+FB$591
UNAVAILABLE

SCREENS LOCKED

SAT: JURASSIC WORLD: FALLEN KINGDOM
+FB$356
UNAVAILABLE

SCREENS LOCKED

SUN: JURASSIC WORLD: FALLEN KINGDOM
+FB$278
UNAVAILABLE

SCREENS LOCKED

UNCLE DREW
+FB$275
UNAVAILABLE

SCREENS LOCKED

FRI: JURASSIC WORLD: FALLEN KINGDOM
+FB$266
UNAVAILABLE

SCREENS LOCKED

SICARIO: DAY OF THE SOLDADO
+FB$201
UNAVAILABLE

SCREENS LOCKED

OCEAN'S 8
+FB$97
UNAVAILABLE

SCREENS LOCKED

TAG
+FB$64
UNAVAILABLE

SCREENS LOCKED

DEADPOOL 2
+FB$41
UNAVAILABLE

SCREENS LOCKED

SOLO: A STAR WARS STORY
+FB$31
UNAVAILABLE

SCREENS LOCKED

SANJU
+FB$30
UNAVAILABLE

SCREENS LOCKED

HEREDITARY
+FB$24
UNAVAILABLE

SCREENS LOCKED

WON'T YOU BE MY NEIGHBOR?
+FB$24
UNAVAILABLE

SCREENS LOCKED

SUPERFLY
+FB$22
UNAVAILABLE

SCREENS LOCKED

AVENGERS: INFINITY WAR
+FB$18"""

FML_RAW = """"Incredibles 2" - $42.8 million


"Jurassic World: Fallen Kingdom" (Saturday) - $25.6 million


"Jurassic World: Fallen Kingdom" (Sunday) - $20.2 million


"Uncle Drew" - $15.4 million


"Jurassic World: Fallen Kingdom" (Friday) - $16.3 million


"Sicario: Day of the Soldado" - $13.8 million


"Ocean's 8" - $7 million


"Tag" - $4.8 million


"Deadpool 2" - $3.3 million


"Solo: A Star Wars Story" - $2.3 million


"Hereditary" - $1.9 million


"Sanju" - $1.9 million


"Won't You Be My Neighbor?" - $1.8 million


"Superfly" - $1.5 million


"Avengers: Infinity War" - $1.3 million"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Jurassic World: Fallen Kingdom (Universal)	$63.0 M	$267.5 M	-57%	2
2	Incredibles 2 (Disney)	$46.0 M	$439.0 M	-43%	3
3	Sicario: Day of the Soldado (Sony / Columbia)	$17.5 M	$17.5 M	NEW	1
4	Uncle Drew (Lionsgate / Summit)	$13.0 M	$13.0 M	NEW	1
5	Ocean's 8 (Warner Bros.)	$7.5 M	$113.8 M	-35%	4
6	Tag (Warner / New Line)	$5.3 M	$40.4 M	-36%	3
7	Deadpool 2 (Fox)	$3.4 M	$310.2 M	-36%	7
8	Solo: A Star Wars Story (Disney)	$2.4 M	$207.2 M	-47%	6
9	Won't You Be My Neighbor? (Focus)	$2.2 M	$7.3 M	+21%	4
10	Sanju (FIP)	$2.1 M	$2.1 M	NEW	1
11	Hereditary (A24)	$2.0 M	$39.1 M	-45%	4"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(2018629, PRICES_RAW, BOR_RAW, FML_RAW)
