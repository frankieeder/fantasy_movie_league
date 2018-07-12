# TODO: FIX THIS AND MAKE IT PART OF A PACKAGE PROBABLY AND FIX DIRECTORY PATHS
from selenium import webdriver
from functools import reduce
from bs4 import BeautifulSoup
from models.utils import *
import pickle
import os
import urllib.request
import re
import ssl


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
            self(key, update=True)
        if save:
            self.save()

    def save(self, output_file=None):
        if not output_file:
            output_file = self.file
        with open(output_file, 'wb') as output:
            pickle.dump(self.memo, output, pickle.HIGHEST_PROTOCOL)

def merge_dicts(*dict_args):
    """
    Given any number of dicts, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dicts.
    """
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result


def apply_dicts_keywise(dicts, f, default):
    max_dict = {}
    all_keys = reduce(lambda x, y: x | y, [set(d.keys()) for d in dicts])
    for key in all_keys:
        max_dict[key] = f((d[key] if (key in d) else default) for d in dicts)
    return max_dict

# SEARCHERS
def search_imdb(query, first_result=True, query_type=None):
    formatted_query = query.lower().replace(" ", "+")
    query_type = query_type if query_type else "all"
    search_page = "https://www.imdb.com/find?q={0}&s={1}".format(formatted_query, query_type)
    if first_result:
        driver = webdriver.Chrome()
        driver.get(search_page)
        results = driver.find_element_by_class_name("findList")
        first_result = results.find_element_by_xpath("//td[2]").find_element_by_tag_name("a")
        first_result.click()
        finish_url = driver.current_url
        driver.close()
        return finish_url
    return search_page

def search_lb(query, first_result=True, query_type=""):
    formatted_query = query.lower().replace(" ", "+")
    search_page = "https://letterboxd.com/search/{0}/{1}/".format(query_type, formatted_query)
    if first_result:
        driver = webdriver.Chrome()
        driver.get(search_page)
        first_result = driver.find_element_by_class_name('search-result').find_element_by_tag_name("a")
        first_result.click()
        finish_url = driver.current_url
        driver.close()
        return finish_url
    return search_page

def search_tmdb(query, first_result=True):
    formatted_query = query.lower().replace(" ", "+")
    search_page = "https://www.themoviedb.org/search?query={0}".format(formatted_query)
    if first_result:
        driver = webdriver.Chrome()
        driver.get(search_page)
        first_result = driver.find_element_by_class_name("item").find_element_by_tag_name("a")
        first_result.click()
        finish_url = driver.current_url
        driver.close()
        return finish_url
    return search_page


# PAGE SCRAPERS
def scrape_imdb_person(url):
    """Defines how to scrape data once we are on an imdb person main page."""
    base_url = re.search(".*/", url)[0]
    context = ssl._create_unverified_context()
    src = urllib.request.urlopen(base_url, context=context).read()
    soup = BeautifulSoup(src, "html.parser")

    filmography = soup.find(id="filmography")
    filmo_headers = filmography.find_all(**{'class': "head"})
    filmo_header_titles = [e.find("a").text for e in filmo_headers]
    filmo_sections = filmography.find_all(**{'class': "filmo-category-section"})
    filmo_section_counts = [len(s.find_all("div")) for s in filmo_sections]
    filmography_counts = {t: c for t, c in zip(filmo_header_titles, filmo_section_counts)}

    awards = scrape_imdb_person_awards(base_url + "awards/")

    meta = {}
    max_star_rank = 10000
    star_rank = soup.find("div",id="prometer_container").find("a").text
    if star_rank == "Top 500":
        meta["star_rank"] = max_star_rank - 500
    elif star_rank == "Top 5000":
        meta["star_rank"] = max_star_rank - 5000
    elif star_rank == "SEE RANK":
        pass
    else:
        meta["star_rank"] = max_star_rank - int(star_rank)
    # TODO: Could add more analysis here, number of photos and videos?
    return merge_dicts(filmography_counts, awards, meta)

def scrape_imdb_person_awards(url):
    """Defines how to scrape data once we are on an imdb person awards page."""
    base_url = re.search(".*/", url)[0]
    context = ssl._create_unverified_context()
    src = urllib.request.urlopen(base_url, context=context).read()
    soup = BeautifulSoup(src, "html.parser")

    results = {}
    award_count_string = soup.find("div", class_="desc").text
    if award_count_string:
        award_count_words = award_count_string.split()
        results["num_wins"] = int(award_count_words[2])
        results["num_noms"] = int(award_count_words[5])
        results["win_nom_ratio"] = results["num_wins"] / results["num_noms"]
    return results

def scrape_lb_studio_using_search_results(url):
    context = ssl._create_unverified_context()
    src = urllib.request.urlopen(url, context=context).read()
    soup = BeautifulSoup(src, "html.parser")
    first_result = soup.find("li", class_="search-result")
    first_result_metadata = first_result.find("p", class_="film-metadata")
    first_result_meta_string = first_result_metadata.contents[0]
    num_movies = int(re.search("[0-9]+", first_result_meta_string)[0])
    return {"num_movies": num_movies}

def scrape_tmdb_title(url):
    context = ssl._create_unverified_context()
    src = urllib.request.urlopen(url, context=context).read()
    soup = BeautifulSoup(src, "html.parser")

    budget_header = soup.find("bdi",string="Budget")
    budget = parse_digit(budget_header.parent.next_sibling)
    return {"budget": budget}


# GETTERS (combine search and scrape functions)
def get_imdb_person_data(person):
    try:
        person_url = search_imdb(person, first_result=True, query_type='nm')
        return scrape_imdb_person(person_url)
    except Exception as e:
        return {}
get_imdb_person_data = MemoizeToFile(get_imdb_person_data, file="./get_imdb_person_data.pkl")

def get_imdb_people_data(people):
    return apply_dicts_keywise([get_imdb_person_data(d) for d in people.split(", ")], max, 0)


def get_lb_studio_data(studio):
    studio_url = search_lb(studio, first_result=False, query_type="studios")
    return scrape_lb_studio_using_search_results(studio_url)
get_lb_studio_data = MemoizeToFile(get_lb_studio_data, file="./get_lb_studio_data.pkl")

def get_studios_data(studios):
    return apply_dicts_keywise([get_lb_studio_data(s) for s in studios.split(", ")], max, 0)

def get_title_data_tmdb(title):
    movie_url = search_tmdb(title)
    return scrape_tmdb_title(movie_url)
get_title_data_tmdb = MemoizeToFile(get_title_data_tmdb, file="./get_title_data_tmdb.pkl")





