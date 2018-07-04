from bs4 import BeautifulSoup
import urllib.request
import csv
import re
import os

def getYears():
    """Finds years that have weekend chart results.

    :return: an integer list of years that have weekend chart results.
    """
    url = "http://www.boxofficemojo.com/weekend/"
    src = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(src, 'html.parser')
    year_header = soup.find_all(name = "b")[1]
    year_elems = year_header.find_all(["a", "font"])
    years = [int(year.get_text()) for year in year_elems]
    return years

def getWeeks(year):
    """Finds weeks in this year that have weekend chart results.

    :param year: year to find week numbers of weekend chart results.
    :return: an integer list of weeks in this year that have weekend chart results.
    """
    url = "http://www.boxofficemojo.com/weekend/?yr=%d" % year
    src = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(src, 'html.parser')
    chart = soup.find(border="0", cellspacing="1", cellpadding="5")
    data = parseTable(chart)
    weeks = [int(row[-1]) for row in data[1:]]
    return weeks

def getAllWeekends():
    """Gets all weekends that have weekend chart results.

    :return: a list of (year, week) tuples that have weekend chart results.
    """
    all_weekends = set()
    for year in getYears():
        for week in getWeeks(year):
            all_weekends.add((year, week))
    return all_weekends

def parseTable(chart):
    """Parses an HTML table element into a python matrix of strings

    :param chart: A bs4 element that is a table
    :return: A matrix of strings to represent a table, indexed by row then column.
    """
    rowelems = chart.find_all('tr')
    rows = [rowelem.find_all('td') for rowelem in rowelems]
    data = [[elem.get_text() for elem in row] for row in rows]
    return(data)

def writeTable(table, filename):
    """Writes table to csv.
    :param table: The table to write (should be indexed by rows then columns)
    :param filename: The directory to write the csv to
    :return: None
    """
    with open(filename, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(table)

def findYear(str):
    """Uses regex to find the integer year ID in a string, with form yr=<digit>

    :param str: string to search
    :return: integer representation of year ID.
    """
    return int(re.search("(?<=yr=)\d*", str)[0])

def findWeekend(str):
    """Uses regex to find the integer weekend ID in a string, with form wknd=<digit>

    :param str: string to search
    :return: integer representation of weekend ID.
    """
    return int(re.search("(?<=wknd=)\d*", str)[0])

# Make output folder
os.chdir(os.path.dirname(os.path.realpath(__file__)))
if not os.path.exists('output/'):
    os.makedirs('output/')

# Figure out what is left to scrape
generated_csvs = [f for f in os.listdir('./output/') if f[-4:] == ".csv"]
seen_weekends = {(findYear(f), findWeekend(f)) for f in generated_csvs}
all_weekends = getAllWeekends()
weekends_to_collect = all_weekends - seen_weekends

for year, week in weekends_to_collect:
    # Get Metadata
    yr_id = "yr=%d" % year
    wknd_id = "wknd=%d" % week

    # Set up page source parser
    url = "http://www.boxofficemojo.com/weekend/chart/?%s&%s" % (yr_id, wknd_id)
    src = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(src, 'html.parser')
    tables = soup.find_all('table')
    chart_header = tables[2]
    chart = soup.find(border="0", cellspacing="1", cellpadding="5")
    dates = soup.find(face="Verdana", color="#800000", size="5").get_text()

    # Parse, trim and format table
    data = parseTable(chart)[:-1]
    data[0][6:7] = ["Theater Count", "Theater Change"]  # fix weird formatting edge case

    # Write data to csv
    csvfile = "./output/" + " | ".join((yr_id, wknd_id, dates)) + ".csv"
    writeTable(data, csvfile)

