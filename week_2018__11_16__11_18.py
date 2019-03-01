import fml

# 11/16/2018 - 11/18/2018 #

PRICES_RAW = """FANTASTIC BEASTS: THE CRIMES OF GRINDELWALD
+FB$699
UNAVAILABLE

SCREENS LOCKED

THE GRINCH
+FB$387
UNAVAILABLE

SCREENS LOCKED

BOHEMIAN RHAPSODY
+FB$203
UNAVAILABLE

SCREENS LOCKED

INSTANT FAMILY
+FB$180
UNAVAILABLE

SCREENS LOCKED

WIDOWS
+FB$167
UNAVAILABLE

SCREENS LOCKED

A STAR IS BORN
+FB$55
UNAVAILABLE

SCREENS LOCKED

THE NUTCRACKER AND THE FOUR REALMS
+FB$54
UNAVAILABLE

SCREENS LOCKED

OVERLORD
+FB$49
UNAVAILABLE

SCREENS LOCKED

NOBODY'S FOOL
+FB$36
UNAVAILABLE

SCREENS LOCKED

THE GIRL IN THE SPIDER'S WEB
+FB$36
UNAVAILABLE

SCREENS LOCKED

VENOM
+FB$27
UNAVAILABLE

SCREENS LOCKED

BOY ERASED
+FB$19
UNAVAILABLE

SCREENS LOCKED

HALLOWEEN
+FB$14
UNAVAILABLE

SCREENS LOCKED

THE HATE U GIVE
+FB$12
UNAVAILABLE

SCREENS LOCKED

CAN YOU EVER FORGIVE ME?
+FB$12"""

FML_RAW = """"Fantastic Beasts: The Crimes of Grindelwald" - $72.1 million


"The Grinch" - $38.8 million


"Bohemian Rhapsody" - $19.7 million


"Instant Family" - $19.4 million


"Widows" - $15.8 million


"A Star Is Born" - $5.7 million


"The Nutcracker and the Four Realms" - $4.9 million


"Overlord" - $4.9 million


"The Girl in the Spider's Web" - $3.5 million


"Nobody's Fool" - $3 million


"Venom" - $2.7 million


"Boy Erased" - $2 million


"Halloween" - $1.4 million


"The Hate U Give" - $1.2 million


"Can You Ever Forgive Me?" - $988,000"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Fantastic Beasts:
The Crimes of Grindelwald
(Warner Bros.)	$68.5 M	$68.5 M	NEW	1
2	Dr. Seuss' The Grinch (Universal)	$38.5 M	$127.7 M	-43%	2
3	Instant Family (Paramount)	$19.0 M	$19.0 M	NEW	1
4	Bohemian Rhapsody (Fox)	$18.7 M	$131.2 M	-40%	3
5	Widows (Fox)	$17.0 M	$17.0 M	NEW	1
6	A Star is Born (Warner Bros.)	$5.4 M	$187.0 M	-33%	7
7	Overlord (Paramount)	$4.8 M	$18.8 M	-53%	2
8	The Nutcracker and the Four Realms
(Disney)	$4.7 M	$44.1 M	-53%	3
9	The Girl in the Spider's Web
(Sony / Columbia / MGM)	$3.6 M	$14.5 M	-54%	2
10	Nobody's Fool (Paramount)	$3.4 M	$30.2 M	-49%	3
11	Venom (Sony / Columbia)	$2.4 M	$210.6 M	-51%	7
12	Boy Erased (Focus)	$1.9 M	$3.2 M	+151%	3
13	A Private War (Aviron Pictures)	$1.6 M	$2.0 M	+714%	3"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(20181116, PRICES_RAW, BOR_RAW, FML_RAW)

