import fml

# 6/1/2018 - 6/3/2018 #

PRICES_RAW = """SOLO: A STAR WARS STORY
+FB$514
UNAVAILABLE

SCREENS LOCKED

DEADPOOL 2
+FB$325
UNAVAILABLE

SCREENS LOCKED

ADRIFT
+FB$215
UNAVAILABLE

SCREENS LOCKED

AVENGERS: INFINITY WAR
+FB$167
UNAVAILABLE

SCREENS LOCKED

ACTION POINT
+FB$143
UNAVAILABLE

SCREENS LOCKED

BOOK CLUB
+FB$126
UNAVAILABLE

SCREENS LOCKED

UPGRADE
+FB$62
UNAVAILABLE

SCREENS LOCKED

LIFE OF THE PARTY
+FB$49
UNAVAILABLE

SCREENS LOCKED

BREAKING IN
+FB$36
UNAVAILABLE

SCREENS LOCKED

OVERBOARD
+FB$30
UNAVAILABLE

SCREENS LOCKED

SHOW DOGS
+FB$25
UNAVAILABLE

SCREENS LOCKED

A QUIET PLACE
+FB$21
UNAVAILABLE

SCREENS LOCKED

BEST OF THE REST
+FB$19
UNAVAILABLE

SCREENS LOCKED

RBG
+FB$15
UNAVAILABLE

SCREENS LOCKED

RAMPAGE
+FB$7"""

FML_RAW = """"Solo: A Star Wars Story" - $37.3 million


"Deadpool 2" - $20.9 million


"Adrift" - $11.7 million


"Avengers: Infinity War" - $8.6 million


"Action Point" - $8.2 million


"Book Club" - $6.2 million


"Life of the Party" - $2.9 million


"Upgrade" - $2.8 million


"Breaking In" - $2 million


"Overboard" - $1.6 million


"Show Dogs" - $1.3 million


"A Quiet Place" - $1.2 million


"RBG" - $795,000


"Best of the Rest" - $698,000


"Rampage" - $419,000"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Solo: A Star Wars Story (Disney)	$31.0 M	$150.5 M	-63%	2
2	Deadpool 2 (Fox)	$20.0 M	$250.3 M	-54%	3
3	Adrift (STXfilms)	$11.5 M	$11.5 M	NEW	1
4	Avengers: Infinity War (Disney)	$10.2 M	$642.3 M	-41%	6
5	Book Club (Paramount)	$6.8 M	$47.0 M	-32%	3
6	Action Point (Paramount)	$4.7 M	$4.7 M	NEW	1
7	Upgrade (OTL Releasing / BH Tilt)	$3.8 M	$3.8 M	NEW	1
8	Life of the Party (Warner / New Line)	$3.1 M	$45.8 M	-42%	4
9	Breaking In (Universal)	$2.3 M	$40.7 M	-46%	4
10	Overboard (Lionsgate / Pantelion / MGM)	$1.9 M	$45.4 M	-39%	5
11	Show Dogs (Global Road)	$1.6 M	$14.5 M	-51%	3"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(201861, PRICES_RAW, BOR_RAW, FML_RAW)

