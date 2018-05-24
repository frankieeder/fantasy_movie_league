import fml

# 5/18/2018 - 5/20/2018 #
PRICES_RAW = """FRI: Deadpool 2 - FRI ONLY
+FB$501
UNAVAILABLE

SCREENS LOCKED

SAT: Deadpool 2 - SAT ONLY
+FB$452
UNAVAILABLE

SCREENS LOCKED

SUN: Deadpool 2 - SUN ONLY
+FB$337
UNAVAILABLE

SCREENS LOCKED

AVENGERS: INFINITY WAR
+FB$280
UNAVAILABLE

SCREENS LOCKED

SHOW DOGS
+FB$99
UNAVAILABLE

SCREENS LOCKED

BOOK CLUB
+FB$98
UNAVAILABLE

SCREENS LOCKED

LIFE OF THE PARTY
+FB$76
UNAVAILABLE

SCREENS LOCKED

BREAKING IN
+FB$73
UNAVAILABLE

SCREENS LOCKED

OVERBOARD
+FB$50
UNAVAILABLE

SCREENS LOCKED

A QUIET PLACE
+FB$45
UNAVAILABLE

SCREENS LOCKED

POPE FRANCIS: A MAN OF HIS WORD
+FB$25
UNAVAILABLE

SCREENS LOCKED

I FEEL PRETTY
+FB$21
UNAVAILABLE

SCREENS LOCKED

RAMPAGE
+FB$19
UNAVAILABLE

SCREENS LOCKED

TULLY
+FB$13
UNAVAILABLE

SCREENS LOCKED

RBG
+FB$13
UNAVAILABLE

SCREENS LOCKED
"""

FML_RAW = """"Deadpool 2" (Friday) - $56.8 million


"Deadpool 2" (Saturday) - $45.3 million


"Deadpool 2" (Sunday) - $35 million


"Avengers: Infinity War" - $30.8 million


"Book Club" - $10.3 million


"Life of the Party" - $8.4 million


"Show Dogs" - $7.9 million


"Breaking In" - $7.2 million


"Overboard" - $4.7 million


"A Quiet Place" - $4.4 million


"Pope Francis: A Man of His Word" - $2.3 million


"Rampage" - $2.2 million


"I Feel Pretty" - $2.1 million


"Tully" - $1.2 million


"RBG" - $988,000"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Deadpool 2 (Fox)	$141.0 M	$141.0 M	NEW	1
2	Avengers: Infinity War (Disney)	$30.0 M	$596.7 M	-52%	4
3	Book Club (Paramount)	$13.8 M	$13.8 M	NEW	1
4	Life of the Party (Warner / New Line)	$7.7 M	$31.0 M	-57%	2
5	Breaking In (Universal)	$7.5 M	$30.0 M	-57%	2
6	Show Dogs (Global Road)	$6.5 M	$6.5 M	NEW	1
7	Overboard (Lionsgate / Pantelion / MGM)	$5.0 M	$37.3 M	-49%	3
8	A Quiet Place (Paramount)	$4.3 M	$176.4 M	-33%	7
9	I Feel Pretty (STXfilms)	$1.7 M	$47.1 M	-55%	5
10	Rampage (Warner / New Line)	$1.6 M	$92.6 M	-54%	6"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(2018518, PRICES_RAW, BOR_RAW, FML_RAW)
