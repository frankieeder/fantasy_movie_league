from selenium import webdriver
import beautifulsoup4
import csv
import re
import os

data_start_url = "http://www.boxofficemojo.com/weekend/chart/?yr=1982&wknd=01&p=.htm"
start_url = "http://www.boxofficemojo.com/weekend/chart/?yr=2018&wknd=01&p=.htm"
generated_csvs = (f for f in os.listdir('.') if f[-4:] == ".csv")
seen_weekends = {tuple(f.split(" | ")[:2]) for f in generated_csvs}
driver = webdriver.Chrome()
driver.get(start_url)
try:
    while True:
        pg_src = driver.page_source
        # Get Metadata
        dates = driver.find_element_by_xpath('//*[@id="body"]/table[2]/tbody/tr/td[1]/font[1]/b').text
        this_url = driver.current_url
        yr_id = re.search("yr=[0-9]*(?=&)", this_url)[0]
        week_id = re.search("wknd=[0-9]*(?=&)", this_url)[0]


        # Find Table and Nav
        table_and_nav = driver.find_element_by_xpath('//*[@id="body"]/table[3]')
        backwards = table_and_nav.find_element_by_link_text('<<Last Weekend')
        forwards = table_and_nav.find_element_by_link_text('Next Weekend>>')
        if (yr_id, week_id) in seen_weekends:
            forwards.click()
            continue

        # Parse Table
        chart = table_and_nav.find_elements_by_tag_name('tr')[1]
        chart_text = chart.text
        rowelems = chart.find_elements_by_tag_name('tr')
        rows = [rowelem.find_elements_by_tag_name('td') for rowelem in rowelems]
        data = [[elem.text for elem in row] for row in rows][:-1] # TODO: Find out why getting text is so slow??

        # Write Data
        csvfile = " | ".join((yr_id, week_id, dates)) + ".csv"
        with open(csvfile, "w") as output:
            writer = csv.writer(output, lineterminator='\n')
            writer.writerows(data)

        # Go To Next Page
        forwards.click()
except Exception as e:
    print(e)
    pass
driver.close()
