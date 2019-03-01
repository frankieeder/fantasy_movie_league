import fml

# 11/9/2018 - 11/11/2018 #

PRICES_RAW = """THE GRINCH
+FB$800
UNAVAILABLE

SCREENS LOCKED

BOHEMIAN RHAPSODY
+FB$372
UNAVAILABLE

SCREENS LOCKED

THE GIRL IN THE SPIDER'S WEB
+FB$150
UNAVAILABLE

SCREENS LOCKED

THE NUTCRACKER AND THE FOUR REALMS
+FB$126
UNAVAILABLE

SCREENS LOCKED

OVERLORD
+FB$107
UNAVAILABLE

SCREENS LOCKED

A STAR IS BORN
+FB$100
UNAVAILABLE

SCREENS LOCKED

NOBODY'S FOOL
+FB$80
UNAVAILABLE

SCREENS LOCKED

VENOM
+FB$65
UNAVAILABLE

SCREENS LOCKED

HALLOWEEN
+FB$59
UNAVAILABLE

SCREENS LOCKED

THUGS OF HINDOSTAN
+FB$40
UNAVAILABLE

SCREENS LOCKED

SMALLFOOT
+FB$26
UNAVAILABLE

SCREENS LOCKED

THE HATE U GIVE
+FB$25
UNAVAILABLE

SCREENS LOCKED

HUNTER KILLER
+FB$25
UNAVAILABLE

SCREENS LOCKED

GOOSEBUMPS 2: HAUNTED HALLOWEEN
+FB$22
UNAVAILABLE

SCREENS LOCKED

CAN YOU EVER FORGIVE ME?
+FB$21"""

FML_RAW = """"The Grinch" - $56.4 million


"Bohemian Rhapsody" - $29.5 million


"The Girl in the Spider's Web" - $11.4 million


"The Nutcracker and the Four Realms" - $10.2 million


"Overlord" - $8.4 million


"A Star Is Born" - $8 million


"Nobody's Fool" - $6.5 million


"Venom" - $5.5 million


"Halloween" - $4.7 million


"Thugs of Hindostan" - $3.2 million


"Smallfoot" - $2.5 million


"The Hate U Give" - $1.8 million


"Hunter Killer" - $1.8 million


"Goosebumps 2: Haunted Halloween" - $1.7 million


"Can You Ever Forgive Me?" - $1.6 million"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Dr. Seuss' The Grinch (Universal)	$63.0 M	$63.0 M	NEW	1
2	Bohemian Rhapsody (Fox)	$27.0 M	$97.2 M	-47%	2
3	The Nutcracker and the Four Realms
(Disney)	$11.2 M	$36.8 M	-45%	2
4	The Girl in the Spider's Web
(Sony / Columbia)	$10.7 M	$10.7 M	NEW	1
5	Overlord (Paramount)	$10.2 M	$10.2 M	NEW	1
6	A Star is Born (Warner Bros.)	$8.5 M	$178.7 M	-23%	6
7	Nobody's Fool (Paramount)	$6.9 M	$24.6 M	-50%	2
8	Venom (Sony / Columbia)	$5.9 M	$207.5 M	-25%	6
9	Halloween (Universal)	$4.9 M	$158.2 M	-55%	4
10	Thugs of Hindostan (Yash Raj Films)	$2.5 M	$2.5 M	NEW	1
11	The Hate U Give (Fox)	$2.1 M	$26.7 M	-37%	6"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(2018119, PRICES_RAW, BOR_RAW, FML_RAW)

