import fml

# 7/6/2018 - 7/8/2018 #

PRICES_RAW = """ANT-MAN AND THE WASP
+FB$804
UNAVAILABLE

SCREENS LOCKED

JURASSIC WORLD: FALLEN KINGDOM
+FB$267
UNAVAILABLE

SCREENS LOCKED

INCREDIBLES 2
+FB$229
UNAVAILABLE

SCREENS LOCKED

THE FIRST PURGE
+FB$201
UNAVAILABLE

SCREENS LOCKED

SICARIO: DAY OF THE SOLDADO
+FB$89
UNAVAILABLE

SCREENS LOCKED

UNCLE DREW
+FB$71
UNAVAILABLE

SCREENS LOCKED

OCEAN'S 8
+FB$48
UNAVAILABLE

SCREENS LOCKED

TAG
+FB$34
UNAVAILABLE

SCREENS LOCKED

WON'T YOU BE MY NEIGHBOR?
+FB$23
UNAVAILABLE

SCREENS LOCKED

DEADPOOL 2
+FB$20
UNAVAILABLE

SCREENS LOCKED

SOLO: A STAR WARS STORY
+FB$13
UNAVAILABLE

SCREENS LOCKED

HEREDITARY
+FB$12
UNAVAILABLE

SCREENS LOCKED

AVENGERS: INFINITY WAR
+FB$11
UNAVAILABLE

SCREENS LOCKED

SANJU
+FB$10
UNAVAILABLE

SCREENS LOCKED

SUPERFLY
+FB$6"""

FML_RAW = """"Ant-Man and the Wasp" - $86.4 million


"Jurassic World: Fallen Kingdom" - $28.2 million


"Incredibles 2" - $27.8 million


"The First Purge" - $22.8 million


"Sicario: Day of the Soldado" - $10.1 million


"Uncle Drew" - $7.3 million


"Ocean's 8" - $5.7 million


"Tag" - $3.7 million


"Won't You Be My Neighbor?" - $2.2 million


"Deadpool 2" - $2.2 million


"Solo: A Star Wars Story" - $1.4 million


"Hereditary" - $1.3 million


"Avengers: Infinity War" - $1.2 million


"Sanju" - $955,000


"Superfly" - $645,000"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Ant-Man and The Wasp (Disney)	$86.0 M	$86.0 M	NEW	1
2	Jurassic World: Fallen Kingdom (Universal)	$27.5 M	$327.5 M	-55%	3
3	Incredibles 2 (Disney)	$26.0 M	$498.0 M	-44%	4
4	The First Purge (Universal)	$19.5 M	$34.0 M	NEW	1
5	Sicario: Day of the Soldado (Sony / Columbia)	$8.0 M	$35.2 M	-58%	2
6	Uncle Drew (Lionsgate / Summit)	$7.7 M	$30.0 M	-49%	2
7	Ocean's 8 (Warner Bros.)	$5.9 M	$127.0 M	-29%	5
8	Tag (Warner / New Line)	$3.8 M	$49.2 M	-35%	4
9	Won't You Be My Neighbor? (Focus)	$2.2 M	$11.5 M	-9%	5
10	Deadpool 2 (Fox)	$2.0 M	$315.0 M	-44%	8"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(201876, PRICES_RAW, BOR_RAW, FML_RAW)

