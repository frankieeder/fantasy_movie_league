import fml

# 9/28/2018 - 9/30/2018 #

PRICES_RAW = """NIGHT SCHOOL
+FB$616
UNAVAILABLE

SCREENS LOCKED

SMALLFOOT
+FB$363
UNAVAILABLE

SCREENS LOCKED

THE HOUSE WITH A CLOCK IN ITS WALLS
+FB$318
UNAVAILABLE

SCREENS LOCKED

A SIMPLE FAVOR
+FB$148
UNAVAILABLE

SCREENS LOCKED

HELL FEST
+FB$128
UNAVAILABLE

SCREENS LOCKED

THE NUN
+FB$102
UNAVAILABLE

SCREENS LOCKED

CRAZY RICH ASIANS
+FB$85
UNAVAILABLE

SCREENS LOCKED

THE PREDATOR
+FB$83
UNAVAILABLE

SCREENS LOCKED

WHITE BOY RICK
+FB$55
UNAVAILABLE

SCREENS LOCKED

PEPPERMINT
+FB$41
UNAVAILABLE

SCREENS LOCKED

LITTLE WOMEN
+FB$33
UNAVAILABLE

SCREENS LOCKED

FAHRENHEIT 11/9
+FB$30
UNAVAILABLE

SCREENS LOCKED

SEARCHING
+FB$25
UNAVAILABLE

SCREENS LOCKED

THE MEG
+FB$24
UNAVAILABLE

SCREENS LOCKED

LIFE ITSELF
+FB$20"""

FML_RAW = """"Night School" - $27.6 million


"Smallfoot" - $23 million


"The House with a Clock in Its Walls" - $14.8 million


"A Simple Favor" - $6.9 million


"Hell Fest" - $5.6 million


"The Nun" - $5.5 million


"Crazy Rich Asians" - $4.5 million


"The Predator" - $4.3 million


"White Boy Rick" - $2.9 million


"Peppermint" - $2.1 million


"Searching" - $1.3 million


"Fahrenheit 11/9" - $1.3 million


"The Meg" - $1.2 million


"Little Women" - $1.1 million


"Life Itself" - $1 million"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Night School (Universal)	$29.5 M	$29.5 M	NEW	1
2	Smallfoot (Warner Bros.)	$24.5 M	$24.5 M	NEW	1
3	The House with a Clock in Its Walls
(Universal)	$15.0 M	$47.7 M	-44%	2
4	A Simple Favor (Lionsgate)	$7.2 M	$43.7 M	-30%	3
5	Hell Fest (Lionsgate / CBS Films)	$5.4 M	$5.4 M	NEW	1
6	The Nun (Warner / New Line)	$5.2 M	$108.7 M	-48%	4
7	Crazy Rich Asians (Warner Bros.)	$4.6 M	$166.3 M	-28%	7
8	The Predator (Fox)	$4.3 M	$48.2 M	-53%	3
9	White Boy Rick (Sony / Studio 8)	$2.7 M	$22.1 M	-44%	3
10	Peppermint (STXfilms)	$2.1 M	$33.9 M	-43%	4"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(2018928, PRICES_RAW, BOR_RAW, FML_RAW)
