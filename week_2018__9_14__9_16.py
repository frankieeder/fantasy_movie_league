import fml

# 9/14/2018 - 9/16/2018 #

PRICES_RAW = """THE PREDATOR
+FB$408
UNAVAILABLE

SCREENS LOCKED

THE NUN
+FB$338
UNAVAILABLE

SCREENS LOCKED

A SIMPLE FAVOR
+FB$257
UNAVAILABLE

SCREENS LOCKED

WHITE BOY RICK
+FB$137
UNAVAILABLE

SCREENS LOCKED

CRAZY RICH ASIANS
+FB$131
UNAVAILABLE

SCREENS LOCKED

PEPPERMINT
+FB$86
UNAVAILABLE

SCREENS LOCKED

THE MEG
+FB$43
UNAVAILABLE

SCREENS LOCKED

SEARCHING
+FB$40
UNAVAILABLE

SCREENS LOCKED

UNBROKEN: PATH TO REDEMPTION
+FB$40
UNAVAILABLE

SCREENS LOCKED

CHRISTOPHER ROBIN
+FB$31
UNAVAILABLE

SCREENS LOCKED

MISSION: IMPOSSIBLE: FALLOUT
+FB$28
UNAVAILABLE

SCREENS LOCKED

BLACKKKLANSMAN
+FB$22
UNAVAILABLE

SCREENS LOCKED

OPERATION FINALE
+FB$21
UNAVAILABLE

SCREENS LOCKED

ALPHA
+FB$18
UNAVAILABLE

SCREENS LOCKED

THE WIFE
+FB$18"""

FML_RAW = """"The Predator" - $27.4 million


"The Nun" - $19.4 million


"A Simple Favor" - $17.9 million


"White Boy Rick" - $8.7 million


"Crazy Rich Asians" - $7.8 million


"Peppermint" - $6.8 million


"The Meg" - $3.3 million


"Searching" - $3.2 million


"Unbroken: Path to Redemption" - $2.5 million


"Christopher Robin" - $2.3 million


"Mission: Impossible: Fallout" - $2.2 million


"BlacKkKlansman" - $1.6 million


"Operation Finale" - $1.4 million


"Alpha" - $1.2 million


"The Wife" - $1 million"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	The Predator (Fox)	$26.8 M	$26.8 M	NEW	1
2	The Nun (Warner / New Line)	$20.5 M	$88.0 M	-62%	2
3	A Simple Favor (Lionsgate)	$17.5 M	$17.5 M	NEW	1
4	Crazy Rich Asians (Warner Bros.)	$9.7 M	$150.8 M	-26%	5
5	White Boy Rick (Sony / Studio 8)	$9.4 M	$9.4 M	NEW	1
6	Peppermint (STXfilms)	$6.7 M	$25.2 M	-50%	2
7	Unbroken: Path to Redemption (Pure Flix)	$3.8 M	$3.8 M	NEW	1
8	The Meg (Warner Bros.)	$3.6 M	$136.8 M	-41%	6
9	Searching (Sony / Screen Gems)	$3.0 M	$19.4 M	-34%	4
10	Mission: Impossible: Fallout (Paramount)	$2.6 M	$216.5 M	-33%	8
11	Disney's Christopher Robin (Disney)	$2.5 M	$95.5 M	-27%	7"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(2018914, PRICES_RAW, BOR_RAW, FML_RAW)
