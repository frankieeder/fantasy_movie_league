import fml

# 10/26/2018 - 10/28/2018 #

PRICES_RAW = """HALLOWEEN
+FB$666
UNAVAILABLE

SCREENS LOCKED

A STAR IS BORN
+FB$243
UNAVAILABLE

SCREENS LOCKED

HUNTER KILLER
+FB$202
UNAVAILABLE

SCREENS LOCKED

VENOM
+FB$201
UNAVAILABLE

SCREENS LOCKED

GOOSEBUMPS 2: HAUNTED HALLOWEEN
+FB$128
UNAVAILABLE

SCREENS LOCKED

THE HATE U GIVE
+FB$100
UNAVAILABLE

SCREENS LOCKED

FIRST MAN
+FB$89
UNAVAILABLE

SCREENS LOCKED

MID90S
+FB$88
UNAVAILABLE

SCREENS LOCKED

SMALLFOOT
+FB$86
UNAVAILABLE

SCREENS LOCKED

NIGHT SCHOOL
+FB$57
UNAVAILABLE

SCREENS LOCKED

INDIVISIBLE
+FB$39
UNAVAILABLE

SCREENS LOCKED

THE OLD MAN & THE GUN
+FB$36
UNAVAILABLE

SCREENS LOCKED

BAD TIMES AT THE EL ROYALE
+FB$34
UNAVAILABLE

SCREENS LOCKED

JOHNNY ENGLISH STRIKES AGAIN
+FB$33
UNAVAILABLE

SCREENS LOCKED

THE HOUSE WITH A CLOCK IN ITS WALLS
+FB$16"""

FML_RAW = """"Halloween" - $35.4 million


"A Star Is Born" - $13.1 million


"Venom" - $10.3 million


"Hunter Killer" - $10.2 million


"Goosebumps 2: Haunted Halloween" - $6.5 million


"The Hate U Give" - $5.3 million


"First Man" - $4.8 million


"Smallfoot" - $4.8 million


"Mid90s" - $3.7 million


"Night School" - $3 million


"Bad Times at the El Royale" - $1.8 million


"The Old Man & The Gun" - $1.5 million


"Johnny English Strikes Again" - $1.3 million


"Indivisible" - $1 million


"The House with a Clock in Its Walls" - $906,000
"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Halloween (Universal)	$36.5 M	$131.5 M	-52%	2
2	A Star is Born (Warner Bros.)	$14.0 M	$148.5 M	-27%	4
3	Venom (Sony / Columbia)	$10.8 M	$187.3 M	-40%	4
4	Hunter Killer
(Lionsgate / Summit Premiere)	$8.3 M	$8.3 M	NEW	1
5	Goosebumps 2: Haunted Halloween
(Sony / Columbia)	$6.7 M	$37.6 M	-31%	3
6	The Hate U Give (Fox)	$5.1 M	$18.3 M	-33%	4
7	Smallfoot (Warner Bros.)	$4.8 M	$72.6 M	-27%	5
8	First Man (Universal / DreamWorks)	$4.7 M	$37.5 M	-44%	3
9	Mid90s (A24)	$3.8 M	$4.2 M	+1,372%	2
10	Night School (Universal)	$3.0 M	$71.2 M	-39%	5
11	The Old Man & the Gun (Fox Searchlight)	$1.8 M	$7.3 M	-16%	5
12	Indivisible (Pure Flix)	$1.7 M	$1.7 M	NEW	1
13	Bad Times at the El Royale (Fox)	$1.6 M	$16.7 M	-53%	3
14	Johnny English Strikes Again (Universal)	$1.5 M	$1.5 M	NEW	1"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(20181026, PRICES_RAW, BOR_RAW, FML_RAW)
