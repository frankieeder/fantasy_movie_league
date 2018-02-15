"""To add and run a new week sidecar file, run new_week.py and input the necessary strings. These include:
 * Year: A string representing the year that this quarter began
 * Quarter: A string representing the quarter that this week is from
 * Week: A string representing the week to calculate projections for
 * Prices: The string created by highlighting and copying the entire price interface of Fantasy Movie League
 * FML Projections: The string created by highlighting and copying all the name-price pairs listed on FML Insider
 * BOR Projections: The string created by highlighting and copying the entire table of predictions posted on Box Office Report
This will also add the new week you make to all_weeks.py for later use.
"""

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
"""import fml

# {0}, QUARTER {1}, WEEK {2} #

PRICES_RAW = \"\"\"{3}\"\"\"

FML_RAW = \"\"\"{4}\"\"\"

BOR_RAW = \"\"\"{5}\"\"\"


PRICES, \\
FML_PROJECTIONS, \\
FML_BRACKET, \\
BOR_PROJECTIONS, \\
BOR_BRACKET = fml.exec_raw({2}, PRICES_RAW, BOR_RAW, FML_RAW)
""".format(year, quarter, week, prices, fml_projections, bor_projections)

lines = contents.split("\n")

new = open(file_name, "w+")

for line in lines:
    new.write(line)
    new.write("\n")

#remove name file extension
file_name = file_name[:-3]
import_line = "import " + file_name

with open('all_weeks.py', 'r') as content_file:
    content = content_file.read()

if import_line not in content:
    all_weeks = open("all_weeks.py", "a")
    all_weeks.write(import_line + "\n")

exec(import_line)
