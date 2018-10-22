import fml

# 8/10/2018 - 8/12/2018 #

PRICES_RAW = """THE MEG
+FB$334
UNAVAILABLE

SCREENS LOCKED

MISSION: IMPOSSIBLE: FALLOUT
+FB$260
UNAVAILABLE

SCREENS LOCKED

CHRISTOPHER ROBIN
+FB$177
UNAVAILABLE

SCREENS LOCKED

SLENDER MAN
+FB$171
UNAVAILABLE

SCREENS LOCKED

BLACKKKLANSMAN
+FB$84
UNAVAILABLE

SCREENS LOCKED

THE SPY WHO DUMPED ME
+FB$83
UNAVAILABLE

SCREENS LOCKED

DOG DAYS
+FB$69
UNAVAILABLE

SCREENS LOCKED

MAMMA MIA! HERE WE GO AGAIN
+FB$65
UNAVAILABLE

SCREENS LOCKED

THE EQUALIZER 2
+FB$63
UNAVAILABLE

SCREENS LOCKED

HOTEL TRANSYLVANIA 3: SUMMER VACATION
+FB$62
UNAVAILABLE

SCREENS LOCKED

ANT-MAN AND THE WASP
+FB$52
UNAVAILABLE

SCREENS LOCKED

INCREDIBLES 2
+FB$41
UNAVAILABLE

SCREENS LOCKED

THE DARKEST MINDS
+FB$38
UNAVAILABLE

SCREENS LOCKED

TEEN TITANS GO! TO THE MOVIES
+FB$31
UNAVAILABLE

SCREENS LOCKED

JURASSIC WORLD: FALLEN KINGDOM
+FB$29"""

FML_RAW = """"Mission: Impossible: Fallout" - $21.3 million


"The Meg" - $19.7 million


"Christopher Robin" - $13.8 million


"Slender Man" - $9.1 million


"The Spy Who Dumped Me" - $6.6 million


"Mamma Mia! Here We Go Again" - $5.8 million


"BlacKkKlansman" - $5.6 million


"The Equalizer 2" - $5.4 million


"Hotel Transylvania 3: Summer Vacation" - $5.3 million


"Dog Days" - $5.1 million


"Ant-Man and the Wasp" - $4.2 million


"Incredibles 2" - $3.3 million


"Teen Titans Go! to The Movies" - $2.5 million


"The Darkest Minds" - $2.4 million


"Jurassic World: Fallen Kingdom" - $2.3 million"""

BOR_RAW = """Film (Distributor)	Weekend
Gross	Total
Gross	%
Change	Week
#
1	The Meg (Warner Bros.)	$26.5 M	$26.5 M	NEW	1
2	Mission: Impossible - Fallout (Paramount)	$22.0 M	$164.3 M	-38%	3
3	Disney's Christopher Robin (Disney)	$13.7 M	$51.8 M	-44%	2
4	BlacKkKlansman (Focus)	$13.0 M	$13.0 M	NEW	1
5	Slender Man (Sony / Screen Gems)	$9.8 M	$9.8 M	NEW	1
6	The Spy Who Dumped Me (Lionsgate)	$6.5 M	$24.3 M	-46%	2
7	Dog Days (LD Entertainment)	$5.8 M	$7.8 M	NEW	1
8	Mamma Mia! Here We Go Again (Universal)	$5.4 M	$103.3 M	-40%	4
9	The Equalizer 2 (Sony / Columbia)	$5.3 M	$89.5 M	-39%	4
10	Hotel Transylvania 3: Summer Vacation
(Sony / Columbia)	$5.2 M	$147.3 M	-35%	5
11	Ant-Man and The Wasp (Disney)	$4.3 M	$203.8 M	-32%	6
12	Incredibles 2 (Disney)	$3.1 M	$589.5 M	-38%	9
13	The Darkest Minds (Fox)	$2.4 M	$11.3 M	-59%	2"""


PRICES, \
FML_PROJECTIONS, \
FML_BRACKET, \
BOR_PROJECTIONS, \
BOR_BRACKET = fml.exec_raw(2018810, PRICES_RAW, BOR_RAW, FML_RAW)
