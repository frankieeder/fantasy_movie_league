import fml

# 9/21/2018 - 9/23/2018 #

PRICES_RAW = """
THE HOUSE WITH A CLOCK IN ITS WALLS
+FB$476
UNAVAILABLE

SCREENS LOCKED

THE PREDATOR
+FB$216
UNAVAILABLE

SCREENS LOCKED

A SIMPLE FAVOR
+FB$202
UNAVAILABLE

SCREENS LOCKED

THE NUN
+FB$173
UNAVAILABLE

SCREENS LOCKED

LIFE ITSELF
+FB$143
UNAVAILABLE

SCREENS LOCKED

CRAZY RICH ASIANS
+FB$127
UNAVAILABLE

SCREENS LOCKED

FAHRENHEIT 11/9
+FB$115
UNAVAILABLE

SCREENS LOCKED

WHITE BOY RICK
+FB$98
UNAVAILABLE

SCREENS LOCKED

PEPPERMINT
+FB$75
UNAVAILABLE

SCREENS LOCKED

ASSASSINATION NATION
+FB$69
UNAVAILABLE

SCREENS LOCKED

THE MEG
+FB$49
UNAVAILABLE

SCREENS LOCKED

SEARCHING
+FB$41
UNAVAILABLE

SCREENS LOCKED

MISSION: IMPOSSIBLE: FALLOUT
+FB$25
UNAVAILABLE

SCREENS LOCKED

CHRISTOPHER ROBIN
+FB$25
UNAVAILABLE

SCREENS LOCKED

UNBROKEN: PATH TO REDEMPTION
+FB$24"""

FML_RAW = """"The House with a Clock in Its Walls" - $23.2 million
"A Simple Favor" - $10.6 million
"The Predator" - $10 million
"The Nun" - $8.4 million
"Crazy Rich Asians" - $5.9 million
"Fahrenheit 11/9" - $5 million
"White Boy Rick" - $4.2 million
"Life Itself" - $3.8 million
"Peppermint" - $2.8 million
"The Meg" - $2.5 million
"Searching" - $2 million
"Mission: Impossible: Fallout" - $1.4 million
"Christopher Robin" - $1.3 million
"Assassination Nation" - $1.1 million
"Unbroken: Path to Redemption" - $952,000"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	The House with a Clock in Its Walls
(Universal)	$21.7 M	$21.7 M	NEW	1
2	The Predator (Fox)	$9.3 M	$41.3 M	-62%	2
3	A Simple Favor (Lionsgate)	$8.8 M	$31.0 M	-45%	2
4	The Nun (Warner / New Line)	$8.3 M	$99.2 M	-54%	3
5	Fahrenheit 11/9 (Briarcliff)	$6.0 M	$6.0 M	NEW	1
6	Crazy Rich Asians (Warner Bros.)	$5.9 M	$158.8 M	-32%	6
7	White Boy Rick (Sony / Studio 8)	$4.8 M	$17.3 M	-46%	2
8	Life Itself (Amazon Studios)	$4.7 M	$4.7 M	NEW	1
9	Peppermint (STXfilms)	$3.2 M	$29.9 M	-47%	3
10	The Meg (Warner Bros.)	$2.4 M	$140.6 M	-38%	7
11	Assassination Nation (NEON)	$2.3 M	$2.3 M	NEW	1
12	Searching (Sony / Screen Gems)	$2.2 M	$23.2 M	-31%	5"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(2018921, PRICES_RAW, BOR_RAW, FML_RAW)
