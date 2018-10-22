import fml

# 8/24/2018 - 8/26/2018 #

PRICES_RAW = """CRAZY RICH ASIANS
+FB$318
UNAVAILABLE

SCREENS LOCKED

THE HAPPYTIME MURDERS
+FB$264
UNAVAILABLE

SCREENS LOCKED

THE MEG
+FB$201
UNAVAILABLE

SCREENS LOCKED

MILE 22
+FB$129
UNAVAILABLE

SCREENS LOCKED

MISSION: IMPOSSIBLE: FALLOUT
+FB$127
UNAVAILABLE

SCREENS LOCKED

CHRISTOPHER ROBIN
+FB$106
UNAVAILABLE

SCREENS LOCKED

ALPHA
+FB$102
UNAVAILABLE

SCREENS LOCKED

BLACKKKLANSMAN
+FB$84
UNAVAILABLE

SCREENS LOCKED

A.X.L.
+FB$58
UNAVAILABLE

SCREENS LOCKED

HOTEL TRANSYLVANIA 3: SUMMER VACATION
+FB$45
UNAVAILABLE

SCREENS LOCKED

SLENDER MAN
+FB$40
UNAVAILABLE

SCREENS LOCKED

MAMMA MIA! HERE WE GO AGAIN
+FB$35
UNAVAILABLE

SCREENS LOCKED

ANT-MAN AND THE WASP
+FB$29
UNAVAILABLE

SCREENS LOCKED

THE EQUALIZER 2
+FB$28
UNAVAILABLE

SCREENS LOCKED

INCREDIBLES 2
+FB$27"""

FML_RAW = """"Crazy Rich Asians" - $16.9 million


"The Happytime Murders" - $14.8 million


"The Meg" - $11.2 million


"Mile 22" - $7.5 million


"Mission: Impossible: Fallout" - $6.8 million


"Christopher Robin" - $5.9 million


"Alpha" - $5.7 million


"BlacKkKlansman" - $4.8 million


"Hotel Transylvania 3: Summer Vacation" - $2.6 million


"Slender Man" - $2.1 million


"A.X.L." - $2.1 million


"Mamma Mia! Here We Go Again" - $2 million


"Ant-Man and the Wasp" - $1.7 million


"The Equalizer 2" - $1.6 million


"Incredibles 2" - $1.5 million"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Crazy Rich Asians (Warner Bros.)	$20.0 M	$71.3 M	-25%	2
2	The Happytime Murders (STXfilms)	$12.8 M	$12.8 M	NEW	1
3	The Meg (Warner Bros.)	$12.7 M	$105.3 M	-40%	3
4	Mission: Impossible: Fallout (Paramount)	$7.1 M	$193.1 M	-34%	5
5	Disney's Christopher Robin (Disney)	$6.3 M	$77.6 M	-29%	4
6	Mile 22 (STXfilms)	$6.2 M	$25.5 M	-55%	2
7	Alpha (Sony / Studio 8)	$6.0 M	$20.6 M	-42%	2
8	BlacKkKlansman (Focus)	$5.4 M	$32.0 M	-27%	3
9	A-X-L (Global Road)	$3.3 M	$3.3 M	NEW	1
10	Hotel Transylvania 3: Summer Vacation
(Sony / Columbia)	$2.8 M	$158.9 M	-26%	7
11	Slender Man (Sony / Screen Gems)	$2.2 M	$24.8 M	-54%	3
12	Mamma Mia! Here We Go Again (Universal)	$2.0 M	$115.3 M	-41%	6"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(2018824, PRICES_RAW, BOR_RAW, FML_RAW)
