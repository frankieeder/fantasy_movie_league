import fml

# 7/20/2018 - 7/22/2018 #

PRICES_RAW = """MAMMA MIA! HERE WE GO AGAIN
+FB$526
UNAVAILABLE

SCREENS LOCKED

THE EQUALIZER 2
+FB$403
UNAVAILABLE

SCREENS LOCKED

HOTEL TRANSYLVANIA 3: SUMMER VACATION
+FB$334
UNAVAILABLE

SCREENS LOCKED

ANT-MAN AND THE WASP
+FB$210
UNAVAILABLE

SCREENS LOCKED

SKYSCRAPER
+FB$167
UNAVAILABLE

SCREENS LOCKED

INCREDIBLES 2
+FB$149
UNAVAILABLE

SCREENS LOCKED

JURASSIC WORLD: FALLEN KINGDOM
+FB$135
UNAVAILABLE

SCREENS LOCKED

UNFRIENDED: DARK WEB
+FB$103
UNAVAILABLE

SCREENS LOCKED

THE FIRST PURGE
+FB$61
UNAVAILABLE

SCREENS LOCKED

SORRY TO BOTHER YOU
+FB$42
UNAVAILABLE

SCREENS LOCKED

SICARIO: DAY OF THE SOLDADO
+FB$29
UNAVAILABLE

SCREENS LOCKED

OCEAN'S 8
+FB$24
UNAVAILABLE

SCREENS LOCKED

LEAVE NO TRACE
+FB$23
UNAVAILABLE

SCREENS LOCKED

UNCLE DREW
+FB$21
UNAVAILABLE

SCREENS LOCKED

WON'T YOU BE MY NEIGHBOR?
+FB$20"""

FML_RAW = """"Mamma Mia! Here We Go Again" - $33.5 million


"The Equalizer 2" - $26.8 million


"Hotel Transylvania 3: Summer Vacation" - $24.5 million


"Ant-Man and the Wasp" - $15.2 million


"Skyscraper" - $12 million


"Incredibles 2" - $9.7 million


"Jurassic World: Fallen Kingdom" - $9.4 million


"Unfriended: Dark Web" - $5.1 million


"The First Purge" - $4.3 million


"Sorry to Bother You" - $2.8 million


"Sicario: Day of the Soldado" - $1.8 million


"Ocean's 8" - $1.6 million


"Uncle Drew" - $1.4 million


"Won't You Be My Neighbor?" - $1.3 million


"Leave No Trace" - $1.1 million

"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Mamma Mia! Here We Go Again (Universal)	$40.0 M	$40.0 M	NEW	1
2	The Equalizer 2 (Sony / Columbia)	$30.0 M	$30.0 M	NEW	1
3	Hotel Transylvania 3: Summer Vacation
(Sony / Columbia)	$24.0 M	$92.5 M	-46%	2
4	Ant-Man and The Wasp (Disney)	$15.7 M	$164.3 M	-46%	3
5	Skyscraper (Universal / Legendary)	$12.2 M	$48.3 M	-51%	2
6	Incredibles 2 (Disney)	$11.2 M	$557.2 M	-31%	6
7	Jurassic World: Fallen Kingdom (Universal)	$10.2 M	$383.0 M	-37%	5
8	The First Purge (Universal)	$4.6 M	$59.9 M	-51%	3
9	Unfriended: Dark Web (OTL Releasing / BH Tilt)	$4.1 M	$4.1 M	NEW	1
10	Sorry to Bother You (Annapurna Pictures)	$3.1 M	$10.5 M	-26%	3"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(2018720, PRICES_RAW, BOR_RAW, FML_RAW)

