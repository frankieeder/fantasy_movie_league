from fml import *
###############
# WEEK 8 TEST #
###############

WEEK_8_PRICES_RAW = """
Boo 2!
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

WEEK_8_ACTUAL_FML_RAW = """"Boo 2!" - $21.226953 million

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
WEEK_8_PRICES = Prices(8, WEEK_8_PRICES_RAW)
#print(WEEK_8_PRICES)
WEEK_8_ACTUAL_FML_PROJECTIONS = FML_Projections(8, WEEK_8_ACTUAL_FML_RAW)
#print(WEEK_8_ACTUAL_FML_PROJECTIONS)
WEEK_8_BRACKET = best_bracket(WEEK_8_PRICES, WEEK_8_ACTUAL_FML_PROJECTIONS)
#print(WEEK_8_BRACKET)
