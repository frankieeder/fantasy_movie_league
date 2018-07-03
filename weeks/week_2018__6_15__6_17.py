import fml

# 6/15/2018 - 6/17/2018 #

PRICES_RAW = """FRI: INCREDIBLES 2
+FB$521
UNAVAILABLE

SCREENS LOCKED

SAT: INCREDIBLES 2
+FB$427
UNAVAILABLE

SCREENS LOCKED

SUN: INCREDIBLES 2
+FB$350
UNAVAILABLE

SCREENS LOCKED

OCEAN'S 8
+FB$201
UNAVAILABLE

SCREENS LOCKED

TAG
+FB$145
UNAVAILABLE

SCREENS LOCKED

SOLO: A STAR WARS STORY
+FB$89
UNAVAILABLE

SCREENS LOCKED

DEADPOOL 2
+FB$78
UNAVAILABLE

SCREENS LOCKED

SUPERFLY
+FB$71
UNAVAILABLE

SCREENS LOCKED

HEREDITARY
+FB$62
UNAVAILABLE

SCREENS LOCKED

AVENGERS: INFINITY WAR
+FB$48
UNAVAILABLE

SCREENS LOCKED

ADRIFT
+FB$26
UNAVAILABLE

SCREENS LOCKED

BOOK CLUB
+FB$25
UNAVAILABLE

SCREENS LOCKED

HOTEL ARTEMIS
+FB$13
UNAVAILABLE

SCREENS LOCKED

LIFE OF THE PARTY
+FB$11
UNAVAILABLE

SCREENS LOCKED

UPGRADE
+FB$11"""

FML_RAW = """"Incredibles 2" (Friday) - $56.2 million


"Incredibles 2" (Saturday) - $46.5 million


"Incredibles 2" (Sunday) - $35.4 million


"Ocean's 8" - $21.2 million


"Tag" - $14.8 million


"Solo: A Star Wars Story" - $8.4 million


"Deadpool 2" - $8.2 million


"Hereditary" - $6.3 million


"Superfly" - $5.3 million


"Avengers: Infinity War" - $4.7 million


"Adrift" - $2.8 million


"Book Club" - $2.6 million


"Upgrade" - $1.32 million


"Life of the Party" - $1.3 million


"Hotel Artemis" - $1.2 million"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Incredibles 2 (Disney)	$143.0 M	$143.0 M	NEW	1
2	Ocean's 8 (Warner Bros.)	$21.0 M	$81.0 M	-50%	2
3	Tag (Warner / New Line)	$12.5 M	$12.5 M	NEW	1
4	Solo: A Star Wars Story (Disney)	$10.0 M	$193.8 M	-37%	4
5	Deadpool 2 (Fox)	$9.0 M	$294.8 M	-36%	5
6	Superfly (Sony / Columbia)	$8.0 M	$11.0 M	NEW	1
7	Hereditary (A24)	$7.0 M	$27.0 M	-48%	2
8	Avengers: Infinity War (Disney)	$5.2 M	$664.1 M	-28%	8
9	Adrift (STXfilms)	$2.4 M	$27.1 M	-54%	3
10	Book Club (Paramount)	$2.3 M	$62.4 M	-46%	5"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(2018615, PRICES_RAW, BOR_RAW, FML_RAW)

