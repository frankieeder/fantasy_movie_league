import fml

# 1/11/2019 - 1/13/2019 #

PRICES_RAW = """AQUAMAN
+$269
UNAVAILABLE

SCREENS LOCKED

A DOG'S WAY HOME
+$207
UNAVAILABLE

SCREENS LOCKED

THE UPSIDE
+$188
UNAVAILABLE

SCREENS LOCKED

ESCAPE ROOM
+$137
UNAVAILABLE

SCREENS LOCKED

ON THE BASIS OF SEX
+$135
UNAVAILABLE

SCREENS LOCKED

MARY POPPINS RETURNS
+$132
UNAVAILABLE

SCREENS LOCKED

SPIDER-MAN: INTO THE SPIDER-VERSE
+$127
UNAVAILABLE

SCREENS LOCKED

BUMBLEBEE
+$114
UNAVAILABLE

SCREENS LOCKED

THE MULE
+$95
UNAVAILABLE

SCREENS LOCKED

VICE
+$60
UNAVAILABLE

SCREENS LOCKED

REPLICAS
+$58
UNAVAILABLE

SCREENS LOCKED

BOHEMIAN RHAPSODY
+$56
UNAVAILABLE

SCREENS LOCKED

IF BEALE STREET COULD TALK
+$55
UNAVAILABLE

SCREENS LOCKED

SECOND ACT
+$41
UNAVAILABLE

SCREENS LOCKED

RALPH BREAKS THE INTERNET
+$39"""

FML_RAW = """"Aquaman" - $17.7 million 
"A Dog's Way Home" - $12.8 million 
"The Upside" - $11.6 million 
"Escape Room" - $9.4 million 
"Mary Poppins Returns" - $8.8 million 
"Spider-Man: Into the Spider-Verse" - $8.7 million 
"On the Basis of Sex" - $7.9 million 
"Bumblebee" - $7.6 million 
"The Mule" - $5.8 million 
"Vice" - $3.9 million 
"If Beale Street Could Talk" - $3.6 million 
"Bohemian Rhapsody" - $3.5 million 
"Replicas" - $3.4 million 
"Second Act" - $2.6 million 
"Ralph Breaks the Internet" - $2.5 million"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Aquaman (Warner Bros.)	$20.0 M	$291.2 M	-35%	4
2	The Upside (STXfilms)	$16.0 M	$16.0 M	NEW	1
3	A Dog's Way Home (Sony / Columbia)	$13.3 M	$13.3 M	NEW	1
4	Spider-Man: Into the Spider-Verse
(Sony / Columbia)	$9.7 M	$148.7 M	-26%	5
5	Mary Poppins Returns (Disney)	$9.5 M	$153.2 M	-40%	4
6	Escape Room (Sony / Columbia)	$9.2 M	$32.8 M	-50%	2
7	Bumblebee (Paramount)	$8.2 M	$110.2 M	-38%	4
8	On the Basis of Sex (Focus)	$7.8 M	$12.1 M	+385%	3
9	The Mule (Warner Bros.)	$6.2 M	$91.0 M	-32%	5
10	Vice (Annapurna Pictures)	$4.4 M	$36.9 M	-23%	3
11	Replicas (Entertainment Studios)	$4.3 M	$4.3 M	NEW	1
12	Bohemian Rhapsody (Fox)	$3.4 M	$198.7 M	+44%	11
13	If Beale Street Could Talk (Annapurna Pictures)	$3.0 M	$8.3 M	+63%	5"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(2019111, PRICES_RAW, BOR_RAW, FML_RAW)

