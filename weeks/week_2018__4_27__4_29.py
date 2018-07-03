import fml

# 4/27/2018 - 4/29/2018 #

PRICES_RAW = """
FRI - AVENGERS: INFINITY WAR - FRI ONLY
+FB$620
UNAVAILABLE

SCREENS LOCKED

SAT - AVENGERS: INFINITY WAR - SAT ONLY
+FB$411
UNAVAILABLE

SCREENS LOCKED

SUN - AVENGERS: INFINITY WAR - SUN ONLY
+FB$334
UNAVAILABLE

SCREENS LOCKED

A QUIET PLACE
+FB$70
UNAVAILABLE

SCREENS LOCKED

RAMPAGE
+FB$55
UNAVAILABLE

SCREENS LOCKED

I FEEL PRETTY
+FB$47
UNAVAILABLE

SCREENS LOCKED

SUPER TROOPERS 2
+FB$33
UNAVAILABLE

SCREENS LOCKED

BLACK PANTHER
+FB$32
UNAVAILABLE

SCREENS LOCKED

READY PLAYER ONE
+FB$21
UNAVAILABLE

SCREENS LOCKED

BLOCKERS
+FB$21
UNAVAILABLE

SCREENS LOCKED

TRUTH OR DARE
+FB$21
UNAVAILABLE

SCREENS LOCKED

ISLE OF DOGS
+FB$13
UNAVAILABLE

SCREENS LOCKED

TRAFFIK
+FB$11
UNAVAILABLE

SCREENS LOCKED

I CAN ONLY IMAGINE
+FB$8
UNAVAILABLE

SCREENS LOCKED

CHAPPAQUIDDICK
+FB$6
UNAVAILABLE

SCREENS LOCKED
"""

FML_RAW = """"Avengers: Infinity War" (Friday) - $110.7 million


"Avengers: Infinity War" (Saturday) - $72.7 million


"Avengers: Infinity War" (Sunday) - $58.8 million


"A Quiet Place" - $11.8 million


"Rampage" - $9.1 million


"I Feel Pretty" - $7.6 million


"Super Troopers 2" - $5.6 million


"Black Panther" - $4.8 million


"Ready Player One" - $3.7 million


"Blockers" - $3.6 million


"Truth or Dare" - $3.6 million


"Isle of Dogs" - $1.7 million


"Traffik" - $1.6 million


"I Can Only Imagine" - $1.2 million


"Chappaquiddick" - $0.932 million"""

BOR_RAW = """
Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Avengers: Infinity War (Disney)	$230.0 M	$230.0 M	NEW	1
2	A Quiet Place (Paramount)	$11.2 M	$148.5 M	-46%	4
3	I Feel Pretty (STXfilms)	$8.3 M	$29.5 M	-48%	2
4	Rampage (Warner / New Line)	$8.0 M	$78.8 M	-60%	3
5	Super Troopers 2 (Fox Searchlight)	$5.3 M	$23.9 M	-65%	2
6	Black Panther (Disney)	$4.7 M	$688.2 M	-5%	11
7	Ready Player One (Warner Bros.)	$3.5 M	$131.7 M	-53%	5
8	Blockers (Universal)	$3.4 M	$53.7 M	-50%	4
9	Truth or Dare (Universal)	$3.2 M	$35.3 M	-59%	3
10	Traffik (Lionsgate / Summit)	$1.9 M	$7.0 M	-52%	2"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(2018427, PRICES_RAW, BOR_RAW, FML_RAW)
