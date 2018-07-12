# TODO: FIX THIS AND MAKE IT PART OF A PACKAGE PROBABLY AND FIX DIRECTORY PATHS
import pickle
import os
from selenium import webdriver
from statistics import mean
from functools import reduce
from bs4 import BeautifulSoup


class MemoizeToFile:
    def __init__(self, func, file):
        self.f = func
        self.file = file
        if os.path.isfile(file):
            with open(file, 'rb') as input_stream:
                self.memo = pickle.load(input_stream)
        else:
            self.memo = dict()
    
    def __call__(self, key, update=False, save=True):
        if not update and key in self.memo:
            return self.memo[key]
        else:
            value = self.f(key)
            self.memo[key] = value
            if save:
                self.save()
            return value
        
    def updateAll(self, save=True):
        for key in self.memo:
            self.get(key, update=True)
        if save:
            self.save()

    def save(self, output_file=None):
        if not output_file:
            output_file = self.file
        with open(output_file, 'wb') as output:
            pickle.dump(self.memo, output, pickle.HIGHEST_PROTOCOL)

driver = webdriver.Chrome()

def search_LB(query, first_result=True):
    pass

def search_imdb(query, first_result=True, querytype=None):
    driver.get("https://www.imdb.com/")
    dropdown = driver.find_element_by_class_name("quicksearch_dropdown")
    if querytype:
        query_type_selection = dropdown.find_element_by_css_selector("[value = '%a']" % querytype)
        query_type_selection.click()
    search = driver.find_element_by_id("navbar-query")
    search.send_keys(query)
    submit = driver.find_element_by_id("navbar-submit-button")
    submit.click()
    if first_result:
        results = driver.find_element_by_class_name("findList")
        first_result = results.find_element_by_xpath("//td[2]").find_element_by_tag_name("a")
        first_result.click()

def search_tmdb(query, first_result=True):
    pass

def maximize_dicts(dicts):
    max_dict = {}
    all_keys = reduce(lambda x, y: x | y, [set(d.keys()) for d in dicts])
    for key in all_keys:
        max_dict[key] = max((d[key] if (key in d) else 0) for d in dicts)
    return max_dict


def scrape_imdb_person():
    """Defines how to scrape data once we are on an imdb person main page."""
    soup = BeautifulSoup(driver.pagesource, "html.parser")
    filmography = driver.find_element_by_id("filmography")
    filmo_headers = filmography.find_elements_by_class_name("head")
    filmo_header_titles = [e.find_element_by_tag_name("a").text for e in filmo_headers]
    filmo_sections = filmography.find_elements_by_class_name("filmo-category-section")
    filmo_section_counts = [len(s.find_elements_by_tag_name("div")) for s in filmo_sections]
    credits = {t: c for t, c in zip(filmo_header_titles, filmo_section_counts)}
    return credits


def get_person_score(person):
    search_imdb(person, first_result=True, querytype='nm')
    return scrape_imdb_person_filmography()
get_person_score = MemoizeToFile(get_person_score, file="./get_person_score.pkl")


def get_person_scores(persons):
    return maximize_dicts([get_person_score(d) for d in persons.split(", ")])


def get_studio_score(studio):
    driver = webdriver.Chrome()
    base_url = "https://pro.imdb.com"
    driver.get("https://pro.imdb.com/company/co0390816/")
    driver.get("https://pro.imdb.com/company/co0390816/")
    # Get to correct page
    search = driver.find_element_by_id("searchField")
    search.send_keys(studio)
    results_field = driver.find_element_by_id("instantSearch")
    results = results_field.find_elements_by_tag_name("li")
    driver.implicitly_wait(1)
    soup = BeautifulSoup(results_field.get_attribute('innerHTML'), 'html.parser')
    companies_title = soup.find("span", string="Companies")
    first_company_result = companies_title.parent.nextSibling
    first_company = first_company_result.find("a")["href"]
    driver.get(base_url + first_company)
    # Once on new page:
    lower_box = driver.find_element_by_class_name("a-box-inner")
    soup = BeautifulSoup(lower_box.get_attribute('innerHTML'), 'html.parser')
    num_title_text = soup.find("span", **{'class':'a-size-mini a-color-secondary tab_subheading'})

    driver.close()
    return None



# get_studio_score("Warner Bros")


def get_studio_scores(studios):
    # TODO: This might not work...?
    return mean(get_studio_score(s)**3 for s in studios.split(", "))