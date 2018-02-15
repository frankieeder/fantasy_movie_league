import fml

# 2017, QUARTER 4, WEEK 8 #

PRICES_RAW = """JUMANJI: WELCOME TO THE JUNGLE
+FB$290
UNAVAILABLE

SCREENS LOCKED

12 STRONG
+FB$251
UNAVAILABLE

SCREENS LOCKED

THE POST
+FB$209
UNAVAILABLE

SCREENS LOCKED

THE GREATEST SHOWMAN
+FB$156
UNAVAILABLE

SCREENS LOCKED

PADDINGTON 2
+FB$110
UNAVAILABLE

SCREENS LOCKED

DEN OF THIEVES
+FB$94
UNAVAILABLE

SCREENS LOCKED

THE COMMUTER
+FB$90
UNAVAILABLE

SCREENS LOCKED

STAR WARS: THE LAST JEDI
+FB$85
UNAVAILABLE

SCREENS LOCKED

INSIDIOUS: THE LAST KEY
+FB$74
UNAVAILABLE

SCREENS LOCKED

PROUD MARY
+FB$65
UNAVAILABLE

SCREENS LOCKED

PHANTOM THREAD
+FB$52
UNAVAILABLE

SCREENS LOCKED

DARKEST HOUR
+FB$47
UNAVAILABLE

SCREENS LOCKED

PITCH PERFECT 3
+FB$45
UNAVAILABLE

SCREENS LOCKED

I, TONYA
+FB$40
UNAVAILABLE

SCREENS LOCKED

COCO
+FB$34"""

FML_RAW = """"Jumanji: Welcome to the Jungle" - $19.6 million

"12 Strong" - $17.9 million

"The Post" - $14 million

"The Greatest Showman" - $9.1 million

"The Commuter" - $8.2 million

"Paddington 2" - $8.1 million

"Star Wars: The Last Jedi" - $6.4 million

"Den of Thieves" - $6.1 million

"Insidious: The Last Key" - $4.8 million

"Proud Mary" - $4.5 million

"Darkest Hour" - $3.4 million

"Phantom Thread" - $3.4 million

"Pitch Perfect 3" - $3.2 million

"I, Tonya" - $2.6 million

"Coco" - $2.4 million"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Jumanji: Welcome to the Jungle
(Sony / Columbia)	$18.5 M	$315.2 M	-34%	5
2	12 Strong (Warner Bros.)	$13.3 M	$13.3 M	NEW	1
3	The Post (Fox / DreamWorks)	$12.3 M	$45.0 M	-36%	5
4	Den of Thieves (STXfilms)	$10.3 M	$10.3 M	NEW	1
5	The Greatest Showman (Fox)	$10.0 M	$112.2 M	-20%	5
6	Paddington 2 (Warner Bros.)	$7.5 M	$24.2 M	-32%	2
7	The Commuter (Lionsgate)	$6.5 M	$25.4 M	-53%	2
8	Star Wars: The Last Jedi (Disney)	$5.8 M	$603.4 M	-51%	6
9	Insidious: The Last Key (Universal)	$5.7 M	$58.4 M	-54%	3
10	Phantom Thread (Focus)	$4.7 M	$7.5 M	+309%	4
11	Proud Mary (Sony / Screen Gems)	$4.5 M	$17.8 M	-55%	2
12	I, Tonya (NEON / 30West)	$3.7 M	$15.3 M	+10%	7
13	Forever My Girl (Roadside)	$3.5 M	$3.5 M	NEW	1
14	Pitch Perfect 3 (Universal)	$3.2 M	$100.7 M	-47%	5
15	Darkest Hour (Focus)	$3.0 M	$41.0 M	-33%	9"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(8, PRICES_RAW, BOR_RAW, FML_RAW)

