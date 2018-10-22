import fml

# 7/13/2018 - 7/15/2018 #

PRICES_RAW = """HOTEL TRANSYLVANIA 3: SUMMER VACATION
+FB$523
UNAVAILABLE

SCREENS LOCKED

SKYSCRAPER
+FB$394
UNAVAILABLE

SCREENS LOCKED

ANT-MAN AND THE WASP
+FB$387
UNAVAILABLE

SCREENS LOCKED

INCREDIBLES 2
+FB$201
UNAVAILABLE

SCREENS LOCKED

JURASSIC WORLD: FALLEN KINGDOM
+FB$174
UNAVAILABLE

SCREENS LOCKED

THE FIRST PURGE
+FB$111
UNAVAILABLE

SCREENS LOCKED

SORRY TO BOTHER YOU
+FB$74
UNAVAILABLE

SCREENS LOCKED

SICARIO: DAY OF THE SOLDADO
+FB$45
UNAVAILABLE

SCREENS LOCKED

OCEAN'S 8
+FB$40
UNAVAILABLE

SCREENS LOCKED

UNCLE DREW
+FB$38
UNAVAILABLE

SCREENS LOCKED

WON'T YOU BE MY NEIGHBOR?
+FB$30
UNAVAILABLE

SCREENS LOCKED

TAG
+FB$21
UNAVAILABLE

SCREENS LOCKED

THREE IDENTICAL STRANGERS
+FB$16
UNAVAILABLE

SCREENS LOCKED

WHITNEY
+FB$14
UNAVAILABLE

SCREENS LOCKED

DEADPOOL 2
+FB$11"""

FML_RAW = """"Hotel Transylvania 3: Summer Vacation" - $43.2 million


"Ant-Man and the Wasp" - $33.4 million


"Skyscraper" - $33.2 million


"Incredibles 2" - $16.6 million


"Jurassic World: Fallen Kingdom" - $14.2 million


"The First Purge" - $6.2 million


"Sorry to Bother You" - $4.4 million


"Sicario: Day of the Soldado" - $3.4 million


"Ocean's 8" - $3.3 million


"Uncle Drew" - $2.9 million


"Won't You Be My Neighbor?" - $2.2 million


"Tag" - $1.6 million


"Three Identical Strangers" - $1 million


"Whitney" - $978,000


"Deadpool 2" - $843,000"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Hotel Transylvania 3: Summer Vacation
(Sony / Columbia)	$46.0 M	$47.3 M	NEW	1
2	Skyscraper (Universal / Legendary)	$30.0 M	$30.0 M	NEW	1
3	Ant-Man and The Wasp (Disney)	$29.5 M	$134.7 M	-61%	2
4	Incredibles 2 (Disney)	$16.0 M	$536.0 M	-44%	5
5	Jurassic World: Fallen Kingdom (Universal)	$15.0 M	$363.2 M	-48%	4
6	The First Purge (Universal)	$8.5 M	$49.2 M	-51%	2
7	Sorry to Bother You (Annapurna Pictures)	$5.2 M	$6.2 M	+615%	2
8	Sicario: Day of the Soldado (Sony / Columbia)	$3.6 M	$42.9 M	-53%	3
9	Uncle Drew (Lionsgate / Summit)	$3.2 M	$36.7 M	-52%	3
10	Ocean's 8 (Warner Bros.)	$2.8 M	$132.2 M	-45%	6
11	Won't You Be My Neighbor? (Focus)	$2.0 M	$16.0 M	-22%	6"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(2018713, PRICES_RAW, BOR_RAW, FML_RAW)

