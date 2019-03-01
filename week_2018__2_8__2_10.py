import fml

# 2/8/2018 - 2/10/2018 #

PRICES_RAW = """THE LEGO MOVIE 2: THE SECOND PART
+$405
UNAVAILABLE

SCREENS LOCKED

HAPPY DEATH DAY 2U
+$307
UNAVAILABLE

SCREENS LOCKED

ALITA: BATTLE ANGEL
+$276
UNAVAILABLE

SCREENS LOCKED

ISN'T IT ROMANTIC
+$207
UNAVAILABLE

SCREENS LOCKED

WHAT MEN WANT
+$202
UNAVAILABLE

SCREENS LOCKED

THE UPSIDE
+$119
UNAVAILABLE

SCREENS LOCKED

COLD PURSUIT
+$111
UNAVAILABLE

SCREENS LOCKED

GLASS
+$63
UNAVAILABLE

SCREENS LOCKED

GREEN BOOK
+$56
UNAVAILABLE

SCREENS LOCKED

SPIDER-MAN: INTO THE SPIDER-VERSE
+$49
UNAVAILABLE

SCREENS LOCKED

AQUAMAN
+$47
UNAVAILABLE

SCREENS LOCKED

THE PRODIGY
+$44
UNAVAILABLE

SCREENS LOCKED

THEY SHALL NOT GROW OLD
+$29
UNAVAILABLE

SCREENS LOCKED

BOHEMIAN RHAPSODY
+$20
UNAVAILABLE

SCREENS LOCKED

MISS BALA
+$20"""

FML_RAW = """"The Lego Movie 2: The Second Part" - $27.8 million 
"Happy Death Day 2U" - $22 million
"Alita: Battle Angel" - $19.7 million 
"Isn't It Romantic" - $14.3 million
"What Men Want" - $13 million 
"The Upside" - $8 million
"Cold Pursuit" - $7.3 million
"Glass" - $4.4 million 
"Green Book" - $3.9 million 
"Spider-Man: Into the Spider-Verse" - $3.2 million 
"The Prodigy" - $3.1 million 
"Aquaman" - $2.8 million 
"They Shall Not Grow Old" - $1.9 million 
"Bohemian Rhapsody" - $1.3 million
"Miss Bala" - $1.2 million"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	The LEGO Movie 2: The Second Part
(Warner Bros.)	$27.0 M	$68.5 M	-21%	2
2	Alita: Battle Angel (Fox)	$22.5 M	$31.0 M	NEW	1
3	Happy Death Day 2U (Universal)	$17.5 M	$27.0 M	NEW	1
4	Isn't It Romantic (Warner / New Line)	$17.0 M	$26.5 M	NEW	1
5	What Men Want (Paramount)	$12.0 M	$36.3 M	-34%	2
6	Cold Pursuit (Lionsgate / Summit)	$7.7 M	$22.7 M	-30%	2
7	The Upside (STXfilms)	$7.5 M	$95.7 M	+6%	6
8	Glass (Universal)	$5.2 M	$105.8 M	-17%	5
9	Green Book (Universal / DreamWorks)	$3.6 M	$66.6 M	+5%	14
10	Spider-Man: Into the Spider-Verse
(Sony / Columbia)	$3.2 M	$184.1 M	+5%	10
11	Aquaman (Warner Bros.)	$3.0 M	$332.7 M	-6%	9
12	The Prodigy (Orion Films)	$2.9 M	$10.8 M	-50%	2"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(201828, PRICES_RAW, BOR_RAW, FML_RAW)

