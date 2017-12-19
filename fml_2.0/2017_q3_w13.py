from fml import *
###########
# WEEK 13 #
###########

WEEK_13_PRICES_RAW = """
Coco
+
FB$716
UNAVAILABLESCREENS LOCKED
Justice League
FB$534
UNAVAILABLESCREENS LOCKED
Wonder
FB$298
UNAVAILABLESCREENS LOCKED
Thor: Ragnarok
FB$206
UNAVAILABLESCREENS LOCKED
Daddy's Home 2
FB$143
UNAVAILABLESCREENS LOCKED
Murder on the Orient Express
FB$128
UNAVAILABLESCREENS LOCKED
Roman J. Israel, Esq.
FB$102
UNAVAILABLESCREENS LOCKED
The Star
FB$96
UNAVAILABLESCREENS LOCKED
A Bad Moms Christmas
FB$70
UNAVAILABLESCREENS LOCKED
The Man Who Invented Christmas
FB$68
UNAVAILABLESCREENS LOCKED
Three Billboards Outside Ebbing, Missouri
FB$51
UNAVAILABLESCREENS LOCKED
Lady Bird
FB$49
UNAVAILABLESCREENS LOCKED
Jigsaw
FB$7
UNAVAILABLESCREENS LOCKED
Blade Runner 2049
FB$6
UNAVAILABLESCREENS LOCKED
Loving Vincent
FB$6"""

WEEK_13_FML_RAW = """"Coco" - $54.1 million

"Justice League" - $41.6 million

"Wonder" - $25.4 million

"Thor: Ragnarok" - $16.2 million

"Daddy's Home 2" - $11.9 million

"Murder on the Orient Express" - $10.8 million

"The Star" - $8.6 million

"A Bad Moms Christmas" - $5.9 million

"Roman J. Israel, Esq." - $5 million

"Lady Bird" - $4.5 million

"Three Billboards Outside Ebbing, Missouri" - $4.1 million

"The Man Who Invented Christmas" - $3.4 million

"Jigsaw" - $513,000

"Blade Runner 2049" - $446,000

"Loving Vincent" - $415,000

"""

WEEK_13_BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Coco (Disney)	$46.5 M	$66.0 M	NEW	1
2	Justice League (Warner Bros.)	$45.0 M	$178.0 M	-52%	2
3	Wonder (Lionsgate)	$27.5 M	$77.0 M	-0%	2
4	Thor: Ragnarok (Disney)	$17.5 M	$277.7 M	-19%	4
5	Daddy's Home 2 (Paramount)	$12.7 M	$71.5 M	-12%	3
6	Murder on the Orient Express (Fox)	$11.7 M	$72.2 M	-15%	3
7	The Star (Sony / AFFIRM)	$7.5 M	$23.2 M	-24%	2
8	A Bad Moms Christmas (STXfilms)	$6.0 M	$61.6 M	-14%	4
9	Roman J. Israel, Esq. (Sony / Columbia)	$4.3 M	$6.0 M	+6,836%	2
10	Lady Bird (A24)	$4.2 M	$11.0 M	+67%	4
11	Three Billboards Outside
Ebbing, Missouri (Fox Searchlight)	$3.9 M	$6.8 M	+254%	3
12	The Man Who Invented Christmas
(Bleecker Street)	$1.9 M	$2.5 M	NEW	1"""

WEEK_13_PRICES, \
WEEK_13_FML_PROJECTIONS, \
WEEK_13_FML_BRACKET, \
WEEK_13_BOR_PROJECTIONS, \
WEEK_13_BOR_BRACKET = exec_raw(13, WEEK_13_PRICES_RAW, WEEK_13_BOR_RAW, WEEK_13_FML_RAW)
