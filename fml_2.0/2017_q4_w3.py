from fml import *
##########
# WEEK 2 #
##########

WEEK_3_PRICES_RAW = """
FRI - STAR WARS: THE LAST JEDI - FRI ONLY
+FB$823
UNAVAILABLE

SCREENS LOCKED

SAT - STAR WARS: THE LAST JEDI - SAT ONLY
+FB$501
UNAVAILABLE

SCREENS LOCKED

SUN - STAR WARS: THE LAST JEDI - SUN ONLY
+FB$422
UNAVAILABLE

SCREENS LOCKED

FERDINAND
+FB$157
UNAVAILABLE

SCREENS LOCKED

COCO
+FB$90
UNAVAILABLE

SCREENS LOCKED

THE DISASTER ARTIST
+FB$45
UNAVAILABLE

SCREENS LOCKED

WONDER
+FB$40
UNAVAILABLE

SCREENS LOCKED

JUSTICE LEAGUE
+FB$35
UNAVAILABLE

SCREENS LOCKED

THOR: RAGNAROK
+FB$25
UNAVAILABLE

SCREENS LOCKED

DADDY'S HOME 2
+FB$25
UNAVAILABLE

SCREENS LOCKED

MURDER ON THE ORIENT EXPRESS
+FB$21
UNAVAILABLE

SCREENS LOCKED

LADY BIRD
+FB$19
UNAVAILABLE

SCREENS LOCKED

THE SHAPE OF WATER
+FB$18
UNAVAILABLE

SCREENS LOCKED

THE STAR
+FB$17
UNAVAILABLE

SCREENS LOCKED

THREE BILLBOARDS OUTSIDE EBBING, MISSOURI
+FB$14
UNAVAILABLE

SCREENS LOCKED"""

WEEK_3_FML_RAW = """"Star Wars: The Last Jedi" (Friday) - $103.2 million

"Star Wars: The Last Jedi" (Saturday) - $63.8 million

"Star Wars: The Last Jedi" (Sunday) - $52.7 million

"Ferdinand" - $18.6 million

"Coco" - $11.2 million

"Wonder" - $4.9 million

"The Disaster Artist" - $4.9 million

"Justice League" - $4.4 million

"Daddy's Home 2" - $3.15 million

"Thor: Ragnarok" - $3.1 million

"Murder on the Orient Express" - $2.6 million

"The Shape of Water" - $2.3 million

"Lady Bird" - $2.3 million

"The Star" - $2.1 million

"Three Billboards Outside Ebbing, Missouri" - $1.7 million"""

WEEK_3_BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Star Wars: The Last Jedi (Disney)	$207.0 M	$207.0 M	NEW	1
2	Ferdinand (Fox)	$18.5 M	$18.5 M	NEW	1
3	Coco (Disney)	$10.3 M	$151.2 M	-44%	4
4	Wonder (Lionsgate)	$5.2 M	$109.0 M	-38%	5
5	Justice League (Warner Bros.)	$4.3 M	$219.6 M	-56%	5
6	The Disaster Artist (A24 / New Line)	$3.7 M	$14.1 M	-42%	3
7	Daddy's Home 2 (Paramount)	$3.3 M	$96.1 M	-44%	6
8	Thor: Ragnarok (Disney)	$2.9 M	$306.3 M	-54%	7
9	Murder on the Orient Express (Fox)	$2.5 M	$97.3 M	-52%	6
10	The Shape of Water (Fox Searchlight)	$2.2 M	$4.1 M	+93%	3
11	Lady Bird (A24)	$2.1 M	$26.1 M	-39%	7
12	The Star (Sony / AFFIRM)	$2.0 M	$35.6 M	-46%	5"""


WEEK_3_PRICES, \
WEEK_3_FML_PROJECTIONS, \
WEEK_3_FML_BRACKET, \
WEEK_3_BOR_PROJECTIONS, \
WEEK_3_BOR_BRACKET = exec_raw(3, WEEK_3_PRICES_RAW, WEEK_3_BOR_RAW, WEEK_3_FML_RAW)
