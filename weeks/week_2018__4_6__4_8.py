import fml

# 4/6/2018 - 4/8/2018 #

PRICES_RAW = """
A QUIET PLACE
+FB$460
UNAVAILABLE

SCREENS LOCKED

READY PLAYER ONE
+FB$334
UNAVAILABLE

SCREENS LOCKED

BLOCKERS
+FB$217
UNAVAILABLE

SCREENS LOCKED

BLACK PANTHER
+FB$108
UNAVAILABLE

SCREENS LOCKED

TYLER PERRY'S ACRIMONY
+FB$103
UNAVAILABLE

SCREENS LOCKED

I CAN ONLY IMAGINE
+FB$96
UNAVAILABLE

SCREENS LOCKED

ISLE OF DOGS
+FB$62
UNAVAILABLE

SCREENS LOCKED

PACIFIC RIM UPRISING
+FB$58
UNAVAILABLE

SCREENS LOCKED

SHERLOCK GNOMES
+FB$57
UNAVAILABLE

SCREENS LOCKED

THE MIRACLE SEASON
+FB$53
UNAVAILABLE

SCREENS LOCKED

CHAPPAQUIDDICK
+FB$50
UNAVAILABLE

SCREENS LOCKED

A WRINKLE IN TIME
+FB$39
UNAVAILABLE

SCREENS LOCKED

LOVE, SIMON
+FB$39
UNAVAILABLE

SCREENS LOCKED

TOMB RAIDER
+FB$34
UNAVAILABLE

SCREENS LOCKED

PAUL, APOSTLE OF CHRIST
+FB$26"""

FML_RAW = """"A Quiet Place" - $31.2 million

"Ready Player One" - $21.8 million

"Blockers" - $15.2 million

"Black Panther" - $7.2 million

"Tyler Perry's Acrimony" - $6.5 million

"I Can Only Imagine" - $6.2 million

"Sherlock Gnomes" - $4.5 million

"Pacific Rim Uprising" - $4 million

"The Miracle Season" - $3.8 million

"Isle of Dogs" - $3.6 million

"A Wrinkle in Time" - $2.7 million

"Love, Simon" - $2.7 million

"Tomb Raider" - $2.3 million

"Chappaquiddick" - $2.3 million

"Paul, Apostle of Christ" - $1.6 million"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	A Quiet Place (Paramount)	$34.0 M	$34.0 M	NEW	1
2	Ready Player One (Warner Bros.)	$23.5 M	$94.8 M	-44%	2
3	Blockers (Universal)	$15.5 M	$15.5 M	NEW	1
4	Black Panther (Disney)	$8.0 M	$664.7 M	-30%	8
5	Tyler Perry's Acrimony (Lionsgate)	$7.8 M	$30.8 M	-55%	2
6	I Can Only Imagine (Roadside)	$7.5 M	$68.1 M	-28%	4
7	Sherlock Gnomes (Paramount / MGM)	$5.2 M	$33.3 M	-26%	3
8	Chappaquiddick (Entertainment Studios)	$4.3 M	$4.3 M	NEW	1
9	Pacific Rim Uprising (Universal)	$4.0 M	$53.8 M	-57%	3
10	Isle of Dogs (Fox Searchlight)	$3.8 M	$11.1 M	+29%	3
11	The Miracle Season
(Mirror / LD Entertainment)	$3.7 M	$3.7 M	NEW	1
12	A Wrinkle in Time (Disney)	$3.2 M	$90.1 M	-34%	5
13	Love, Simon (Fox)	$3.0 M	$37.7 M	-37%	4"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(201846, PRICES_RAW, BOR_RAW, FML_RAW)
