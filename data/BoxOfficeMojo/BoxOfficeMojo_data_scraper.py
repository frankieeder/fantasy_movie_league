from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import re
import os

data_start_url = "http://www.boxofficemojo.com/weekend/chart/?yr=1982&wknd=01&p=.htm"
start_url = data_start_url # "http://www.boxofficemojo.com/weekend/chart/?yr=2016&wknd=01&p=.htm"
# Make output folder
os.chdir(os.path.dirname(os.path.realpath(__file__)))
if not os.path.exists('output/'):
    os.makedirs('output/')
generated_csvs = (f for f in os.listdir('./output/') if f[-4:] == ".csv")
seen_weekends = {tuple(f.split(" | ")[:2]) for f in generated_csvs}
driver = webdriver.Chrome()
driver.get(start_url)
try:
    while True:
        # Get Metadata
        this_url = driver.current_url
        yr_id = re.search("yr=[^&]*", this_url)[0]
        week_id = re.search("wknd=[^&]*", this_url)[0]
        forwards = driver.find_element_by_link_text('Next Weekend>>') # Will raise error when we have reached the most recent results
        if (yr_id, week_id) not in seen_weekends:
            # Set up page source parser
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            tables = soup.find_all('table')
            chart_header = tables[2]
            chart = soup.find(border="0", cellspacing="1", cellpadding="5")
            dates = soup.find(face="Verdana", color="#800000", size="5").get_text()

            # Parse Table
            rowelems = chart.find_all('tr')
            rows = [rowelem.find_all('td') for rowelem in rowelems]
            data = [[elem.get_text() for elem in row] for row in rows][:-1]
            data[0][6:7] = ["Theater Count", "Theater Change"] # fix weird formatting edge case

            # Write Data
            csvfile = "./output/" + " | ".join((yr_id, week_id, dates)) + ".csv"
            with open(csvfile, "w") as output:
                writer = csv.writer(output, lineterminator='\n')
                writer.writerows(data)
        # Go To Next Page
        forwards.click()
except Exception as e:
    raise e
    pass
driver.close()
