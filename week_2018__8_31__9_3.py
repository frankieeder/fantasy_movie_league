import fml

# 8/31/2018 - 9/3/2018 #

PRICES_RAW = """CRAZY RICH ASIANS
+FB$460
UNAVAILABLE

SCREENS LOCKED

THE MEG
+FB$204
UNAVAILABLE

SCREENS LOCKED

MISSION: IMPOSSIBLE: FALLOUT
+FB$143
UNAVAILABLE

SCREENS LOCKED

OPERATION FINALE
+FB$133
UNAVAILABLE

SCREENS LOCKED

CHRISTOPHER ROBIN
+FB$116
UNAVAILABLE

SCREENS LOCKED

SEARCHING
+FB$111
UNAVAILABLE

SCREENS LOCKED

THE HAPPYTIME MURDERS
+FB$108
UNAVAILABLE

SCREENS LOCKED

ALPHA
+FB$97
UNAVAILABLE

SCREENS LOCKED

BLACKKKLANSMAN
+FB$92
UNAVAILABLE

SCREENS LOCKED

MILE 22
+FB$89
UNAVAILABLE

SCREENS LOCKED

KIN
+FB$82
UNAVAILABLE

SCREENS LOCKED

INCREDIBLES 2
+FB$62
UNAVAILABLE

SCREENS LOCKED

YA VEREMOS
+FB$56
UNAVAILABLE

SCREENS LOCKED

HOTEL TRANSYLVANIA 3: SUMMER VACATION
+FB$49
UNAVAILABLE

SCREENS LOCKED

A.X.L.
+FB$44
"""

FML_RAW = """"Crazy Rich Asians" - $30.6 million


"The Meg" - $14.5 million


"Mission: Impossible: Fallout" - $9.6 million


"Operation Finale" - $8.8 million


"Christopher Robin" - $8 million


"Searching" - $7.1 million


"Alpha" - $6.7 million


"The Happytime Murders" - $6.6 million


"Mile 22" - $6 million


"Kin" - $5.9 million


"BlacKkKlansman" - $5.6 million


"Incredibles 2" - $4.3 million


"A.X.L." - $2.7 million


"Hotel Transylvania 3: Summer Vacation" - $2.7 million


"Ya Veremos" - $2.5 million"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Crazy Rich Asians (Warner Bros.)	$34.0 M	$123.3 M	+37%	3
2	The Meg (Warner Bros.)	$13.7 M	$123.6 M	+7%	4
3	Operation Finale (MGM)	$12.7 M	$15.0 M	NEW	1
4	Mission: Impossible: Fallout (Paramount)	$9.2 M	$206.5 M	+14%	6
5	Searching (Sony / Screen Gems)	$8.8 M	$9.3 M	+2,164%	2
6	Disney's Christopher Robin (Disney)	$7.5 M	$88.0 M	+20%	5
7	The Happytime Murders (STXfilms)	$6.5 M	$19.1 M	-32%	2
8	BlacKkKlansman (Focus)	$6.4 M	$40.5 M	+26%	4
9	Alpha (Sony / Studio 8)	$6.3 M	$29.3 M	+5%	3
10	Mile 22 (STXfilms)	$5.5 M	$33.7 M	-14%	3
11	Kin (Lionsgate / Summit)	$4.5 M	$4.5 M	NEW	1
12	Incredibles 2 (Disney)	$3.7 M	$601.5 M	+125%	12"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(2018831, PRICES_RAW, BOR_RAW, FML_RAW)
