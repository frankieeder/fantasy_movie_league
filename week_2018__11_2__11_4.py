import fml

# 11/2/2018 - 11/4/2018 #

PRICES_RAW = """BOHEMIAN RHAPSODY
+FB$510
UNAVAILABLE

SCREENS LOCKED

THE NUTCRACKER AND THE FOUR REALMS
+FB$260
UNAVAILABLE

SCREENS LOCKED

HALLOWEEN
+FB$201
UNAVAILABLE

SCREENS LOCKED

NOBODY'S FOOL
+FB$180
UNAVAILABLE

SCREENS LOCKED

A STAR IS BORN
+FB$127
UNAVAILABLE

SCREENS LOCKED

VENOM
+FB$80
UNAVAILABLE

SCREENS LOCKED

GOOSEBUMPS 2: HAUNTED HALLOWEEN
+FB$62
UNAVAILABLE

SCREENS LOCKED

SMALLFOOT
+FB$42
UNAVAILABLE

SCREENS LOCKED

THE HATE U GIVE
+FB$42
UNAVAILABLE

SCREENS LOCKED

HUNTER KILLER
+FB$39
UNAVAILABLE

SCREENS LOCKED

FIRST MAN
+FB$35
UNAVAILABLE

SCREENS LOCKED

SUSPIRIA
+FB$31
UNAVAILABLE

SCREENS LOCKED

NIGHT SCHOOL
+FB$24
UNAVAILABLE

SCREENS LOCKED

MID90S
+FB$23
UNAVAILABLE

SCREENS LOCKED

THE OLD MAN & THE GUN
+FB$17"""

FML_RAW = """"Bohemian Rhapsody" - $31.8 million


"The Nutcracker and the Four Realms" - $19.4 million


"Halloween" - $14.1 million


"Nobody's Fool" - $13.8 million


"A Star Is Born" - $9.7 million


"Venom" - $6.2 million


"Goosebumps 2: Haunted Halloween" - $4.8 million


"The Hate U Give" - $3.3 million


"Smallfoot" - $3.3 million


"Hunter Killer" - $3 million


"First Man" - $2.8 million


"Suspiria" - $2.2 million


"Night School" - $1.9 million


"Mid90s" - $1.8 million


"The Old Man & The Gun" - $1.3 million"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Bohemian Rhapsody (Fox)	$44.5 M	$44.5 M	NEW	1
2	The Nutcracker and the Four Realms
(Disney)	$18.3 M	$18.3 M	NEW	1
3	Nobody's Fool (Paramount)	$15.7 M	$15.7 M	NEW	1
4	Halloween (Universal)	$14.0 M	$155.5 M	-55%	3
5	A Star is Born (Warner Bros.)	$9.7 M	$164.7 M	-31%	5
6	Venom (Sony / Columbia)	$6.2 M	$197.3 M	-42%	5
7	Goosebumps 2: Haunted Halloween
(Sony / Columbia)	$5.0 M	$45.3 M	-31%	4
8	The Hate U Give (Fox)	$3.3 M	$23.6 M	-35%	5
9	Hunter Killer
(Lionsgate / Summit Premiere)	$3.2 M	$12.8 M	-52%	2
10	Smallfoot (Warner Bros.)	$3.1 M	$76.7 M	-35%	6
11	First Man (Universal / DreamWorks)	$2.5 M	$42.2 M	-49%	4
12	Suspiria (Amazon Studios)	$2.0 M	$2.3 M	+987%	2"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(2018112, PRICES_RAW, BOR_RAW, FML_RAW)

