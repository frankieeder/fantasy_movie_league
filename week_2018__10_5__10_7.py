import fml

# 10/5/2018 - 10/7/2018 #

PRICES_RAW = """VENOM
+FB$799
UNAVAILABLE

SCREENS LOCKED

A STAR IS BORN
+FB$546
UNAVAILABLE

SCREENS LOCKED

SMALLFOOT
+FB$190
UNAVAILABLE

SCREENS LOCKED

NIGHT SCHOOL
+FB$170
UNAVAILABLE

SCREENS LOCKED

THE HOUSE WITH A CLOCK IN ITS WALLS
+FB$92
UNAVAILABLE

SCREENS LOCKED

A SIMPLE FAVOR
+FB$46
UNAVAILABLE

SCREENS LOCKED

THE NUN
+FB$34
UNAVAILABLE

SCREENS LOCKED

CRAZY RICH ASIANS
+FB$30
UNAVAILABLE

SCREENS LOCKED

HELL FEST
+FB$26
UNAVAILABLE

SCREENS LOCKED

THE PREDATOR
+FB$20
UNAVAILABLE

SCREENS LOCKED

WHITE BOY RICK
+FB$15
UNAVAILABLE

SCREENS LOCKED

PEPPERMINT
+FB$10
UNAVAILABLE

SCREENS LOCKED

THE HATE U GIVE
+FB$8
UNAVAILABLE

SCREENS LOCKED

FREE SOLO
+FB$7
UNAVAILABLE

SCREENS LOCKED

THE MEG
+FB$6"""

FML_RAW = """"Venom" - $63.5 million


"A Star Is Born" - $48.6 million


"Smallfoot" - $13.6 million


"Night School" - $12.7 million


"The House with a Clock in Its Walls" - $7 million


"A Simple Favor" - $3.6 million


"The Nun" - $2.8 million


"Crazy Rich Asians" - $2.7 million


"Hell Fest" - $2.1 million


"The Predator" - $1.8 million


"White Boy Rick" - $1.1 million


"Peppermint" - $848,000


"The Hate U Give" - $746,000


"Free Solo" - $593,000


"The Meg" - $510,000"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Venom (Sony / Columbia)	$68.5 M	$68.5 M	NEW	1
2	A Star is Born (Warner Bros.)	$48.5 M	$48.5 M	NEW	1
3	Smallfoot (Warner Bros.)	$13.8 M	$41.7 M	-40%	2
4	Night School (Universal)	$12.0 M	$47.0 M	-56%	2
5	The House with a Clock in Its Walls
(Universal)	$6.0 M	$53.8 M	-52%	3
6	A Simple Favor (Lionsgate)	$3.6 M	$49.2 M	-45%	4
7	The Nun (Warner / New Line)	$2.6 M	$113.3 M	-52%	5
8	Crazy Rich Asians (Warner Bros.)	$2.5 M	$169.6 M	-39%	8
9	Hell Fest (Lionsgate / CBS Films)	$2.2 M	$9.1 M	-57%	2
10	The Predator (Fox)	$1.3 M	$50.4 M	-66%	4"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(2018105, PRICES_RAW, BOR_RAW, FML_RAW)
