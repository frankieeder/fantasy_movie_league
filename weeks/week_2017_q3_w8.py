import fml
###############
# WEEK 8 TEST #
###############

PRICES_RAW = """
Boo 2! A Madea Halloween
FB$411
UNAVAILABLESCREENS LOCKED
Happy Death Day
FB$202
UNAVAILABLESCREENS LOCKED
Only the Brave
FB$201
UNAVAILABLESCREENS LOCKED
Geostorm
FB$186
UNAVAILABLESCREENS LOCKED
The Snowman
FB$167
UNAVAILABLESCREENS LOCKED
Blade Runner 2049
FB$128
UNAVAILABLESCREENS LOCKED
The Foreigner
FB$105
UNAVAILABLESCREENS LOCKED
It
FB$57
UNAVAILABLESCREENS LOCKED
The Mountain Between Us
FB$49
UNAVAILABLESCREENS LOCKED
American Made
FB$50
UNAVAILABLESCREENS LOCKED
Kingsman: The Golden Circle
FB$47
UNAVAILABLESCREENS LOCKED
Same Kind of Different as Me
FB$53
UNAVAILABLESCREENS LOCKED
The Lego Ninjago Movie
FB$42
UNAVAILABLESCREENS LOCKED
My Little Pony: The Movie
FB$35
UNAVAILABLESCREENS LOCKED
Victoria and Abdul
+
FB$31"""

ACTUAL_FML_RAW = """"Boo 2! A Madea Halloween" - $21.226953 million

"Happy Death Day" - $9.363415 million

"Only the Brave" - $6.002665 million

"Geostorm" - $13.707376 million

"The Snowman" - $3.372565 million

"Blade Runner 2049" - $7.353151 million

"The Foreigner" - $5.787447 million

"It" - $3.451663 million

"The Mountain Between Us" - $2.773757 million

"American Made" - $3.131650 million

"Kingsman: The Golden Circle" - $3.011307 million

"Same Kind of Different as Me" - $2.591985 million

"The Lego Ninjago Movie" - $2.226261 million

"My Little Pony: The Movie" - $2.027064 million

"Victoria and Abdul" - $2.126115 million"""

FML_RAW = """"Boo 2! A Madea Halloween" - $23.8 million

"Happy Death Day" - $13.9 million

"Only the Brave" - $12.3 million

"Geostorm" - $11.6 million

"The Snowman" - $10.8 million

"Blade Runner 2049" - $7.85 million

"The Foreigner" - $6.4 million

"It" - $3.8 million

"The Mountain Between Us" - $2.95 million

"American Made" - $2.9 million

"Kingsman: The Golden Circle" - $2.7 million

"Same Kind of Different as Me" - $2.6 million

"The Lego Ninjago Movie" - $2.5 million

"My Little Pony: The Movie" - $2 million

"Victoria and Abdul" - $1.8 million"""

PRICES = fml.Prices(8, PRICES_RAW)
print(PRICES)
ACTUAL_FML_EARNINGS = fml.FML_Projections(8, ACTUAL_FML_RAW)
print(ACTUAL_FML_EARNINGS)
REAL_BRACKET = fml.best_bracket(PRICES, ACTUAL_FML_EARNINGS)
print(REAL_BRACKET)
FML_PROJECTIONS = fml.FML_Projections(8, FML_RAW)
FML_BRACKET = fml.best_bracket(PRICES, FML_PROJECTIONS)
