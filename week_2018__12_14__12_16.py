import fml

# 12/14/2018 - 12/16/2018 #

PRICES_RAW = """SPIDER-MAN: INTO THE SPIDER-VERSE
+$571
UNAVAILABLE

SCREENS LOCKED

THE MULE
+$235
UNAVAILABLE

SCREENS LOCKED

MORTAL ENGINES
+$171
UNAVAILABLE

SCREENS LOCKED

THE GRINCH
+$155
UNAVAILABLE

SCREENS LOCKED

RALPH BREAKS THE INTERNET
+$127
UNAVAILABLE

SCREENS LOCKED

ONCE UPON A DEADPOOL
+$76
UNAVAILABLE

SCREENS LOCKED

CREED II
+$68
UNAVAILABLE

SCREENS LOCKED

BOHEMIAN RHAPSODY
+$55
UNAVAILABLE

SCREENS LOCKED

THE FAVOURITE
+$52
UNAVAILABLE

SCREENS LOCKED

INSTANT FAMILY
+$51
UNAVAILABLE

SCREENS LOCKED

FANTASTIC BEASTS: THE CRIMES OF GRINDELWALD
+$48
UNAVAILABLE

SCREENS LOCKED

GREEN BOOK
+$41
UNAVAILABLE

SCREENS LOCKED

ROBIN HOOD
+$23
UNAVAILABLE

SCREENS LOCKED

WIDOWS
+$21
UNAVAILABLE

SCREENS LOCKED

A STAR IS BORN
+$19"""

FML_RAW = """"Spider-Man: Into the Spider-Verse" - $48.4 million 
"The Mule" - $17.6 million 
"Mortal Engines" - $13.4 million 
"The Grinch" - $10.5 million 
"Ralph Breaks the Internet" - $9.7 million 
"Creed II" - $5.4 million 
"Once Upon a Deadpool" - $4.2 million 
"Bohemian Rhapsody" - $3.9 million 
"Instant Family" - $3.8 million 
"The Favourite" - $3.7 million 
"Green Book" - $3.4 million 
"Fantastic Beasts: The Crimes of Grindelwald" - $3.3 million 
"Robin Hood" - $1.8 million 
"Widows" - $1.7 million 
"A Star Is Born" - $1.3 million"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	Spider-Man: Into the Spider-Verse
(Sony / Columbia)	$39.0 M	$39.0 M	NEW	1
2	The Mule (Warner Bros.)	$20.0 M	$20.0 M	NEW	1
3	Dr. Seuss' The Grinch (Universal)	$11.5 M	$239.3 M	-24%	6
4	Mortal Engines (Universal)	$11.0 M	$11.0 M	NEW	1
5	Ralph Breaks the Internet (Disney)	$9.5 M	$154.5 M	-42%	4
6	Creed II (MGM)	$5.2 M	$104.8 M	-48%	4
7	Once Upon a Deadpool (Fox)	$4.5 M	$6.5 M	NEW	1
8	Bohemian Rhapsody (Fox)	$4.0 M	$180.3 M	-35%	7
9	Instant Family (Paramount)	$3.8 M	$60.3 M	-34%	5
10	Fantastic Beasts:
The Crimes of Grindelwald
(Warner Bros.)	$3.7 M	$151.8 M	-47%	5
11	Green Book (Universal / DreamWorks)	$3.3 M	$25.4 M	-15%	5
12	The Favourite (Fox Searchlight)	$3.1 M	$7.3 M	+106%	6"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(20181214, PRICES_RAW, BOR_RAW, FML_RAW)

