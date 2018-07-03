import fml
##########
# WEEK 2 #
##########

PRICES_RAW = """
JUMANJI: WELCOME TO THE JUNGLE
+FB$369
UNAVAILABLE

SCREENS LOCKED

STAR WARS: THE LAST JEDI
+FB$336
UNAVAILABLE

SCREENS LOCKED

INSIDIOUS: THE LAST KEY
+FB$262
UNAVAILABLE

SCREENS LOCKED

THE GREATEST SHOWMAN
+FB$143
UNAVAILABLE

SCREENS LOCKED

PITCH PERFECT 3
+FB$126
UNAVAILABLE

SCREENS LOCKED

MOLLY'S GAME
+FB$100
UNAVAILABLE

SCREENS LOCKED

FERDINAND
+FB$81
UNAVAILABLE

SCREENS LOCKED

I, TONYA
+FB$56
UNAVAILABLE

SCREENS LOCKED

DARKEST HOUR
+FB$52
UNAVAILABLE

SCREENS LOCKED

COCO
+FB$50
UNAVAILABLE

SCREENS LOCKED

ALL THE MONEY IN THE WORLD
+FB$48
UNAVAILABLE

SCREENS LOCKED

THE SHAPE OF WATER
+FB$32
UNAVAILABLE

SCREENS LOCKED

DOWNSIZING
+FB$30
UNAVAILABLE

SCREENS LOCKED

FATHER FIGURES
+FB$28
UNAVAILABLE

SCREENS LOCKED

WONDER
+FB$24"""

FML_RAW = """""Jumanji: Welcome to the Jungle" - $29.1 million

"Star Wars: The Last Jedi" - $24.8 million

"Insidious: The Last Key" - $18.6 million

"The Greatest Showman" - $10.6 million

"Pitch Perfect 3" - $8 million

"Ferdinand" - $6.9 million

"Molly's Game" - $4.7 million

"Coco" - $4.5 million

"Darkest Hour" - $3.5 million

"All the Money in the World" - $3.2 million

"I, Tonya" - $2.9 million

"Downsizing" - $2.7 million

"The Shape of Water" - $2.4 million

"Father Figures" - $2.3 million

"Wonder" - $2 million"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Jumanji: Welcome to the Jungle
(Sony / Columbia)	$31.0 M	$239.0 M	-38%	3
2	Star Wars: The Last Jedi (Disney)	$23.0 M	$572.3 M	-56%	4
3	Insidious: The Last Key (Universal)	$20.0 M	$20.0 M	NEW	1
4	The Greatest Showman (Fox)	$11.7 M	$74.7 M	-25%	3
5	Pitch Perfect 3 (Universal)	$8.7 M	$84.7 M	-48%	3
6	Molly's Game (STXfilms)	$7.0 M	$14.2 M	+198%	2
7	Ferdinand (Fox)	$6.7 M	$69.3 M	-41%	4
8	Darkest Hour (Focus)	$5.2 M	$27.2 M	-5%	7
9	Coco (Disney)	$4.5 M	$190.8 M	-40%	7
10	All the Money in the World (Sony / TriStar)	$3.4 M	$20.0 M	-39%	2
11	The Shape of Water (Fox Searchlight)	$2.7 M	$21.2 M	-24%	6
12	Wonder (Lionsgate)	$2.4 M	$126.7 M	-26%	8
13	Downsizing (Paramount)	$2.2 M	$23.0 M	-53%	3"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(6, PRICES_RAW, BOR_RAW, FML_RAW)
