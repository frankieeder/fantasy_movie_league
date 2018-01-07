from fml import *
###########
# WEEK 12 #
###########

WEEK_12_PRICES_RAW = """
FRI: Justice League - FRI ONLY
FB$636
UNAVAILABLESCREENS LOCKED
SAT: Justice League - SAT ONLY
FB$434
UNAVAILABLESCREENS LOCKED
SUN: Justice League - SUN ONLY
FB$334
UNAVAILABLESCREENS LOCKED
Thor: Ragnarok
FB$269
UNAVAILABLESCREENS LOCKED
Daddy's Home 2
FB$175
UNAVAILABLESCREENS LOCKED
Murder on the Orient Express
FB$152
UNAVAILABLESCREENS LOCKED
Wonder
FB$140
UNAVAILABLESCREENS LOCKED
The Star
FB$120
UNAVAILABLESCREENS LOCKED
A Bad Moms Christmas
FB$77
UNAVAILABLESCREENS LOCKED
Lady Bird
FB$30
UNAVAILABLESCREENS LOCKED
Jigsaw
FB$16
UNAVAILABLESCREENS LOCKED
Boo 2! A Madea Halloween
FB$9
UNAVAILABLESCREENS LOCKED
Blade Runner 2049
FB$8
UNAVAILABLESCREENS LOCKED
Geostorm
FB$8
UNAVAILABLESCREENS LOCKED
Three Billboards Outside Ebbing, Missouri
+
FB$8"""

WEEK_12_FML_RAW = """"Justice League" (Friday) - $58.1 million

"Justice League" (Saturday) - $41.1 million

"Justice League" (Sunday) - $29.2 million

"Thor: Ragnarok" - $25 million

"Daddy's Home 2" - $15.9 million

"Murder on the Orient Express" - $14.5 million

"Wonder" - $12.9 million

"The Star" - $10.3 million

"A Bad Moms Christmas" - $7 million

"Lady Bird" - $2.9 million

"Jigsaw" - $1.45 million

"Boo 2! A Madea Halloween" - $844,000

"Blade Runner 2049" - $763,000

"Three Billboards Outside Ebbing, Missouri" - $755,000

"Geostorm" - $721,000"""

WEEK_12_BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Justice League (Warner Bros.)	$118.0 M	$118.0 M	NEW	1
2	Thor: Ragnarok (Disney)	$23.0 M	$248.5 M	-60%	3
3	Wonder (Lionsgate)	$17.0 M	$17.0 M	NEW	1
4	Daddy's Home 2 (Paramount)	$14.2 M	$50.0 M	-52%	2
5	Murder on the Orient Express (Fox)	$14.0 M	$51.8 M	-51%	2
6	The Star (Sony / AFFIRM)	$8.0 M	$8.0 M	NEW	1
7	A Bad Moms Christmas (STXfilms)	$6.8 M	$50.6 M	-41%	3
8	Lady Bird (A24)	$3.2 M	$5.4 M	+167%	3
9	Three Billboards Outside
Ebbing, Missouri (Fox Searchlight)	$1.3 M	$1.7 M	+304%	2
10	Jigsaw (Lionsgate)	$1.2 M	$36.6 M	-65%	4"""
WEEK_12_PRICES, \
WEEK_12_FML_PROJECTIONS, \
WEEK_12_FML_BRACKET, \
WEEK_12_BOR_PROJECTIONS, \
WEEK_12_BOR_BRACKET = exec_raw(12, WEEK_12_PRICES_RAW, WEEK_12_BOR_RAW, WEEK_12_FML_RAW)
