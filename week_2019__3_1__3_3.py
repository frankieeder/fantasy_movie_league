import fml

# 3/1/2019 - 3/3/2019 #

PRICES_RAW = """HOW TO TRAIN YOUR DRAGON: THE HIDDEN WORLD
+$501
UNAVAILABLE

SCREENS LOCKED

TYLER PERRY'S A MADEA FAMILY FUNERAL
+$363
UNAVAILABLE

SCREENS LOCKED

GRETA
+$126
UNAVAILABLE

SCREENS LOCKED

ALITA: BATTLE ANGEL
+$111
UNAVAILABLE

SCREENS LOCKED

THE LEGO MOVIE 2: THE SECOND PART
+$87
UNAVAILABLE

SCREENS LOCKED

FIGHTING WITH MY FAMILY
+$70
UNAVAILABLE

SCREENS LOCKED

ISN'T IT ROMANTIC
+$67
UNAVAILABLE

SCREENS LOCKED

HAPPY DEATH DAY 2U
+$45
UNAVAILABLE

SCREENS LOCKED

GREEN BOOK
+$44
UNAVAILABLE

SCREENS LOCKED

WHAT MEN WANT
+$41
UNAVAILABLE

SCREENS LOCKED

THE UPSIDE
+$32
UNAVAILABLE

SCREENS LOCKED

COLD PURSUIT
+$28
UNAVAILABLE

SCREENS LOCKED

RUN THE RACE
+$20
UNAVAILABLE

SCREENS LOCKED

GLASS
+$15
UNAVAILABLE

SCREENS LOCKED

SPIDER-MAN: INTO THE SPIDER-VERSE
+$11"""

FML_RAW = """"How to Train Your Dragon: The Hidden World" - $32.2 million 
"Tyler Perry's A Madea Family Funeral" - $22.8 million 
"Alita: Battle Angel" - $6.3 million 
"Greta" - $5.6 million 
"The Lego Movie 2: The Second Part" - $5.3 million 
"Fighting with My Family" - $4.1 million 
"Isn't It Romantic" - $3.9 million 
"Green Book" - $2.7 million 
"What Men Want" - $2.5 million 
"Happy Death Day 2U" - $2.3 million 
"The Upside" - $1.8 million 
"Cold Pursuit" - $1.6 million
"Run the Race" - $1 million 
"Glass" - $842,000
"Spider-Man: Into the Spider-Verse" - $643,000"""

BOR_RAW = """1	How to Train Your Dragon: The Hidden World
(Universal / DreamWorks Animation)	$30.0 M	$98.0 M	-45%	2
2	Tyler Perry's A Madea Family Funeral
(Lionsgate)	$22.0 M	$22.0 M	NEW	1
3	Alita: Battle Angel (Fox)	$7.0 M	$72.2 M	-43%	3
4	The LEGO Movie 2: The Second Part
(Warner Bros.)	$6.2 M	$91.2 M	-36%	4
5	Fighting With My Family (MGM)	$4.5 M	$14.7 M	-42%	3
6	Greta (Focus)	$4.4 M	$4.4 M	NEW	1
7	Isn't It Romantic (Warner / New Line)	$4.3 M	$39.9 M	-40%	3
8	Green Book (Universal / DreamWorks)	$3.8 M	$75.1 M	+79%	16
9	Happy Death Day 2U (Universal)	$2.8 M	$25.5 M	-43%	3
10	What Men Want (Paramount)	$2.6 M	$49.5 M	-50%	4
11	Spider-Man: Into the Spider-Verse
(Sony / Columbia)	$2.0 M	$187.3 M	+126%	12
12	The Upside (STXfilms)	$1.9 M	$102.7 M	-40%	8"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(201931, PRICES_RAW, BOR_RAW, FML_RAW)

