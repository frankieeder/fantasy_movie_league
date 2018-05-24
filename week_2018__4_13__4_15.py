import fml

# 4/13/2018 - 4/15/2018 #

PRICES_RAW = """
RAMPAGE
+FB$535
UNAVAILABLE

SCREENS LOCKED

A QUIET PLACE
+FB$361
UNAVAILABLE

SCREENS LOCKED

TRUTH OR DARE
+FB$207
UNAVAILABLE

SCREENS LOCKED

READY PLAYER ONE
+FB$167
UNAVAILABLE

SCREENS LOCKED

BLOCKERS
+FB$147
UNAVAILABLE

SCREENS LOCKED

ISLE OF DOGS
+FB$105
UNAVAILABLE

SCREENS LOCKED

BLACK PANTHER
+FB$74
UNAVAILABLE

SCREENS LOCKED

I CAN ONLY IMAGINE
+FB$62
UNAVAILABLE

SCREENS LOCKED

ACRIMONY
+FB$52
UNAVAILABLE

SCREENS LOCKED

CHAPPAQUIDDICK
+FB$47
UNAVAILABLE

SCREENS LOCKED

SHERLOCK GNOMES
+FB$46
UNAVAILABLE

SCREENS LOCKED

THE MIRACLE SEASON
+FB$29
UNAVAILABLE

SCREENS LOCKED

PACIFIC RIM UPRISING
+FB$27
UNAVAILABLE

SCREENS LOCKED

A WRINKLE IN TIME
+FB$25
UNAVAILABLE

SCREENS LOCKED

LOVE, SIMON
+FB$18
UNAVAILABLE

SCREENS LOCKED
"""

FML_RAW = """"Rampage" - $36.6 million

"A Quiet Place" - $31.8 million

"Truth or Dare" - $16.7 million

"Ready Player One" - $13.9 million

"Blockers" - $13.3 million

"Isle of Dogs" - $7.8 million

"Black Panther" - $6.1 million

"I Can Only Imagine" - $5.3 million

"Acrimony" - $3.9 million

"Sherlock Gnomes" - $3.8 million

"Chappaquiddick" - $3.2 million

"The Miracle Season" - $2.6 million

"Pacific Rim Uprising" - $2.5 million

"A Wrinkle in Time" - $2.2 million

"Love, Simon" - $1.6 million
"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Rampage (Warner / New Line)	$33.5 M	$33.5 M	NEW	1
2	A Quiet Place (Paramount)	$32.0 M	$98.8 M	-36%	2
3	Truth or Dare (Universal)	$15.0 M	$15.0 M	NEW	1
4	Ready Player One (Warner Bros.)	$13.2 M	$117.0 M	-46%	3
5	Blockers (Universal)	$12.8 M	$39.8 M	-38%	2
6	Isle of Dogs (Fox Searchlight)	$6.5 M	$20.0 M	+42%	4
7	Black Panther (Disney)	$6.1 M	$674.7 M	-30%	9
8	I Can Only Imagine (Roadside)	$5.1 M	$76.5 M	-35%	5
9	Acrimony (Lionsgate)	$3.9 M	$38.1 M	-53%	3
10	Chappaquiddick (Entertainment Studios)	$3.6 M	$11.6 M	-38%	2
11	Sherlock Gnomes (Paramount / MGM)	$3.5 M	$38.4 M	-36%	4"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(2018413, PRICES_RAW, BOR_RAW, FML_RAW)
