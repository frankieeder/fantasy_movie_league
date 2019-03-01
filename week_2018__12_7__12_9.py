import fml

# 12/7/2018 - 12/9/2018 #

PRICES_RAW = """RALPH BREAKS THE INTERNET
+$326
UNAVAILABLE

SCREENS LOCKED

THE GRINCH
+$265
UNAVAILABLE

SCREENS LOCKED

CREED II
+$212
UNAVAILABLE

SCREENS LOCKED

FANTASTIC BEASTS: THE CRIMES OF GRINDELWALD
+$126
UNAVAILABLE

SCREENS LOCKED

BOHEMIAN RHAPSODY
+$119
UNAVAILABLE

SCREENS LOCKED

INSTANT FAMILY
+$103
UNAVAILABLE

SCREENS LOCKED

GREEN BOOK
+$64
UNAVAILABLE

SCREENS LOCKED

THE POSSESSION OF HANNAH GRACE
+$63
UNAVAILABLE

SCREENS LOCKED

ROBIN HOOD
+$62
UNAVAILABLE

SCREENS LOCKED

WIDOWS
+$57
UNAVAILABLE

SCREENS LOCKED

THE FAVOURITE
+$47
UNAVAILABLE

SCREENS LOCKED

SCHINDLER'S LIST
+$36
UNAVAILABLE

SCREENS LOCKED

A STAR IS BORN
+$30
UNAVAILABLE

SCREENS LOCKED

THE NUTCRACKER AND THE FOUR REALMS
+$17
UNAVAILABLE

SCREENS LOCKED

VOX LUX
+$8"""

FML_RAW = """"Ralph Breaks the Internet" - $16.7 million 
"The Grinch" - $12.8 million
"Creed II" - $10.1 million
"Fantastic Beasts: The Crimes of Grindelwald" - $6.2 million
"Bohemian Rhapsody" - $5.8 million 
"Instant Family" - $5.1 million 
"Green Book" - $3.2 million 
"The Possession of Hannah Grace" - $2.9 million
"Robin Hood" - $2.6 million
"Widows" - $2.5 million 
"The Favourite" - $2.3 million 
"Schindler's List" - $1.5 million
"A Star Is Born" - $1.4 million
"The Nutcracker and the Four Realms" - $759,000
"Vox Lux" - $353,000"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Ralph Breaks the Internet (Disney)	$16.2 M	$141.2 M	-37%	3
2	Dr. Seuss' The Grinch (Universal)	$15.0 M	$223.3 M	-16%	5
3	Creed II (MGM)	$10.5 M	$96.5 M	-37%	3
4	Fantastic Beasts:
The Crimes of Grindelwald
(Warner Bros.)	$6.3 M	$144.7 M	-45%	4
5	Bohemian Rhapsody (Fox)	$6.0 M	$173.5 M	-25%	6
6	Instant Family (Paramount)	$5.5 M	$54.0 M	-23%	4
7	Green Book (Universal / DreamWorks)	$3.7 M	$19.8 M	-6%	4
8	Robin Hood (Lionsgate / Summit)	$3.0 M	$26.7 M	-37%	3
9	Widows (Fox)	$2.9 M	$37.9 M	-34%	4
10	The Possession of Hannah Grace
(Sony / Screen Gems)	$2.8 M	$11.1 M	-56%	2
11	A Star is Born (Warner Bros.)	$2.6 M	$197.1 M	+42%	10"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(2018127, PRICES_RAW, BOR_RAW, FML_RAW)

