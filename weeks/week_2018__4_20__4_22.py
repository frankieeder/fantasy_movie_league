import fml

# 4/20/2018 - 4/22/2018 #

PRICES_RAW = """A QUIET PLACE
+FB$361
UNAVAILABLE

SCREENS LOCKED

RAMPAGE
+FB$258
UNAVAILABLE

SCREENS LOCKED

I FEEL PRETTY
+FB$251
UNAVAILABLE

SCREENS LOCKED

TRUTH OR DARE
+FB$126
UNAVAILABLE

SCREENS LOCKED

BLOCKERS
+FB$98
UNAVAILABLE

SCREENS LOCKED

READY PLAYER ONE
+FB$95
UNAVAILABLE

SCREENS LOCKED

SUPER TROOPERS 2
+FB$84
UNAVAILABLE

SCREENS LOCKED

BLACK PANTHER
+FB$72
UNAVAILABLE

SCREENS LOCKED

TRAFFIK
+FB$68
UNAVAILABLE

SCREENS LOCKED

ISLE OF DOGS
+FB$47
UNAVAILABLE

SCREENS LOCKED

I CAN ONLY IMAGINE
+FB$33
UNAVAILABLE

SCREENS LOCKED

ACRIMONY
+FB$26
UNAVAILABLE

SCREENS LOCKED

CHAPPAQUIDDICK
+FB$25
UNAVAILABLE

SCREENS LOCKED

THE MIRACLE SEASON
+FB$19
UNAVAILABLE

SCREENS LOCKED

SHERLOCK GNOMES
+FB$18
UNAVAILABLE

SCREENS LOCKED
"""

FML_RAW = """"A Quiet Place" - $21.6 million


"Rampage" - $17 million


"I Feel Pretty" - $16.2 million


"Truth or Dare" - $7.9 million


"Blockers" - $5.9 million


"Ready Player One" - $5.8 million


"Super Troopers 2" - $5.2 million


"Black Panther" - $3.8 million


"Traffik" - $3 million


"Isle of Dogs" - $2.9 million


"I Can Only Imagine" - $2.4 million


"Chappaquiddick" - $1.7 million


"Acrimony" - $1.6 million


"The Miracle Season" - $1.3 million


"Sherlock Gnomes" - $1.2 million"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	A Quiet Place (Paramount)	$21.0 M	$131.2 M	-36%	3
2	Rampage (Warner / New Line)	$20.0 M	$66.2 M	-44%	2
3	I Feel Pretty (STXfilms)	$18.5 M	$18.5 M	NEW	1
4	Super Troopers 2 (Fox Searchlight)	$11.8 M	$11.8 M	NEW	1
5	Ready Player One (Warner Bros.)	$7.3 M	$125.9 M	-37%	4
6	Truth or Dare (Universal)	$7.0 M	$29.5 M	-63%	2
7	Blockers (Universal)	$5.8 M	$46.9 M	-46%	3
8	Traffik (Lionsgate / Summit)	$5.2 M	$5.2 M	NEW	1
9	Black Panther (Disney)	$4.5 M	$680.8 M	-22%	10
10	Isle of Dogs (Fox Searchlight)	$3.4 M	$24.4 M	-38%	5
11	I Can Only Imagine (Roadside)	$2.4 M	$79.3 M	-42%	6"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(2018420, PRICES_RAW, BOR_RAW, FML_RAW)
