import fml

# 2017, QUARTER 4, WEEK 7 #

PRICES_RAW = """JUMANJI: WELCOME TO THE JUNGLE
+FB$293
UNAVAILABLE

SCREENS LOCKED

THE POST
+FB$210
UNAVAILABLE

SCREENS LOCKED

PADDINGTON 2
+FB$201
UNAVAILABLE

SCREENS LOCKED

INSIDIOUS: THE LAST KEY
+FB$170
UNAVAILABLE

SCREENS LOCKED

PROUD MARY
+FB$169
UNAVAILABLE

SCREENS LOCKED

THE COMMUTER
+FB$143
UNAVAILABLE

SCREENS LOCKED

STAR WARS: THE LAST JEDI
+FB$139
UNAVAILABLE

SCREENS LOCKED

THE GREATEST SHOWMAN
+FB$132
UNAVAILABLE

SCREENS LOCKED

PITCH PERFECT 3
+FB$70
UNAVAILABLE

SCREENS LOCKED

DARKEST HOUR
+FB$64
UNAVAILABLE

SCREENS LOCKED

MOLLY'S GAME
+FB$59
UNAVAILABLE

SCREENS LOCKED

FERDINAND
+FB$58
UNAVAILABLE

SCREENS LOCKED

COCO
+FB$44
UNAVAILABLE

SCREENS LOCKED

THE SHAPE OF WATER
+FB$41
UNAVAILABLE

SCREENS LOCKED

BEST OF THE REST
+FB$41"""

FML_RAW = """"Jumanji: Welcome to the Jungle" - $32.7 million

"Paddington 2" - $22.4 million

"The Post" - $22.3 million

"Proud Mary" - $18.5 million

"Star Wars: The Last Jedi" - $15.5 million

"The Commuter" - $14.6 million

"Insidious: The Last Key" - $13.2 million

"The Greatest Showman" - $12.6 million

"Pitch Perfect 3" - $7.3 million

"Ferdinand" - $6.5 million

"Darkest Hour" - $4.9 million

"Coco" - $4.8 million

"Molly's Game" - $4.8 million

"The Shape of Water" - $2.7 million

Best of the Rest - $2.4 million"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Jumanji: Welcome to the Jungle
(Sony / Columbia)	$37.0 M	$293.5 M	-1%	4
2	The Post (Fox / DreamWorks)	$26.5 M	$31.0 M	+1,461%	4
3	Proud Mary (Sony / Screen Gems)	$20.0 M	$20.0 M	NEW	1
4	Paddington 2 (Warner Bros.)	$19.5 M	$19.5 M	NEW	1
5	Star Wars: The Last Jedi (Disney)	$17.5 M	$597.5 M	-26%	5
6	The Commuter (Lionsgate)	$15.0 M	$15.0 M	NEW	1
7	The Greatest Showman (Fox)	$14.0 M	$96.8 M	+2%	4
8	Insidious: The Last Key (Universal)	$13.0 M	$49.2 M	-56%	2
9	Pitch Perfect 3 (Universal)	$6.8 M	$95.8 M	-34%	4
10	Ferdinand (Fox)	$6.7 M	$78.7 M	-13%	5
11	Darkest Hour (Focus)	$6.5 M	$37.7 M	+7%	8
12	Molly's Game (STXfilms)	$6.0 M	$23.0 M	-12%	3
13	Coco (Disney)	$5.3 M	$198.8 M	-2%	8
14	I, Tonya (NEON / 30West)	$3.7 M	$10.3 M	+51%	6
15	The Shape of Water (Fox Searchlight)	$3.3 M	$27.0 M	+5%	7"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(7, PRICES_RAW, BOR_RAW, FML_RAW)

