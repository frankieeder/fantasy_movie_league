import fml

# 11/23/2018 - 11/25/2018 #

PRICES_RAW = """RALPH BREAKS THE INTERNET
+$566
UNAVAILABLE

SCREENS LOCKED

CREED II
+$363
UNAVAILABLE

SCREENS LOCKED

FANTASTIC BEASTS: THE CRIMES OF GRINDELWALD
+$362
UNAVAILABLE

SCREENS LOCKED

THE GRINCH
+$307
UNAVAILABLE

SCREENS LOCKED

BOHEMIAN RHAPSODY
+$146
UNAVAILABLE

SCREENS LOCKED

INSTANT FAMILY
+$127
UNAVAILABLE

SCREENS LOCKED

WIDOWS
+$94
UNAVAILABLE

SCREENS LOCKED

ROBIN HOOD
+$94
UNAVAILABLE

SCREENS LOCKED

GREEN BOOK
+$68
UNAVAILABLE

SCREENS LOCKED

A STAR IS BORN
+$39
UNAVAILABLE

SCREENS LOCKED

THE NUTCRACKER AND THE FOUR REALMS
+$36
UNAVAILABLE

SCREENS LOCKED

OVERLORD
+$22
UNAVAILABLE

SCREENS LOCKED

BOY ERASED
+$15
UNAVAILABLE

SCREENS LOCKED

THE FRONT RUNNER
+$12
UNAVAILABLE

SCREENS LOCKED

NOBODY'S FOOL
+$11"""

FML_RAW = """"Ralph Breaks the Internet" - $54.4 million


"Fantastic Beasts: The Crimes of Grindelwald" - $34.8 million


"The Grinch" - $30.1 million


"Creed II" - $28.4 million


"Bohemian Rhapsody" - $14.1 million


"Instant Family" - $12.7 million


"Robin Hood" - $9.7 million


"Widows" - $9.5 million


"Green Book" - $6.6 million


"A Star Is Born" - $4 million


"The Nutcracker and the Four Realms" - $3.8 million


"Overlord" - $2 million


"Boy Erased" - $1.5 million


"Nobody's Fool" - $1.1 million


"The Front Runner" - $712,000"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Ralph Breaks the Internet (Disney)	$51.0 M	$73.5 M	NEW	1
2	Creed II (MGM)	$37.0 M	$53.5 M	NEW	1
3	Dr. Seuss' The Grinch (Universal)	$28.5 M	$177.5 M	-26%	3
4	Fantastic Beasts:
The Crimes of Grindelwald
(Warner Bros.)	$28.0 M	$114.8 M	-55%	2
5	Bohemian Rhapsody (Fox)	$13.0 M	$151.3 M	-19%	4
6	Instant Family (Paramount)	$11.8 M	$34.8 M	-19%	2
7	Robin Hood (Lionsgate / Summit)	$8.5 M	$12.8 M	NEW	1
8	Widows (Fox)	$8.3 M	$26.5 M	-33%	2
9	Green Book (Universal / DreamWorks)	$4.0 M	$5.8 M	+1,148%	2
10	A Star is Born (Warner Bros.)	$3.0 M	$191.1 M	-30%	8
11	The Nutcracker and the Four Realms
(Disney)	$2.9 M	$49.3 M	-39%	4"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(20181123, PRICES_RAW, BOR_RAW, FML_RAW)

