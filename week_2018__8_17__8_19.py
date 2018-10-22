import fml

# 7/17/2018 - 7/19/2018 #

PRICES_RAW = """CRAZY RICH ASIANS
+FB$358
UNAVAILABLE

SCREENS LOCKED

THE MEG
+FB$356
UNAVAILABLE

SCREENS LOCKED

MILE 22
+FB$296
UNAVAILABLE

SCREENS LOCKED

MISSION: IMPOSSIBLE: FALLOUT
+FB$193
UNAVAILABLE

SCREENS LOCKED

BLACKKKLANSMAN
+FB$129
UNAVAILABLE

SCREENS LOCKED

CHRISTOPHER ROBIN
+FB$128
UNAVAILABLE

SCREENS LOCKED

ALPHA
+FB$89
UNAVAILABLE

SCREENS LOCKED

SLENDER MAN
+FB$84
UNAVAILABLE

SCREENS LOCKED

THE SPY WHO DUMPED ME
+FB$61
UNAVAILABLE

SCREENS LOCKED

MAMMA MIA! HERE WE GO AGAIN
+FB$56
UNAVAILABLE

SCREENS LOCKED

HOTEL TRANSYLVANIA 3: SUMMER VACATION
+FB$55
UNAVAILABLE

SCREENS LOCKED

THE EQUALIZER 2
+FB$51
UNAVAILABLE

SCREENS LOCKED

ANT-MAN AND THE WASP
+FB$43
UNAVAILABLE

SCREENS LOCKED

INCREDIBLES 2
+FB$39
UNAVAILABLE

SCREENS LOCKED

DOG DAYS
+FB$23"""

FML_RAW = """"The Meg" - $20.3 million


"Crazy Rich Asians" - $18.4 million


"Mile 22" - $16.7 million


"Mission: Impossible: Fallout" - $11 million


"Christopher Robin" - $7.4 million


"BlacKkKlansman" - $7.1 million


"Alpha" - $5.2 million


"Slender Man" - $4.6 million


"The Spy Who Dumped Me" - $3.7 million


"Mamma Mia! Here We Go Again" - $3.6 million


"Hotel Transylvania 3: Summer Vacation" - $3.5 million


"The Equalizer 2" - $3.2 million


"Ant-Man and the Wasp" - $2.7 million


"Incredibles 2" - $2.4 million


"Dog Days" - $1.3 million"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Crazy Rich Asians (Warner Bros.)	$24.0 M	$34.0 M	NEW	1
2	The Meg (Warner Bros.)	$21.5 M	$84.8 M	-53%	2
3	Mile 22 (STXfilms)	$17.0 M	$17.0 M	NEW	1
4	Mission: Impossible: Fallout (Paramount)	$11.5 M	$181.5 M	-41%	4
5	Alpha (Sony / Columbia)	$8.0 M	$8.0 M	NEW	1
6	Disney's Christopher Robin (Disney)	$7.9 M	$66.2 M	-39%	3
7	BlacKkKlansman (Focus)	$6.4 M	$22.4 M	-41%	2
8	Slender Man (Sony / Screen Gems)	$4.9 M	$21.4 M	-57%	2
9	Mamma Mia! Here We Go Again (Universal)	$3.6 M	$111.7 M	-39%	5
10	Hotel Transylvania 3: Summer Vacation
(Sony / Columbia)	$3.5 M	$153.9 M	-33%	6
11	The Spy Who Dumped Me (Lionsgate)	$3.3 M	$31.0 M	-49%	3
12	The Equalizer 2 (Sony / Columbia)	$3.1 M	$95.2 M	-43%	5
13	Ant-Man and The Wasp (Disney)	$2.6 M	$208.3 M	-37%	7
14	Incredibles 2 (Disney)	$2.4 M	$594.3 M	-30%	10"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(2018717, PRICES_RAW, BOR_RAW, FML_RAW)
