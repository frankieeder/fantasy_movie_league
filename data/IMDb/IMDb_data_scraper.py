from bs4 import BeautifulSoup, NavigableString
import urllib.request
import csv
import os
import ssl
import datetime
from bisect import bisect_left

def split_list(iterable, splitters):
    splitters = set(splitters)
    lists = []
    this_list = []
    for elem in iterable:
        if elem in splitters:
            if len(this_list) > 0:
                lists.append(this_list)
                this_list = []
            continue
        else:
            this_list.append(elem)
    return lists

def writeTable(table, filename):
    """Writes table to csv.
    :param table: The table to write (should be indexed by rows then columns)
    :param filename: The directory to write the csv to
    :return: None
    """
    with open(filename, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(table)
def getText(item):
    return item.get_text() if item else None

def IMDBResultToRow(tag):
    header = tag.find("h3", **{"class":"lister-item-header"})
    strings = [s for s in tag.descendants if isinstance(s, NavigableString)]
    title = header.find("a")
    title = title and title.get_text()
    year = header.find("span", **{"class":"lister-item-year text-muted unbold"})
    year = year and year.get_text().split()
    year = (year or None) and year[-1][1:5]
    runtime = tag.find("span", **{"class":"runtime"})
    runtime = runtime and runtime.get_text()[:-4]
    genre = tag.find("span", **{"class":"genre"})
    genre = genre and genre.get_text().strip()
    imdb_rating = tag.find("strong")
    imdb_rating = imdb_rating and imdb_rating.get_text()
    metacritic_rating = tag.find("div", **{"class":"inline-block ratings-metascore"})
    metacritic_rating = metacritic_rating and metacritic_rating.find("span").get_text()
    crew_query = tag.find(lambda x: "Director:" in x.previous_element) or tag.find(lambda x: "Stars:" in x.previous_element)
    if crew_query:
        crew_query = [s.strip() for s in crew_query.parent.get_text().split("\n")]
        lists = split_list(crew_query, ("|", ""))
        objs = {l[0]:" ".join(l[1:]) for l in lists}
        directors = objs.get("Director:", None)
        cast = objs.get("Stars:", None)
    else:
        directors, cast = None, None
    numvotes = tag.find(lambda x: "Votes:" in x)
    numvotes = numvotes and numvotes.next_sibling.next_sibling.get_text()
    result = [
        title,
        year,
        runtime,
        genre,
        imdb_rating,
        metacritic_rating,
        directors,
        cast,
        numvotes
    ]
    return result

# Make output folder
os.chdir(os.path.dirname(os.path.realpath(__file__)))
if not os.path.exists('output/'):
    os.makedirs('output/')

# Figure out what is left to scrape
generated_csvs = [f for f in os.listdir('./output/') if f[-4:] == ".csv"]
starting_year = 1978
ending_year = datetime.datetime.now().year
seen_years = {int(f[:-4]) for f in generated_csvs}
all_years = set(range(starting_year, ending_year + 1))
years_to_collect = all_years - seen_years

for year in years_to_collect:
    base_url = "https://www.imdb.com/search/title"
    next = "?year={0}&title_type=feature&sort=release_date,asc".format(year)
    context = ssl._create_unverified_context()
    data = [["title", "year", "runtime", "genres", "imdb_rating", "metacritic_rating", "directors", "cast", "numvotes"]]
    while next:
        src = urllib.request.urlopen(base_url + next, context=context).read()
        soup = BeautifulSoup(src, 'html.parser')
        results = soup.find_all("div", **{'class':'lister-item mode-advanced'})
        processed_results = [IMDBResultToRow(r) for r in results]
        next = soup.find_all("a", text="Next »")
        next = next[0]["href"] if next else None
        data.extend(processed_results)
    csvfile = "./output/{0}.csv".format(year)
    writeTable(data, csvfile)