import fml

# 3/30/2018 - 4/1/2018 #

PRICES_RAW = """READY PLAYER ONE
+FB$522
UNAVAILABLE

SCREENS LOCKED

ACRIMONY
+FB$219
UNAVAILABLE

SCREENS LOCKED

PACIFIC RIM UPRISING
+FB$167
UNAVAILABLE

SCREENS LOCKED

I CAN ONLY IMAGINE
+FB$153
UNAVAILABLE

SCREENS LOCKED

BLACK PANTHER
+FB$148
UNAVAILABLE

SCREENS LOCKED

SHERLOCK GNOMES
+FB$91
UNAVAILABLE

SCREENS LOCKED

GOD'S NOT DEAD: A LIGHT IN DARKNESS
+FB$75
UNAVAILABLE

SCREENS LOCKED

LOVE, SIMON
+FB$71
UNAVAILABLE

SCREENS LOCKED

ISLE OF DOGS
+FB$69
UNAVAILABLE

SCREENS LOCKED

TOMB RAIDER
+FB$65
UNAVAILABLE

SCREENS LOCKED

A WRINKLE IN TIME
+FB$54
UNAVAILABLE

SCREENS LOCKED

GAME NIGHT
+FB$41
UNAVAILABLE

SCREENS LOCKED

PAUL, APOSTLE OF CHRIST
+FB$41
UNAVAILABLE

SCREENS LOCKED

MIDNIGHT SUN
+FB$28
UNAVAILABLE

SCREENS LOCKED

UNSANE
+FB$23"""

FML_RAW = """"Ready Player One" - $36.7 million

"Acrimony" - $13.2 million

"Pacific Rim Uprising" - $11.7 million

"Black Panther" - $11.4 million

"I Can Only Imagine" - $11.2 million

"Sherlock Gnomes" - $5.8 million

"God's Not Dead: A Light in Darkness" - $5.4 million

"Love, Simon" - $5.1 million

"Isle of Dogs" - $4.9 million

"Tomb Raider" - $4.7 million

"A Wrinkle in Time" - $4.2 million

"Game Night" - $3.2 million

"Paul, Apostle of Christ" - $2.7 million

"Midnight Sun" - $2 million

"Unsane" - $1.8 million
"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Ready Player One (Warner Bros.)	$43.0 M	$56.0 M	NEW	1
2	Acrimony (Lionsgate)	$18.5 M	$18.5 M	NEW	1
3	Black Panther (Disney)	$11.2 M	$650.3 M	-35%	7
4	Pacific Rim Uprising (Universal)	$10.8 M	$47.5 M	-62%	2
5	I Can Only Imagine (Roadside)	$10.5 M	$55.2 M	-23%	3
6	Sherlock Gnomes (Paramount / MGM)	$6.7 M	$22.7 M	-37%	2
7	Love, Simon (Fox)	$5.1 M	$32.1 M	-33%	3
8	Tomb Raider (Warner / MGM)	$4.7 M	$50.5 M	-53%	3
9	God's Not Dead: A Light in Darkness	(Pure Flix)	$4.2 M	$4.2 M	NEW	1
10	A Wrinkle in Time (Disney)	$4.1 M	$82.3 M	-50%	4
11	Paul, Apostle of Christ (Sony / AFFIRM)	$4.0 M	$12.1 M	-23%	2
12	Isle of Dogs (Fox Searchlight)	$3.2 M	$6.2 M	+98%	2"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(2018330, PRICES_RAW, BOR_RAW, FML_RAW)
