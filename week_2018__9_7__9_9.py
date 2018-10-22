import fml

# 9/7/2018 - 9/9/2018 #

PRICES_RAW = """THE NUN
+FB$615
UNAVAILABLE

SCREENS LOCKED

CRAZY RICH ASIANS
+FB$218
UNAVAILABLE

SCREENS LOCKED

PEPPERMINT
+FB$205
UNAVAILABLE

SCREENS LOCKED

THE MEG
+FB$88
UNAVAILABLE

SCREENS LOCKED

MISSION: IMPOSSIBLE: FALLOUT
+FB$62
UNAVAILABLE

SCREENS LOCKED

SEARCHING
+FB$62
UNAVAILABLE

SCREENS LOCKED

OPERATION FINALE
+FB$52
UNAVAILABLE

SCREENS LOCKED

GOD BLESS THE BROKEN ROAD
+FB$48
UNAVAILABLE

SCREENS LOCKED

CHRISTOPHER ROBIN
+FB$42
UNAVAILABLE

SCREENS LOCKED

BLACKKKLANSMAN
+FB$37
UNAVAILABLE

SCREENS LOCKED

ALPHA
+FB$32
UNAVAILABLE

SCREENS LOCKED

THE HAPPYTIME MURDERS
+FB$30
UNAVAILABLE

SCREENS LOCKED

INCREDIBLES 2
+FB$26
UNAVAILABLE

SCREENS LOCKED

MILE 22
+FB$26
UNAVAILABLE

SCREENS LOCKED
"""

FML_RAW = """"The Nun" - $38.4 million


"Crazy Rich Asians" - $14.2 million


"Peppermint" - $11.8 million


"The Meg" - $5.4 million


"Mission: Impossible: Fallout" - $4.1 million


"Searching" - $3.9 million


"Operation Finale" - $3.3 million


"Christopher Robin" - $2.7 million


"BlacKkKlansman" - $2.4 million


"Alpha" - $2.4 million


"God Bless the Broken Road" - $2.1 million


"The Happytime Murders" - $1.8 million


"Mile 22" - $1.6 million


"Hotel Transylvania 3: Summer Vacation" - $1.1 million


"Incredibles 2" - $1 million
"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	The Nun (Warner / New Line)	$53.0 M	$53.0 M	NEW	1
2	Crazy Rich Asians (Warner Bros.)	$14.3 M	$137.0 M	-34%	4
3	Peppermint (STXfilms)	$14.2 M	$14.2 M	NEW	1
4	The Meg (Warner Bros.)	$5.5 M	$131.1 M	-48%	5
5	Searching (Sony / Screen Gems)	$4.5 M	$14.5 M	-26%	3
6	Mission: Impossible: Fallout (Paramount)	$4.1 M	$212.4 M	-42%	7
7	Operation Finale (MGM)	$3.0 M	$14.0 M	-50%	2
8	God Bless the Broken Road (Freestyle)	$2.9 M	$2.9 M	NEW	1
9	Disney's Christopher Robin (Disney)	$2.8 M	$91.3 M	-47%	6
10	BlacKkKlansman (Focus)	$2.5 M	$43.4 M	-41%	5
11	Alpha (Sony / Studio 8)	$2.3 M	$32.2 M	-49%	4"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(201897, PRICES_RAW, BOR_RAW, FML_RAW)
