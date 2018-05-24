import fml

# 5/11/2018 - 5/13/2018 #

PRICES_RAW = """
AVENGERS: INFINITY WAR
+FB$580
UNAVAILABLE

SCREENS LOCKED

LIFE OF THE PARTY
+FB$225
UNAVAILABLE

SCREENS LOCKED

BREAKING IN
+FB$131
UNAVAILABLE

SCREENS LOCKED

OVERBOARD
+FB$85
UNAVAILABLE

SCREENS LOCKED

A QUIET PLACE
+FB$50
UNAVAILABLE

SCREENS LOCKED

I FEEL PRETTY
+FB$33
UNAVAILABLE

SCREENS LOCKED

RAMPAGE
+FB$26
UNAVAILABLE

SCREENS LOCKED

BLACK PANTHER
+FB$22
UNAVAILABLE

SCREENS LOCKED

TULLY
+FB$21
UNAVAILABLE

SCREENS LOCKED

RBG
+FB$13
UNAVAILABLE

SCREENS LOCKED

BLOCKERS
+FB$9
UNAVAILABLE

SCREENS LOCKED

TRUTH OR DARE
+FB$9
UNAVAILABLE

SCREENS LOCKED

SUPER TROOPERS 2
+FB$9
UNAVAILABLE

SCREENS LOCKED

BAD SAMARITAN
+FB$7
UNAVAILABLE

SCREENS LOCKED

READY PLAYER ONE
+FB$6"""

FML_RAW = """"Avengers: Infinity War" - $59.7 million


"Life of the Party" - $19.4 million


"Breaking In" - $13.6 million


"Overboard" - $6.2 million


"A Quiet Place" - $5.3 million


"I Feel Pretty" - $3 million


"Rampage" - $2.8 million


"Black Panther" - $1.9 million


"Tully" - $1.8 million


"RBG" - $1.5 million


"Blockers" - $958,000


"Super Troopers 2" - $898,000


"Truth or Dare" - $741,000


"Ready Player One" - $722,000


"Bad Samaritan" - $708,000"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Avengers: Infinity War (Disney)	$60.0 M	$546.3 M	-48%	3
2	Life of the Party (Warner / New Line)	$22.0 M	$22.0 M	NEW	1
3	Breaking In (Universal)	$19.0 M	$19.0 M	NEW	1
4	Overboard (Lionsgate / Pantelion / MGM)	$9.7 M	$29.3 M	-34%	2
5	A Quiet Place (Paramount)	$6.5 M	$169.7 M	-16%	6
6	I Feel Pretty (STXfilms)	$3.7 M	$43.8 M	-27%	4
7	Rampage (Warner / New Line)	$3.3 M	$89.6 M	-29%	5
8	Tully (Focus)	$3.2 M	$7.9 M	-3%	2
9	Black Panther (Disney)	$2.3 M	$696.5 M	-29%	13
10	RBG (Magnolia)	$1.2 M	$2.0 M	+107%	2
11	Blockers (Universal)	$1.1 M	$58.1 M	-37%	6"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(2018511, PRICES_RAW, BOR_RAW, FML_RAW)

