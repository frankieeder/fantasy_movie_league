import fml
##########
# WEEK 2 #
##########

PRICES_RAW = """
STAR WARS: THE LAST JEDI
+FB$610
UNAVAILABLE

SCREENS LOCKED

JUMANJI: WELCOME TO THE JUNGLE
+FB$588
UNAVAILABLE

SCREENS LOCKED

PITCH PERFECT 3
+FB$242
UNAVAILABLE

SCREENS LOCKED

THE GREATEST SHOWMAN
+FB$143
UNAVAILABLE

SCREENS LOCKED

FERDINAND
+FB$131
UNAVAILABLE

SCREENS LOCKED

COCO
+FB$110
UNAVAILABLE

SCREENS LOCKED

DARKEST HOUR
+FB$93
UNAVAILABLE

SCREENS LOCKED

THE SHAPE OF WATER
+FB$73
UNAVAILABLE

SCREENS LOCKED

DOWNSIZING
+FB$64
UNAVAILABLE

SCREENS LOCKED

FATHER FIGURES
+FB$48
UNAVAILABLE

SCREENS LOCKED

ALL THE MONEY IN THE WORLD
+FB$40
UNAVAILABLE

SCREENS LOCKED

WONDER
+FB$32
UNAVAILABLE

SCREENS LOCKED

MOLLY'S GAME
+FB$21
UNAVAILABLE

SCREENS LOCKED

BEST OF THE REST
+FB$21
UNAVAILABLE

SCREENS LOCKED

LADY BIRD
+FB$20"""

FML_RAW = """""Star Wars: The Last Jedi" - $77.8 million

"Jumanji: Welcome to the Jungle" - $58 million

"Pitch Perfect 3" - $25.1 million

"The Greatest Showman" - $14.9 million

"Ferdinand" - $12.5 million

"Coco" - $9.8 million

"Darkest Hour" - $7.3 million

"Downsizing" - $6.1 million

"The Shape of Water" - $5.7 million

"All the Money in the World" - $5.2 million

"Father Figures" - $4.5 million

"Wonder" - $3.4 million

"Molly's Game" - $2.3 million

"Best of the Rest" - $1.9 million

"Lady Bird" - $1.8 million"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Star Wars: The Last Jedi (Disney)	$72.5 M	$537.0 M	-27%	3
2	Jumanji: Welcome to the Jungle
(Sony / Columbia)	$57.5 M	$171.5 M	+4%	2
3	Pitch Perfect 3 (Universal)	$22.5 M	$67.0 M	-15%	2
4	The Greatest Showman (Fox)	$16.0 M	$47.8 M	+11%	2
5	Ferdinand (Fox)	$13.5 M	$54.0 M	+33%	3
6	Coco (Disney)	$9.8 M	$181.7 M	+20%	6
7	Darkest Hour (Focus)	$6.9 M	$19.5 M	+25%	6
8	Downsizing (Paramount)	$6.6 M	$18.8 M	-14%	2
9	The Shape of Water (Fox Searchlight)	$5.1 M	$17.2 M	+15%	5
10	All the Money in the World (Sony / TriStar)	$5.0 M	$11.7 M	+92%	1
11	Father Figures (Warner Bros.)	$4.9 M	$13.8 M	-11%	2
12	Wonder (Lionsgate)	$3.0 M	$120.8 M	+11%	7"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(5, PRICES_RAW, BOR_RAW, FML_RAW)
