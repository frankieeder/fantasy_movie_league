import fml

# 5/25/2018 - 5/28/2018 #

PRICES_RAW = """DEADPOOL 2
+FB$680
UNAVAILABLE

SCREENS LOCKED

FRI: SOLO: A STAR WARS STORY
+FB$587
UNAVAILABLE

SCREENS LOCKED

SAT: SOLO: A STAR WARS STORY
+FB$371
UNAVAILABLE

SCREENS LOCKED

SUN: SOLO: A STAR WARS STORY
+FB$334
UNAVAILABLE

SCREENS LOCKED

MON: SOLO: A STAR WARS STORY
+FB$271
UNAVAILABLE

SCREENS LOCKED

AVENGERS: INFINITY WAR
+FB$252
UNAVAILABLE

SCREENS LOCKED

BOOK CLUB
+FB$133
UNAVAILABLE

SCREENS LOCKED

LIFE OF THE PARTY
+FB$57
UNAVAILABLE

SCREENS LOCKED

SHOW DOGS
+FB$52
UNAVAILABLE

SCREENS LOCKED

BREAKING IN
+FB$49
UNAVAILABLE

SCREENS LOCKED

A QUIET PLACE
+FB$35
UNAVAILABLE

SCREENS LOCKED

OVERBOARD
+FB$33
UNAVAILABLE

SCREENS LOCKED

RBG
+FB$16
UNAVAILABLE

SCREENS LOCKED

RAMPAGE
+FB$10
UNAVAILABLE

SCREENS LOCKED

I FEEL PRETTY
+FB$8"""

FML_RAW = """"Deadpool 2" - $55.2 million


"Solo: A Star Wars Story" (Friday) - $50.2 million


"Solo: A Star Wars Story" (Saturday) - $39.7 million


"Solo: A Star Wars Story" (Sunday) - $35 million


"Solo: A Star Wars Story" (Monday) - $26.4 million


"Avengers: Infinity War" - $22.5 million


"Book Club" - $11.7 million


"Life of the Party" - $5.3 million


"Show Dogs" - $4.4 million


"Breaking In" - $4.1 million


"A Quiet Place" - $3.2 million


"Overboard" - $2.7 million


"RBG" - $1.2 million


"Rampage" - $1.1 million


"I Feel Pretty" - $853,000
"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Solo: A Star Wars Story (Disney)	$146.0 M	$146.0 M	NEW	1
2	Deadpool 2 (Fox)	$63.0 M	$229.0 M	-50%	2
3	Avengers: Infinity War (Disney)	$22.0 M	$627.0 M	-25%	5
4	Book Club (Paramount)	$13.0 M	$35.2 M	-4%	2
5	Life of the Party (Warner / New Line)	$5.5 M	$39.5 M	-28%	3
6	Show Dogs (Global Road)	$5.0 M	$12.8 M	-17%	2
7	Breaking In (Universal)	$4.7 M	$36.3 M	-31%	3
8	Overboard (Lionsgate / Pantelion / MGM)	$3.0 M	$41.5 M	-35%	4
9	A Quiet Place (Paramount)	$2.8 M	$180.5 M	-29%	8
10	RBG (Magnolia)	$1.2 M	$5.7 M	-4%	4"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(2018525, PRICES_RAW, BOR_RAW, FML_RAW)
