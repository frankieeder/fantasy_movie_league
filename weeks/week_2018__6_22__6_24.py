import fml

# 6/22/2018 - 6/24/2018 #

PRICES_RAW = """INCREDIBLES 2
+FB$725
UNAVAILABLE

SCREENS LOCKED

FRI: JURASSIC WORLD: FALLEN KINGDOM
+FB$412
UNAVAILABLE

SCREENS LOCKED

SAT: JURASSIC WORLD: FALLEN KINGDOM
+FB$334
UNAVAILABLE

SCREENS LOCKED

SUN: JURASSIC WORLD: FALLEN KINGDOM
+FB$274
UNAVAILABLE

SCREENS LOCKED

OCEAN'S 8
+FB$75
UNAVAILABLE

SCREENS LOCKED

TAG
+FB$59
UNAVAILABLE

SCREENS LOCKED

SOLO: A STAR WARS STORY
+FB$43
UNAVAILABLE

SCREENS LOCKED

DEADPOOL 2
+FB$38
UNAVAILABLE

SCREENS LOCKED

AVENGERS: INFINITY WAR
+FB$29
UNAVAILABLE

SCREENS LOCKED

HEREDITARY
+FB$28
UNAVAILABLE

SCREENS LOCKED

SUPERFLY
+FB$27
UNAVAILABLE

SCREENS LOCKED

WON'T YOU BE MY NEIGHBOR?
+FB$16
UNAVAILABLE

SCREENS LOCKED

ADRIFT
+FB$8
UNAVAILABLE

SCREENS LOCKED

BOOK CLUB
+FB$7
UNAVAILABLE

SCREENS LOCKED

A WRINKLE IN TIME
+FB$6"""

FML_RAW = """"Incredibles 2" - $94.9 million


"Jurassic World: Fallen Kingdom" (Friday) - $57.5 million


"Jurassic World: Fallen Kingdom" (Saturday) - $46.4 million


"Jurassic World: Fallen Kingdom" (Sunday) - $36.5 million


"Ocean's 8" - $9.3 million


"Tag" - $7.7 million


"Solo: A Star Wars Story" - $5.4 million


"Deadpool 2" - $4.9 million


"Avengers: Infinity War" - $3.9 million


"Hereditary" - $3.6 million


"Superfly" - $2.6 million


"Won't You Be My Neighbor?" - $1.8 million


"Adrift" - $1 million


"Book Club" - $938,000


"A Wrinkle in Time" - $803,000"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Jurassic World: Fallen Kingdom (Universal)	$124.0 M	$124.0 M	NEW	1
2	Incredibles 2 (Disney)	$92.0 M	$365.0 M	-50%	2
3	Ocean's 8 (Warner Bros.)	$10.2 M	$99.0 M	-46%	3
4	Tag (Warner / New Line)	$7.8 M	$29.8 M	-48%	2
5	Solo: A Star Wars Story (Disney)	$5.0 M	$203.0 M	-50%	5
6	Deadpool 2 (Fox)	$4.9 M	$303.8 M	-44%	6
7	Hereditary (A24)	$3.9 M	$35.2 M	-43%	3
8	Superfly (Sony / Columbia)	$3.7 M	$15.6 M	-46%	2
9	Avengers: Infinity War (Disney)	$3.2 M	$670.2 M	-41%	9
10	Won't You Be My Neighbor? (Focus)	$2.0 M	$4.3 M	+99%	3"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(2018622, PRICES_RAW, BOR_RAW, FML_RAW)

