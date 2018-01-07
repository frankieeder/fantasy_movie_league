from fml import *
##########
# WEEK 2 #
##########

WEEK_4_PRICES_RAW = """
STAR WARS: THE LAST JEDI
+FB$815
UNAVAILABLE

SCREENS LOCKED

JUMANJI: WELCOME TO THE JUNGLE
+FB$275
UNAVAILABLE

SCREENS LOCKED

PITCH PERFECT 3
+FB$251
UNAVAILABLE

SCREENS LOCKED

THE GREATEST SHOWMAN
+FB$110
UNAVAILABLE

SCREENS LOCKED

DOWNSIZING
+FB$72
UNAVAILABLE

SCREENS LOCKED

FERDINAND
+FB$67
UNAVAILABLE

SCREENS LOCKED

FATHER FIGURES
+FB$54
UNAVAILABLE

SCREENS LOCKED

COCO
+FB$51
UNAVAILABLE

SCREENS LOCKED

ALL THE MONEY IN THE WORLD
+FB$31
UNAVAILABLE

SCREENS LOCKED

WONDER
+FB$28
UNAVAILABLE

SCREENS LOCKED

THE SHAPE OF WATER
+FB$23
UNAVAILABLE

SCREENS LOCKED

DADDY'S HOME 2
+FB$20
UNAVAILABLE

SCREENS LOCKED

JUSTICE LEAGUE
+FB$17
UNAVAILABLE

SCREENS LOCKED

DARKEST HOUR
+FB$16
UNAVAILABLE

SCREENS LOCKED

BEST OF THE REST
+FB$15"""

WEEK_4_FML_RAW = """""Star Wars: The Last Jedi" - $134 million

"Jumanji: Welcome to the Jungle" - $46.9 million

"Pitch Perfect 3" - $40.6 million

"The Greatest Showman" - $16.1 million

"Ferdinand" - $12.4 million

"Downsizing" - $12.3 million

"Coco" - $8.8 million

"Father Figures" - $8.6 million

"Wonder" - $4.7 million

"Daddy's Home 2" - $3.8 million

"All the Money in the World" - $3.2 million

"The Shape of Water" - $3.1 million

"Darkest Hour" - $2.3 million

"Justice League" - $2.2 million

Best of the Rest - $1.9 million

"""

WEEK_4_BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Star Wars: The Last Jedi (Disney)	$128.0 M	$432.5 M	-42%	2
2	Jumanji: Welcome to the Jungle
(Sony / Columbia)	$40.0 M	$56.0 M	NEW	1
3	Pitch Perfect 3 (Universal)	$33.0 M	$33.0 M	NEW	1
4	The Greatest Showman (Fox)	$17.0 M	$23.5 M	NEW	1
5	Ferdinand (Fox)	$11.0 M	$30.0 M	-18%	2
6	Downsizing (Paramount)	$10.5 M	$10.5 M	NEW	1
7	Coco (Disney)	$9.7 M	$166.0 M	-3%	5
8	Father Figures (Warner Bros.)	$9.0 M	$9.0 M	NEW	1
9	Wonder (Lionsgate)	$4.3 M	$117.3 M	-18%	6
10	The Shape of Water (Fox Searchlight)	$4.2 M	$8.9 M	+145%	4
11	All the Money in the World (Sony / TriStar)	$4.0 M	$4.0 M	NEW	0
12	Darkest Hour (Focus)	$3.3 M	$6.2 M	+289%	5
13	Daddy's Home 2 (Paramount)	$3.2 M	$101.8 M	-16%	7
14	Justice League (Warner Bros.)	$2.8 M	$224.6 M	-35%	6"""


WEEK_4_PRICES, \
WEEK_4_FML_PROJECTIONS, \
WEEK_4_FML_BRACKET, \
WEEK_4_BOR_PROJECTIONS, \
WEEK_4_BOR_BRACKET = exec_raw(4, WEEK_4_PRICES_RAW, WEEK_4_BOR_RAW, WEEK_4_FML_RAW)
