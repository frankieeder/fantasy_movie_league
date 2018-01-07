import fml
##########
# WEEK 2 #
##########

PRICES_RAW = """
Coco
FB$390
UNAVAILABLESCREENS LOCKED
Justice League
FB$177
UNAVAILABLESCREENS LOCKED
Wonder
FB$169
UNAVAILABLESCREENS LOCKED
Just Getting Started
FB$152
UNAVAILABLESCREENS LOCKED
The Disaster Artist
FB$150
UNAVAILABLESCREENS LOCKED
Thor: Ragnarok
FB$126
UNAVAILABLESCREENS LOCKED
Daddy's Home 2
FB$95
UNAVAILABLESCREENS LOCKED
Murder on the Orient Express
FB$88
UNAVAILABLESCREENS LOCKED
Lady Bird
FB$73
UNAVAILABLESCREENS LOCKED
Three Billboards Outside Ebbing, Missouri
FB$68
UNAVAILABLESCREENS LOCKED
The Star
FB$58
UNAVAILABLESCREENS LOCKED
A Bad Moms Christmas
FB$47
UNAVAILABLESCREENS LOCKED
The Shape of Water
FB$34
UNAVAILABLESCREENS LOCKED
Roman J. Israel, Esq.
FB$20
UNAVAILABLESCREENS LOCKED
Darkest Hour
FB$13"""

FML_RAW = """"Coco" - $18.3 million
"Justice League" - $8.2 million
"Wonder" - $7.6 million
"Thor: Ragnarok" - $6.5 million
"Just Getting Started" - $5.2 million
"Daddy's Home 2" - $4.4 million
"The Disaster Artist" - $4.2 million
"Murder on the Orient Express" - $3.9 million
"Lady Bird" - $3.6 million
"Three Billboards Outside Ebbing, Missouri" - $3.4 million
"The Star" - $2.9 million
"A Bad Moms Christmas" - $2.4 million
"The Shape of Water" - $1.3 million
"Roman J. Israel, Esq." - $956,000
"Darkest Hour" - $667,000"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Coco (Disney)	$19.5 M	$136.7 M	-29%	3
2	Justice League (Warner Bros.)	$9.8 M	$212.2 M	-41%	4
3	Wonder (Lionsgate)	$8.3 M	$100.0 M	-32%	4
4	The Disaster Artist (A24 / New Line)	$8.0 M	$9.6 M	+560%	2
5	Thor: Ragnarok (Disney)	$7.5 M	$302.6 M	-24%	6
6	Daddy's Home 2 (Paramount)	$5.2 M	$90.2 M	-31%	5
7	Just Getting Started (Broad Green Pictures)	$5.0 M	$5.0 M	NEW	1
8	Murder on the Orient Express (Fox)	$4.3 M	$91.8 M	-36%	5
9	Lady Bird (A24)	$4.0 M	$22.8 M	-7%	6
10	Three Billboards Outside
Ebbing, Missouri (Fox Searchlight)	$3.8 M	$19.4 M	-14%	5
11	The Star (Sony / AFFIRM)	$3.4 M	$31.9 M	-17%	4
12	A Bad Moms Christmas (STXfilms)	$2.6 M	$68.7 M	-23%	6"""

PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(2, PRICES_RAW, BOR_RAW, FML_RAW)
