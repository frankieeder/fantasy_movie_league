import fml

# 11/30/2018 - 12/2/2018 #

PRICES_RAW = """RALPH BREAKS THE INTERNET
+$460
UNAVAILABLE

SCREENS LOCKED

THE GRINCH
+$334
UNAVAILABLE

SCREENS LOCKED

CREED II
+$304
UNAVAILABLE

SCREENS LOCKED

FANTASTIC BEASTS: THE CRIMES OF GRINDELWALD
+$205
UNAVAILABLE

SCREENS LOCKED

BOHEMIAN RHAPSODY
+$144
UNAVAILABLE

SCREENS LOCKED

INSTANT FAMILY
+$134
UNAVAILABLE

SCREENS LOCKED

ROBIN HOOD
+$73
UNAVAILABLE

SCREENS LOCKED

WIDOWS
+$67
UNAVAILABLE

SCREENS LOCKED

GREEN BOOK
+$64
UNAVAILABLE

SCREENS LOCKED

THE POSSESSION OF HANNAH GRACE
+$57
UNAVAILABLE

SCREENS LOCKED

A STAR IS BORN
+$32
UNAVAILABLE

SCREENS LOCKED

THE NUTCRACKER AND THE FOUR REALMS
+$27
UNAVAILABLE

SCREENS LOCKED

THE FAVOURITE
+$18
UNAVAILABLE

SCREENS LOCKED

BOY ERASED
+$14
UNAVAILABLE

SCREENS LOCKED

NOBODY'S FOOL
+$8"""

FML_RAW = """"Ralph Breaks the Internet" - $28.7 million


"The Grinch" - $20 million


"Creed II" - $18.2 million


"Fantastic Beasts: The Crimes of Grindelwald" - $12.1 million


"Instant Family" - $7.9 million


"Bohemian Rhapsody" - $7.8 million


"Widows" - $4.1 million


"Green Book" - $4 million


"Robin Hood" - $3.9 million


"The Possession of Hannah Grace" - $3.2 million


"A Star Is Born" - $1.8 million


"The Nutcracker and the Four Realms" - $1.7 million


"The Favourite" - $1.1 million


"Boy Erased" - $878,000


"Nobody's Fool" - $428,000"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Ralph Breaks the Internet (Disney)	$27.5 M	$121.7 M	-51%	2
2	Dr. Seuss' The Grinch (Universal)	$18.0 M	$204.0 M	-41%	4
3	Creed II (MGM)	$17.0 M	$81.3 M	-52%	2
4	Fantastic Beasts:
The Crimes of Grindelwald
(Warner Bros.)	$11.5 M	$134.7 M	-61%	3
5	Bohemian Rhapsody (Fox)	$8.3 M	$164.6 M	-41%	5
6	Instant Family (Paramount)	$7.8 M	$46.7 M	-37%	3
7	The Possession of Hannah Grace
(Sony / Screen Gems)	$5.6 M	$5.6 M	NEW	1
8	Widows (Fox)	$4.8 M	$33.5 M	-42%	3
9	Robin Hood (Lionsgate / Summit)	$4.5 M	$21.5 M	-51%	2
10	Green Book (Universal / DreamWorks)	$4.2 M	$14.4 M	-24%	3"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(20181130, PRICES_RAW, BOR_RAW, FML_RAW)

