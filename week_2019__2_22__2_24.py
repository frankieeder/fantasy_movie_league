import fml

# 2/22/2019 - 2/24/2019 #

PRICES_RAW = """HOW TO TRAIN YOUR DRAGON: THE HIDDEN WORLD
+$664
UNAVAILABLE

SCREENS LOCKED

ALITA: BATTLE ANGEL
+$232
UNAVAILABLE

SCREENS LOCKED

FIGHTING WITH MY FAMILY
+$167
UNAVAILABLE

SCREENS LOCKED

THE LEGO MOVIE 2: THE SECOND PART
+$157
UNAVAILABLE

SCREENS LOCKED

ISN'T IT ROMANTIC
+$115
UNAVAILABLE

SCREENS LOCKED

WHAT MEN WANT
+$84
UNAVAILABLE

SCREENS LOCKED

HAPPY DEATH DAY 2U
+$58
UNAVAILABLE

SCREENS LOCKED

RUN THE RACE
+$55
UNAVAILABLE

SCREENS LOCKED

THE UPSIDE
+$54
UNAVAILABLE

SCREENS LOCKED

GREEN BOOK
+$41
UNAVAILABLE

SCREENS LOCKED

COLD PURSUIT
+$41
UNAVAILABLE

SCREENS LOCKED

GLASS
+$29
UNAVAILABLE

SCREENS LOCKED

THE PRODIGY
+$21
UNAVAILABLE

SCREENS LOCKED

SPIDER-MAN: INTO THE SPIDER-VERSE
+$17
UNAVAILABLE

SCREENS LOCKED

AQUAMAN
+$14"""

FML_RAW = """"How to Train Your Dragon: The Hidden World" - $44.7 million 
"Alita: Battle Angel" - $12.9 million 
"The Lego Movie 2: The Second Part" - $11.2 million 
"Fighting with My Family" - $10.8 million
"Isn't It Romantic" - $6.1 million
"What Men Want" - $5 million
"Happy Death Day 2U" - $4 million
"The Upside" - $2.9 million
"Cold Pursuit" - $2.7 million
"Run the Race" - $2.2 million
"Green Book" - $2.2 million
"Glass" - $1.8 million 
"The Prodigy" - $1.4 million
"Spider-Man: Into the Spider-Verse" - $1.2 million
"Aquaman" - $966,000"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	How to Train Your Dragon: The Hidden World
(Universal / DreamWorks Animation)	$46.0 M	$48.5 M	NEW	1
2	Alita: Battle Angel (Fox)	$16.0 M	$65.3 M	-44%	2
3	The LEGO Movie 2: The Second Part
(Warner Bros.)	$11.0 M	$84.8 M	-47%	3
4	Isn't It Romantic (Warner / New Line)	$8.5 M	$34.8 M	-40%	2
5	Fighting With My Family (MGM)	$8.0 M	$8.2 M	+5,665%	2
6	What Men Want (Paramount)	$6.5 M	$46.5 M	-39%	3
7	Happy Death Day 2U (Universal)	$4.8 M	$21.5 M	-49%	2
8	The Upside (STXfilms)	$4.3 M	$100.9 M	-22%	7
9	Cold Pursuit (Lionsgate / Summit)	$3.1 M	$26.9 M	-48%	3
10	Green Book (Universal / DreamWorks)	$3.0 M	$70.5 M	+4%	15
11	Run the Race (Roadside)	$2.9 M	$2.9 M	NEW	1
12	Glass (Universal)	$2.2 M	$108.4 M	-44%	6"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(2019222, PRICES_RAW, BOR_RAW, FML_RAW)

