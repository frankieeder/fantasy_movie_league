import pandas as pd
import numpy as np
from models.utils import *
import os
import models.tmdb_searcher as tmdbs

pd.set_option('display.max_rows', 50)
pd.set_option('display.max_columns', 50)

cwd = os.getcwd()
#### BOM
# Get and populate raw data
BOM_path = "../data/BoxOfficeMojo/output"
BOM_dirs = [os.path.join(cwd, BOM_path, f) for f in os.listdir(BOM_path) if f[-4:] == ".csv"]
BOM_tables = [pd.read_csv(f) for f in BOM_dirs]
BOM_table = pd.concat(BOM_tables)

# Format, Cleans, and Select Data
BOM_table.columns = replace_list(list(BOM_table.columns), {'Title (click to view)': "title", "LW": "LW Ranking"})
BOM_good_cols = ['Weekend Gross', 'LW Ranking', 'title', 'Theater Count', 'Theater Change',
                 'Total Gross', 'Week #', 'year']
BOM_categorical_cols = ["title"]
BOM_numeric_cols = [c for c in BOM_good_cols if c not in BOM_categorical_cols]
BOM_table = BOM_table[BOM_good_cols]
BOM_table[BOM_numeric_cols] = BOM_table[BOM_numeric_cols].replace(regex=["[^0-9.-]", "^-$"], value=["", ""]).apply(pd.to_numeric, errors='coerce')
BOM_table.loc[:, 'year'] = BOM_table['year'].astype(int) #TODO: This shouldn't be necessary tho!
BOM_table['LW Total Gross'] = BOM_table['Total Gross'] - BOM_table['Weekend Gross']
BOM_table.drop('Total Gross', 1)
unique_BOM_movies = BOM_table['title'].drop_duplicates()
BOM_table.columns = ["bom_" + e for e in BOM_table.columns]


#### TMDB
# Pull crucial data, and merge to make initial df
TMDB_ids = tmdbs.get_tmdb_movie_id.dict(unique_BOM_movies)
TMDB_title_details = tmdbs.get_tmdb_movie_details.df(TMDB_ids.values())
TMDB_title_crew = tmdbs.get_tmdb_movie_crew.df(TMDB_ids.values())
TMDB_df = TMDB_title_details.merge(TMDB_title_crew, how='outer', on='id')
# Cut useless columns
TMDB_good_cols = ['id', 'belongs_to_collection', 'budget', 'genres',
       'popularity', 'release_date', 'runtime',
       'title', 'vote_average', 'cast', 'crew', 'production_companies']
TMDB_df = TMDB_df[TMDB_good_cols]
# Process release dates
TMDB_year_splits = TMDB_df['release_date'].str.split("-", expand=True).apply(pd.to_numeric, errors='coerce')
TMDB_df['release_year'] = TMDB_year_splits[0]
TMDB_df['release_month'] = TMDB_year_splits[1]
TMDB_df['release_day'] = TMDB_year_splits[2]
TMDB_df = TMDB_df.drop('release_date', 1)
# Process belongs_to_collection
TMDB_df['belongs_to_collection'] = [(True if e else False) for e in TMDB_df['belongs_to_collection']]
# Process genres
genre_splitter = lambda x: [] if not x else [g['name'] for g in x]
TMDB_genres = one_hot_encode(TMDB_df['id'], TMDB_df['genres'], genre_splitter)
TMDB_df = TMDB_df.merge(TMDB_genres, left_on='id', right_index=True).drop('genres', 1)

# TODO: Process cast
TMDB_df = TMDB_df.drop('cast', 1)
# TODO: Process crew
TMDB_df = TMDB_df.drop('crew', 1)
# TODO: Process production_companies
TMDB_df = TMDB_df.drop('production_companies', 1)

TMDB_df.columns = ["tmdb_" + e for e in TMDB_df.columns]


