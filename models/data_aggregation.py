import pandas as pd
import numpy as np
import os
import re
from models.metascraping import *
import statistics
import itertools

pd.set_option('display.max_rows', 50)
pd.set_option('display.max_columns', 500)

def parse_digit(string):
    return float(re.sub("[^0-9.-]", "", string)) if isinstance(string, str) else string

def replace_list(list, val, replacement):
    return [(replacement if i == val else i) for i in list]

cwd = os.getcwd()
BOM_path = "../data/BoxOfficeMojo/output"
BOM_dirs = [os.path.join(cwd, BOM_path, f) for f in os.listdir(BOM_path) if f[-4:] == ".csv"]
BOM_tables = [pd.read_csv(f) for f in BOM_dirs]
BOM_table = pd.concat(BOM_tables)
BOM_table.columns = replace_list(list(BOM_table.columns),'Title (click to view)', "Title")


IMDb_path = "../data/IMDb/output"
IMDb_dirs = [os.path.join(cwd, IMDb_path, f) for f in os.listdir(IMDb_path) if f[-4:] == ".csv"]
IMDb_tables = [pd.read_csv(f) for f in IMDb_dirs]
IMDb_table = pd.concat(IMDb_tables)

movie_table = BOM_table.merge(IMDb_table, left_on="Title", right_on="title")
good_cols = ['LW', 'Studio', 'Weekend Gross', '% Change',
       'Theater Count', 'Theater Change', 'Average', 'Total Gross', 'Budget*',
       'Week #', 'title', 'year', 'runtime', 'genres', 'imdb_rating',
       'metacritic_rating', 'directors', 'cast', 'numvotes']
categorical_cols = ["Studio", "genres", "directors"]
cols_to_ignore_temp = ["title", "cast"]
numerical_cols = list(set(good_cols) - set(categorical_cols) - set(cols_to_ignore_temp))

movie_table = movie_table.loc[:, good_cols]
movie_table = movie_table.replace(["-", "", "N"], value=np.NaN)
movie_table.loc[:, numerical_cols] = movie_table.loc[:, numerical_cols].applymap(parse_digit)


# Process Actors and
directors = set(movie_table.loc[:, "directors"])
actors = set(movie_table.loc[:, "cast"])
people = directors | actors
people.remove(np.NaN)
for person in people:
    person_scores = get_person_scores(person)


