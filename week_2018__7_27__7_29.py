import fml

# 7/27/2018 - 7/29/2018 #

PRICES_RAW = """MISSION: IMPOSSIBLE: FALLOUT
+FB$756
UNAVAILABLE

SCREENS LOCKED

MAMMA MIA! HERE WE GO AGAIN
+FB$227
UNAVAILABLE

SCREENS LOCKED

THE EQUALIZER 2
+FB$201
UNAVAILABLE

SCREENS LOCKED

HOTEL TRANSYLVANIA 3: SUMMER VACATION
+FB$157
UNAVAILABLE

SCREENS LOCKED

TEEN TITANS GO! TO THE MOVIES
+FB$149
UNAVAILABLE

SCREENS LOCKED

ANT-MAN AND THE WASP
+FB$116
UNAVAILABLE

SCREENS LOCKED

INCREDIBLES 2
+FB$89
UNAVAILABLE

SCREENS LOCKED

JURASSIC WORLD: FALLEN KINGDOM
+FB$76
UNAVAILABLE

SCREENS LOCKED

SKYSCRAPER
+FB$61
UNAVAILABLE

SCREENS LOCKED

BLINDSPOTTING
+FB$41
UNAVAILABLE

SCREENS LOCKED

THE FIRST PURGE
+FB$28
UNAVAILABLE

SCREENS LOCKED

EIGHTH GRADE
+FB$26
UNAVAILABLE

SCREENS LOCKED

SORRY TO BOTHER YOU
+FB$18
UNAVAILABLE

SCREENS LOCKED

UNFRIENDED: DARK WEB
+FB$18
UNAVAILABLE

SCREENS LOCKED

THREE IDENTICAL STRANGERS
+FB$16"""

FML_RAW = """"Mission: Impossible: Fallout" - $63.6 million


"Mamma Mia! Here We Go Again" - $19.8 million


"The Equalizer 2" - $18.3 million


"Hotel Transylvania 3: Summer Vacation" - $13.6 million


"Teen Titans Go! To The Movies" - $13.4 million


"Ant-Man and the Wasp" - $9.1 million


"Incredibles 2" - $7.9 million


"Jurassic World: Fallen Kingdom" - $6.7 million


"Skyscraper" - $5.3 million


"Blindspotting" - $3 million


"The First Purge" - $2.4 million


"Sorry to Bother You" - $1.8 million


"Unfriended: Dark Web" - $1.6 million


"Three Identical Strangers" - $1.1 million


"Eighth Grade" - $946,000"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Mission: Impossible: Fallout (Paramount)	$57.0 M	$57.0 M	NEW	1
2	Mamma Mia! Here We Go Again (Universal)	$20.5 M	$75.5 M	-41%	2
3	The Equalizer 2 (Sony / Columbia)	$16.0 M	$66.0 M	-56%	2
4	Hotel Transylvania 3: Summer Vacation
(Sony / Columbia)	$14.0 M	$120.5 M	-41%	3
5	Teen Titans GO! To The Movies (Warner Bros.)	$13.5 M	$13.5 M	NEW	1
6	Ant-Man and The Wasp (Disney)	$9.3 M	$184.0 M	-44%	4
7	Incredibles 2 (Disney)	$8.3 M	$573.7 M	-30%	7
8	Jurassic World: Fallen Kingdom (Universal)	$7.2 M	$397.8 M	-36%	6
9	Skyscraper (Universal / Legendary)	$5.7 M	$59.3 M	-50%	3
10	The First Purge (Universal)	$2.4 M	$65.7 M	-53%	4
11	Blindspotting (Lionsgate / Summit)	$2.0 M	$2.5 M	+495%	2"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(2018727, PRICES_RAW, BOR_RAW, FML_RAW)
