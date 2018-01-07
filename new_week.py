year = input("Year? ")
quarter = input("Quarter? ")
week = input("Week? ")

prices = []
print("Prices? (terminate with a new line containing 'end')")
while True:
    line = input()
    if line == 'end':
        break
    prices.append(line)
prices = '\n'.join(prices)

fml_projections = []
print("FML Projections? (terminate with a new line containing 'end')")
while True:
    line = input()
    if line == 'end':
        break
    fml_projections.append(line)
fml_projections = '\n'.join(fml_projections)

bor_projections = []
print("BOR Projections? (terminate with a new line containing 'end')")
while True:
    line = input()
    if line == 'end':
        break
    bor_projections.append(line)
bor_projections = '\n'.join(bor_projections)

file_name = "week_{0}_q{1}_w{2}.py".format(year, quarter, week)

contents = \
"""from fml import *

# {4}, QUARTER {5}, WEEK {0} #

WEEK_{0}_PRICES_RAW = \"\"\"{1}\"\"\"

WEEK_{0}_FML_RAW = \"\"\"{2}\"\"\"

WEEK_{0}_BOR_RAW = \"\"\"{3}\"\"\"


WEEK_{0}_PRICES, \\
WEEK_{0}_FML_PROJECTIONS, \\
WEEK_{0}_FML_BRACKET, \\
WEEK_{0}_BOR_PROJECTIONS, \\
WEEK_{0}_BOR_BRACKET = exec_raw({0}, WEEK_{0}_PRICES_RAW, WEEK_{0}_BOR_RAW, WEEK_{0}_FML_RAW)
""".format(week, prices, fml_projections, bor_projections, year, quarter)

lines = contents.split("\n")

new = open(file_name, "w+")

for line in lines:
    new.write(line)
    new.write("\n")

#remove name file extension
file_name = file_name[:-3]

all_weeks = open("all_weeks.py", "a")
all_weeks.write("from " + file_name + " import *\n")
