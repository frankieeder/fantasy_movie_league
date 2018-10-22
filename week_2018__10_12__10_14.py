import fml

# 10/12/2018 - 10/14/2018 #

PRICES_RAW = """VENOM
+FB$501
UNAVAILABLE

SCREENS LOCKED

A STAR IS BORN
+FB$412
UNAVAILABLE

SCREENS LOCKED

FIRST MAN
+FB$371
UNAVAILABLE

SCREENS LOCKED

GOOSEBUMPS 2: HAUNTED HALLOWEEN
+FB$265
UNAVAILABLE

SCREENS LOCKED

SMALLFOOT
+FB$150
UNAVAILABLE

SCREENS LOCKED

BAD TIMES AT THE EL ROYALE
+FB$149
UNAVAILABLE

SCREENS LOCKED

NIGHT SCHOOL
+FB$109
UNAVAILABLE

SCREENS LOCKED

THE HOUSE WITH A CLOCK IN ITS WALLS
+FB$57
UNAVAILABLE

SCREENS LOCKED

A SIMPLE FAVOR
+FB$27
UNAVAILABLE

SCREENS LOCKED

THE NUN
+FB$21
UNAVAILABLE

SCREENS LOCKED

THE HATE U GIVE
+FB$21
UNAVAILABLE

SCREENS LOCKED

COLETTE
+FB$21
UNAVAILABLE

SCREENS LOCKED

CRAZY RICH ASIANS
+FB$19
UNAVAILABLE

SCREENS LOCKED

FREE SOLO
+FB$14
UNAVAILABLE

SCREENS LOCKED

BEST OF THE REST
+FB$12"""

FML_RAW = """"Venom" - $31.2 million


"A Star Is Born" - $28.3 million


"First Man" - $23.5 million


"Goosebumps 2: Haunted Halloween" - $17.3 million


"Smallfoot" - $9 million


"Bad Times at the El Royale" - $8 million


"Night School" - $6.2 million


"The House with a Clock in Its Walls" - $4.2 million


"A Simple Favor" - $1.8 million


"The Nun" - $1.4 million


"Colette" - $1.4 million


"The Hate U Give" - $1.3 million


"Crazy Rich Asians" - $1.2 million


"Free Solo" - $1 million


"Best of the Rest" - $760,000"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Venom (Sony / Columbia)	$31.0 M	$137.0 M	-61%	2
2	A Star is Born (Warner Bros.)	$29.0 M	$94.0 M	-32%	2
3	First Man (Universal / DreamWorks)	$21.5 M	$21.5 M	NEW	1
4	Goosebumps 2: Haunted Halloween
(Sony / Columbia)	$15.5 M	$15.5 M	NEW	1
5	Smallfoot (Warner Bros.)	$9.5 M	$57.7 M	-34%	3
6	Bad Times at the El Royale (Fox)	$9.2 M	$9.2 M	NEW	1
7	Night School (Universal)	$7.3 M	$58.9 M	-42%	3
8	The House with a Clock in Its Walls
(Universal)	$3.8 M	$61.9 M	-48%	4
9	A Simple Favor (Lionsgate)	$2.0 M	$52.6 M	-42%	5
10	The Nun (Warner / New Line)	$1.5 M	$116.1 M	-45%	6
11	Gosnell (GVN Releasing)	$1.4 M	$1.4 M	NEW	1
12	The Hate U Give (Fox)	$1.3 M	$2.0 M	+154%	2"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(20181012, PRICES_RAW, BOR_RAW, FML_RAW)

