import fml

# 6/8/2018 - 6/10/2018 #

PRICES_RAW = """OCEAN'S 8
+FB$626
UNAVAILABLE

SCREENS LOCKED

HEREDITARY
+FB$219
UNAVAILABLE

SCREENS LOCKED

SOLO: A STAR WARS STORY
+FB$218
UNAVAILABLE

SCREENS LOCKED

DEADPOOL 2
+FB$201
UNAVAILABLE

SCREENS LOCKED

HOTEL ARTEMIS
+FB$138
UNAVAILABLE

SCREENS LOCKED

AVENGERS: INFINITY WAR
+FB$93
UNAVAILABLE

SCREENS LOCKED

ADRIFT
+FB$89
UNAVAILABLE

SCREENS LOCKED

BOOK CLUB
+FB$67
UNAVAILABLE

SCREENS LOCKED

UPGRADE
+FB$32
UNAVAILABLE

SCREENS LOCKED

LIFE OF THE PARTY
+FB$31
UNAVAILABLE

SCREENS LOCKED

BREAKING IN
+FB$24
UNAVAILABLE

SCREENS LOCKED

A QUIET PLACE
+FB$16
UNAVAILABLE

SCREENS LOCKED

OVERBOARD
+FB$16
UNAVAILABLE

SCREENS LOCKED

ACTION POINT
+FB$15
UNAVAILABLE

SCREENS LOCKED

RBG
+FB$11"""

FML_RAW = """"Ocean's 8" - $42.6 million


"Solo: A Star Wars Story" - $14.3 million


"Deadpool 2" - $13.2 million


"Hereditary" - $11.4 million


"Avengers: Infinity War" - $6.7 million


"Adrift" - $6.1 million


"Hotel Artemis" - $5 million


"Book Club" - $5 million


"Upgrade" - $2.3 million


"Life of the Party" - $2.3 million


"Breaking In" - $1.7 million


"A Quiet Place" - $1.1 million


"Overboard" - $1 million


"Action Point" - $901,000


"RBG" - $743,000"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Ocean's 8 (Warner Bros.)	$39.0 M	$39.0 M	NEW	1
2	Solo: A Star Wars Story (Disney)	$14.3 M	$175.2 M	-51%	3
3	Deadpool 2 (Fox)	$13.5 M	$278.5 M	-42%	4
4	Hereditary (A24)	$10.0 M	$10.0 M	NEW	1
5	Avengers: Infinity War (Disney)	$6.9 M	$654.8 M	-34%	7
6	Adrift (STXfilms)	$5.9 M	$22.7 M	-49%	2
7	Book Club (Paramount)	$4.9 M	$57.8 M	-30%	4
8	Hotel Artemis (Global Road)	$4.7 M	$4.7 M	NEW	1
9	Upgrade (OTL Releasing / BH Tilt)	$2.3 M	$9.2 M	-51%	2
10	Life of the Party (Warner / New Line)	$2.0 M	$50.3 M	-43%	5"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(201868, PRICES_RAW, BOR_RAW, FML_RAW)

