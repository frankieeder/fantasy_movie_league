import fml

# 10/19/2018 - 10/21/2018 #

PRICES_RAW = """FRI: HALLOWEEN
+FB$394
UNAVAILABLE

SCREENS LOCKED

SAT: HALLOWEEN
+FB$352
UNAVAILABLE

SCREENS LOCKED

A STAR IS BORN
+FB$252
UNAVAILABLE

SCREENS LOCKED

SUN: HALLOWEEN
+FB$217
UNAVAILABLE

SCREENS LOCKED

VENOM
+FB$216
UNAVAILABLE

SCREENS LOCKED

FIRST MAN
+FB$148
UNAVAILABLE

SCREENS LOCKED

GOOSEBUMPS 2: HAUNTED HALLOWEEN
+FB$143
UNAVAILABLE

SCREENS LOCKED

THE HATE U GIVE
+FB$118
UNAVAILABLE

SCREENS LOCKED

SMALLFOOT
+FB$80
UNAVAILABLE

SCREENS LOCKED

NIGHT SCHOOL
+FB$59
UNAVAILABLE

SCREENS LOCKED

BAD TIMES AT THE EL ROYALE
+FB$48
UNAVAILABLE

SCREENS LOCKED

THE HOUSE WITH A CLOCK IN ITS WALLS
+FB$28
UNAVAILABLE

SCREENS LOCKED

THE OLD MAN & THE GUN
+FB$23
UNAVAILABLE

SCREENS LOCKED

FREE SOLO
+FB$14
UNAVAILABLE

SCREENS LOCKED

BEAUTIFUL BOY
+FB$12"""

FML_RAW = """"Halloween" (Friday) - $32.4 million


"Halloween" (Saturday) - $26.4 million


"A Star Is Born" - $19.2 million


"Venom" - $16.9 million


"Halloween" (Sunday) - $16.6 million


"First Man" - $10.5 million


"Goosebumps 2: Haunted Halloween" - $9.4 million


"The Hate U Give" - $6.7 million


"Smallfoot" - $5.8 million


"Night School" - $4.5 million


"Bad Times at the El Royale" - $3.2 million


"The House with a Clock in Its Walls" - $2.1 million


"The Old Man & The Gun" - $1.4 million


"Free Solo" - $1 million


"Beautiful Boy" - $1 million"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Halloween (Universal)	$75.0 M	$75.0 M	NEW	1
2	A Star is Born (Warner Bros.)	$18.5 M	$125.8 M	-35%	3
3	Venom (Sony / Columbia)	$16.5 M	$169.8 M	-53%	3
4	First Man (Universal / DreamWorks)	$9.3 M	$30.8 M	-42%	2
5	Goosebumps 2: Haunted Halloween
(Sony / Columbia)	$9.2 M	$28.2 M	-42%	2
6	The Hate U Give (Fox)	$7.7 M	$10.9 M	+343%	3
7	Smallfoot (Warner Bros.)	$5.7 M	$65.2 M	-37%	4
8	Night School (Universal)	$4.6 M	$66.4 M	-41%	4
9	Bad Times at the El Royale (Fox)	$3.3 M	$13.3 M	-54%	2
10	The House with a Clock in Its Walls
(Universal)	$1.9 M	$65.0 M	-51%	5
11	The Old Man & the Gun (Fox Searchlight)	$1.8 M	$3.9 M	+96%	4"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(20181019, PRICES_RAW, BOR_RAW, FML_RAW)

