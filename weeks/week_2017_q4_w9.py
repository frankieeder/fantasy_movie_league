import fml

# 2017, QUARTER 4, WEEK 9 #

PRICES_RAW = """
MAZE RUNNER: THE DEATH CURE
+FB$358
UNAVAILABLE

SCREENS LOCKED

JUMANJI: WELCOME TO THE JUNGLE
+FB$222
UNAVAILABLE

SCREENS LOCKED

THE GREATEST SHOWMAN
+FB$134
UNAVAILABLE

SCREENS LOCKED

THE POST
+FB$129
UNAVAILABLE

SCREENS LOCKED

12 STRONG
+FB$128
UNAVAILABLE

SCREENS LOCKED

DEN OF THIEVES
+FB$127
UNAVAILABLE

SCREENS LOCKED

HOSTILES
+FB$126
UNAVAILABLE

SCREENS LOCKED

PADDINGTON 2
+FB$93
UNAVAILABLE

SCREENS LOCKED

THE SHAPE OF WATER
+FB$86
UNAVAILABLE

SCREENS LOCKED

PHANTOM THREAD
+FB$81
UNAVAILABLE

SCREENS LOCKED

THREE BILLBOARDS OUTSIDE EBBING, MISSOURI
+FB$68
UNAVAILABLE

SCREENS LOCKED

BEST OF THE REST
+FB$67
UNAVAILABLE

SCREENS LOCKED

FOREVER MY GIRL
+FB$64
UNAVAILABLE

SCREENS LOCKED

THE COMMUTER
+FB$58
UNAVAILABLE

SCREENS LOCKED

STAR WARS: THE LAST JEDI
+FB$57"""

FML_RAW = """"Maze Runner: The Death Cure" - $22.8 million

"Jumanji: Welcome to the Jungle" - $14.9 million

"12 Strong" - $8.9 million

"The Greatest Showman" - $8.5 million

"Den of Thieves" - $7.7 million

"The Post" - $7.6 million

"Paddington 2" - $5.8 million

"Hostiles" - $4.8 million

"Star Wars: The Last Jedi" - $4.1 million

"The Shape of Water" - $3.4 million

"Three Billboards Outside Ebbing, Missouri" - $3.3 million

"The Commuter" - $3.3 million

"Forever My Girl" - $3.2 million

"Phantom Thread" - $3 million

Best of the Rest - $3 million"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Maze Runner: The Death Cure (Fox)	$23.0 M	$23.0 M	NEW	1
2	Jumanji: Welcome to the Jungle
(Sony / Columbia)	$15.3 M	$337.0 M	-22%	6
3	Hostiles (Entertainment Studios)	$10.2 M	$12.1 M	+1,658%	6
4	The Post (Fox / DreamWorks)	$9.3 M	$58.9 M	-21%	6
5	The Greatest Showman (Fox)	$9.2 M	$126.3 M	-14%	6
6	12 Strong (Warner Bros.)	$8.7 M	$29.8 M	-45%	2
7	Den of Thieves (STXfilms)	$8.0 M	$28.0 M	-47%	2
8	Paddington 2 (Warner Bros.)	$5.5 M	$32.0 M	-31%	3
9	The Shape of Water (Fox Searchlight)	$4.8 M	$36.5 M	+120%	9
10	Star Wars: The Last Jedi (Disney)	$4.5 M	$611.0 M	-31%	7
11	Phantom Thread (Focus)	$3.7 M	$11.4 M	+14%	5
12	The Commuter (Lionsgate)	$3.5 M	$31.6 M	-47%	3
13	I, Tonya (NEON / 30West)	$3.4 M	$19.3 M	+19%	8
14	Three Billboards Outside
Ebbing, Missouri (Fox Searchlight)	$3.3 M	$36.7 M	+72%	12
15	Darkest Hour (Focus)	$3.2 M	$45.5 M	+17%	10
16	Forever My Girl (Roadside)	$3.1 M	$8.6 M	-27%	2
17	Insidious: The Last Key (Universal)	$3.0 M	$63.2 M	-49%	4"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(9, PRICES_RAW, BOR_RAW, FML_RAW)

