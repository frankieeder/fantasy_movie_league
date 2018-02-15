import fml
###########
# WEEK 13 #
###########

PRICES_RAW = """
Coco
+
FB$417
UNAVAILABLESCREENS LOCKED
Justice League
FB$280
UNAVAILABLESCREENS LOCKED
Wonder
FB$230
UNAVAILABLESCREENS LOCKED
Thor: Ragnarok
FB$134
UNAVAILABLESCREENS LOCKED
Murder on the Orient Express
FB$132
UNAVAILABLESCREENS LOCKED
Daddy's Home 2
FB$126
UNAVAILABLESCREENS LOCKED
Three Billboards Outside Ebbing, Missouri
FB$74
UNAVAILABLESCREENS LOCKED
Lady Bird
FB$66
UNAVAILABLESCREENS LOCKED
The Star
FB$60
UNAVAILABLESCREENS LOCKED
A Bad Moms Christmas
FB$44
UNAVAILABLESCREENS LOCKED
Roman J. Israel, Esq.
FB$36
UNAVAILABLESCREENS LOCKED
The Man Who Invented Christmas
FB$14
UNAVAILABLESCREENS LOCKED
The Disaster Artist
FB$13
UNAVAILABLESCREENS LOCKED
Call Me by Your Name
FB$8
UNAVAILABLESCREENS LOCKED
Wonder Wheel
FB$6"""

FML_RAW = """"Coco" - $25.2 million

"Justice League" - $16.8 million

"Wonder" - $14.4 million

"Thor: Ragnarok" - $7.8 million

"Daddy's Home 2" - $7.1 million

"Murder on the Orient Express" - $6.9 million

"Three Billboards Outside Ebbing, Missouri" - $4.2 million

"Lady Bird" - $3.2 million

"The Star" - $3 million

"A Bad Moms Christmas" - $2.5 million

"Roman J. Israel, Esq." - $2 million

"The Man Who Invented Christmas" - $596,000

"The Disaster Artist" - $369,000

"Call Me by Your Name" - $309,000

"Wonder Wheel" - $256,000

"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Coco (Disney)	$28.5 M	$111.0 M	-44%	2
2	Justice League (Warner Bros.)	$15.7 M	$196.3 M	-62%	3
3	Wonder (Lionsgate)	$12.8 M	$88.2 M	-44%	3
4	Thor: Ragnarok (Disney)	$8.0 M	$289.2 M	-53%	5
5	Murder on the Orient Express (Fox)	$7.6 M	$85.6 M	-42%	4
6	Daddy's Home 2 (Paramount)	$7.0 M	$82.3 M	-47%	4
7	Three Billboards Outside
Ebbing, Missouri (Fox Searchlight)	$5.0 M	$14.1 M	+14%	4
8	The Star (Sony / AFFIRM)	$3.8 M	$27.0 M	-45%	3
9	Lady Bird (A24)	$3.7 M	$16.5 M	-9%	5
10	A Bad Moms Christmas (STXfilms)	$2.7 M	$64.0 M	-45%	5
11	Roman J. Israel, Esq. (Sony / Columbia)	$2.4 M	$10.0 M	-46%	3"""

PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(1, PRICES_RAW, BOR_RAW, FML_RAW)
