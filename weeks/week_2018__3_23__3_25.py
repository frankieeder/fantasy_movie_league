import fml

# 3/23/2018 - 3/25/2018 #

PRICES_RAW = """
PACIFIC RIM UPRISING
+FB$340
UNAVAILABLE

SCREENS LOCKED

BLACK PANTHER
+FB$251
UNAVAILABLE

SCREENS LOCKED

SHERLOCK GNOMES
+FB$223
UNAVAILABLE

SCREENS LOCKED

I CAN ONLY IMAGINE
+FB$176
UNAVAILABLE

SCREENS LOCKED

TOMB RAIDER
+FB$157
UNAVAILABLE

SCREENS LOCKED

PAUL, APOSTLE OF CHRIST
+FB$155
UNAVAILABLE

SCREENS LOCKED

A WRINKLE IN TIME
+FB$126
UNAVAILABLE

SCREENS LOCKED

LOVE, SIMON
+FB$98
UNAVAILABLE

SCREENS LOCKED

MIDNIGHT SUN
+FB$66
UNAVAILABLE

SCREENS LOCKED

UNSANE
+FB$58
UNAVAILABLE

SCREENS LOCKED

GAME NIGHT
+FB$56
UNAVAILABLE

SCREENS LOCKED

PETER RABBIT
+FB$50
UNAVAILABLE

SCREENS LOCKED

RED SPARROW
+FB$34
UNAVAILABLE

SCREENS LOCKED

THE STRANGERS: PREY AT NIGHT
+FB$34
UNAVAILABLE

SCREENS LOCKED

DEATH WISH
+FB$24"""

FML_RAW = """"Pacific Rim Uprising" - $23.4 million

"Black Panther" - $17.9 million

"Sherlock Gnomes" - $13.7 million

"I Can Only Imagine" - $13 million

"Tomb Raider" - $11.2 million

"A Wrinkle in Time" - $8.3 million

"Love, Simon" - $7.8 million

"Paul, Apostle of Christ" - $5.5 million

"Midnight Sun" - $4 million

"Game Night" - $4 million

"Unsane" - $3.9 million

"Peter Rabbit" - $3.7 million

"Red Sparrow" - $2.5 million

"The Strangers: Prey at Night" - $2.1 million

"Death Wish" - $1.5 million"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Pacific Rim Uprising (Universal)	$28.5 M	$28.5 M	NEW	1
2	Black Panther (Disney)	$18.0 M	$632.0 M	-32%	6
3	Sherlock Gnomes (Paramount / MGM)	$15.0 M	$15.0 M	NEW	1
4	I Can Only Imagine (Roadside)	$14.0 M	$38.2 M	-18%	2
5	Tomb Raider (Warner / MGM)	$10.8 M	$42.3 M	-54%	2
6	A Wrinkle in Time (Disney)	$8.3 M	$74.0 M	-49%	3
7	Paul, Apostle of Christ (Sony / AFFIRM)	$8.0 M	$8.0 M	NEW	1
8	Love, Simon (Fox)	$6.7 M	$22.3 M	-43%	2
9	Midnight Sun (Open Road)	$4.0 M	$4.0 M	NEW	1
10	Game Night (Warner / New Line)	$3.8 M	$60.4 M	-32%	5
11	Unsane (Bleecker Street / Fingerprint)	$3.7 M	$3.7 M	NEW	1
12	Peter Rabbit (Sony / Columbia)	$3.3 M	$107.5 M	-37%	7"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(2018323, PRICES_RAW, BOR_RAW, FML_RAW)
