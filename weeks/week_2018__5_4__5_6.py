import fml

# 5/4/2018 - 5/6/2018 #

PRICES_RAW = """
SAT - AVENGERS: INFINITY WAR - SAT ONLY
+FB$560
UNAVAILABLE

SCREENS LOCKED

SUN - AVENGERS: INFINITY WAR - SUN ONLY
+FB$418
UNAVAILABLE

SCREENS LOCKED

FRI - AVENGERS: INFINITY WAR - FRI ONLY
+FB$335
UNAVAILABLE

SCREENS LOCKED

OVERBOARD
+FB$167
UNAVAILABLE

SCREENS LOCKED

A QUIET PLACE
+FB$94
UNAVAILABLE

SCREENS LOCKED

I FEEL PRETTY
+FB$63
UNAVAILABLE

SCREENS LOCKED

TULLY
+FB$56
UNAVAILABLE

SCREENS LOCKED

RAMPAGE
+FB$52
UNAVAILABLE

SCREENS LOCKED

BLACK PANTHER
+FB$42
UNAVAILABLE

SCREENS LOCKED

BAD SAMARITAN
+FB$40
UNAVAILABLE

SCREENS LOCKED

BLOCKERS
+FB$21
UNAVAILABLE

SCREENS LOCKED

TRUTH OR DARE
+FB$18
UNAVAILABLE

SCREENS LOCKED

SUPER TROOPERS 2
+FB$17
UNAVAILABLE

SCREENS LOCKED

READY PLAYER ONE
+FB$16
UNAVAILABLE

SCREENS LOCKED

TRAFFIK
+FB$10"""

FML_RAW = """"Avengers: Infinity War" (Saturday) - $50.5 million


"Avengers: Infinity War" (Sunday) - $37.4 million


"Avengers: Infinity War" (Friday) - $30.2 million


"Overboard" - $7.8 million


"A Quiet Place" - $7.3 million


"I Feel Pretty" - $5.2 million


"Tully" - $5 million


"Rampage" - $4.4 million


"Black Panther" - $3 million


"Bad Samaritan" - $2.1 million


"Blockers" - $1.5 million


"Ready Player One" - $1.3 million


"Truth or Dare" - $1.3 million


"Super Troopers 2" - $1.2 million


"Traffik" - $741,000"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Avengers: Infinity War (Disney)	$119.0 M	$455.0 M	-54%	2
2	Overboard (Lionsgate / Pantelion / MGM)	$12.3 M	$12.3 M	NEW	1
3	A Quiet Place (Paramount)	$8.0 M	$160.2 M	-27%	5
4	I Feel Pretty (STXfilms)	$5.5 M	$38.3 M	-33%	3
5	Rampage (Warner / New Line)	$4.7 M	$84.9 M	-35%	4
6	Tully (Focus)	$4.2 M	$4.2 M	NEW	1
7	Black Panther (Disney)	$3.3 M	$693.3 M	-30%	12
8	Bad Samaritan (Electric Entertainment)	$2.3 M	$2.3 M	NEW	1
9	Super Troopers 2 (Fox Searchlight)	$1.9 M	$25.4 M	-49%	3
10	Truth or Dare (Universal)	$1.8 M	$38.1 M	-45%	4
11	Blockers (Universal)	$1.7 M	$56.2 M	-43%	5"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(201854, PRICES_RAW, BOR_RAW, FML_RAW)

