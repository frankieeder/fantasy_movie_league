import pandas as pd
import numpy as np
from models.utils import *
import os
import models.tmdb_searcher as tmdbs
import models.imdb_searcher as imdbs
import re

pd.set_option('display.max_rows', 50)
pd.set_option('display.max_columns', 50)

cwd = os.getcwd()
#### BOM
# Get and populate raw data
BOM_path = "../data/BoxOfficeMojo/output"
BOM_dirs = [os.path.join(cwd, BOM_path, f) for f in os.listdir(BOM_path) if f[-4:] == ".csv"]
BOM_dfs = [pd.read_csv(f) for f in BOM_dirs]
BOM_df = pd.concat(BOM_dfs)

# Cut useless columns and type data
BOM_df.columns = replace_list(list(BOM_df.columns), {'Title (click to view)': "title", "LW": "LW Ranking"})
BOM_good_cols = ['Weekend Gross', 'title', 'LW Ranking', 'Theater Count', 'Theater Change',
                 'Total Gross', 'Week #', 'year', 'week']
BOM_categorical_cols = ["title"]
BOM_numeric_cols = [c for c in BOM_good_cols if c not in BOM_categorical_cols]
BOM_df = BOM_df[BOM_good_cols]
BOM_df[BOM_numeric_cols] = BOM_df[BOM_numeric_cols].replace(regex=["[^0-9.-]", "^-$"], value=["", ""]).apply(pd.to_numeric, errors='coerce')
BOM_df.loc[:, 'year'] = BOM_df['year'].astype(int) #TODO: This shouldn't be necessary tho!
unique_BOM_movies = BOM_df['title'].drop_duplicates()
# Process grosses
BOM_df['LW Total Gross'] = BOM_df['Total Gross'] - BOM_df['Weekend Gross']
# Trim data rowwise
BOM_df = BOM_df.loc[BOM_df['Week #'] > 0, :]
BOM_df = BOM_df.loc[BOM_df['LW Total Gross'] >= 0, :]
BOM_df.loc[pd.isnull(BOM_df['Theater Change']) & (BOM_df['Week #'] > 1), 'Theater Change'] = 0
BOM_df = BOM_df.loc[~BOM_df['title'].str.contains('re-issue', case=False), :]

BOM_df.columns = ["bom_" + e for e in BOM_df.columns]

#### TMDB
# Pull crucial data, and merge to make initial df
TMDB_ids = tmdbs.get_tmdb_movie_id.dict(unique_BOM_movies)
TMDB_title_details = tmdbs.get_tmdb_movie_details.df(TMDB_ids.values())
TMDB_title_crew = tmdbs.get_tmdb_movie_crew.df(TMDB_ids.values())
TMDB_df = TMDB_title_details.merge(TMDB_title_crew, how='outer', on='id')
# Remerge ideas back into dataframe for later extrapolation (we do this hear to avoid np.NaN's when caching)
TMDB_ids_df = pd.DataFrame.from_dict(TMDB_ids, orient='index')
TMDB_ids_df['bom_title'] = TMDB_ids_df.index
TMDB_ids_df.columns = replace_list(TMDB_ids_df.columns, {0: "id"})
# Cut useless columns
TMDB_good_cols = ['id', 'belongs_to_collection', 'budget', 'genres',
       'popularity', 'release_date', 'runtime',
       'title', 'vote_average', 'cast', 'crew', 'production_companies']
TMDB_imdb_ids = TMDB_df['imdb_id']
TMDB_df = TMDB_df[TMDB_good_cols]
# Process release dates
TMDB_year_splits = TMDB_df['release_date'].str.split("-", expand=True).apply(pd.to_numeric, errors='coerce')
TMDB_df.loc[:, 'release_year'] = TMDB_year_splits[0]
TMDB_df.loc[:, 'release_month'] = TMDB_year_splits[1]
TMDB_df.loc[:,'release_day'] = TMDB_year_splits[2]
TMDB_df = TMDB_df.drop('release_date', 1)
# Process belongs_to_collection
TMDB_df['belongs_to_collection'] = [(True if e else False) for e in TMDB_df['belongs_to_collection']]
# Process genres
genre_splitter = lambda x: [] if not x else [g['name'] for g in x]
TMDB_genres = one_hot_encode(TMDB_df['id'], TMDB_df['genres'], genre_splitter)
TMDB_df = TMDB_df.merge(TMDB_genres, left_on='id', right_index=True).drop('genres', 1)
# Reappend bom_id's
TMDB_df = TMDB_df.merge(TMDB_ids_df, on='id')

# TODO: Process cast
TMDB_df = TMDB_df.drop('cast', 1)
# TODO: Process crew
TMDB_df = TMDB_df.drop('crew', 1)
# TODO: Process production_companies
TMDB_df = TMDB_df.drop('production_companies', 1)

TMDB_df.columns = ["tmdb_" + e for e in TMDB_df.columns]

## should be updated to include imdb things:
movie_dt = BOM_df.merge(TMDB_df, left_on='bom_title', right_on='tmdb_bom_title').drop('tmdb_bom_title', 1)

#### IMDB
IMDb_data = imdbs.get_imdb_title_data_from_id.df(TMDB_imdb_ids)
actors = IMDb_data['actors'].drop_duplicates()
directors = IMDb_data['directors'].drop_duplicates()
actorsdict = {a: imdbs.get_imdb_people_data(a) for a in actors}
directorsdf = {d: imdbs.get_imdb_people_data(d) for d in directors}
if False:
    """PROB BAD STRATEGY TO ACCOMPLISH THIS"""
    IMDb_path = "../data/IMDb/output"
    IMDb_dirs = [os.path.join(cwd, IMDb_path, f) for f in os.listdir(IMDb_path) if f[-4:] == ".csv"]
    IMDb_tables = [pd.read_csv(f) for f in IMDb_dirs]
    IMDb_df = pd.concat(IMDb_tables)
    IMDb_df = IMDb_df.set_index('title', drop=False)
    IMDb_df = IMDb_df.loc[unique_BOM_movies,:]
    IMDb_df.columns = ["imdb_" + e for e in IMDb_df.columns]

    # Process and attach Actors, Directors, and Genres
    directors = IMDb_df["imdb_directors"].drop_duplicates()
    cast = IMDb_df["imdb_cast"].drop_duplicates()
    genres = IMDb_df["imdb_genres"].drop_duplicates()
    director_dict = {d: imdbs.get_imdb_people_data(d) for d in directors}
    director_df = pd.DataFrame.from_dict(director_dict, orient='index')
    cast_dict = {c: imdbs.get_imdb_people_data(c) for c in cast}
    cast_df = pd.DataFrame.from_dict(cast_dict, orient='index')
    genres_dict = {g: imdbs.get_imdb_people_data(g) for g in genres}
    genres_df = pd.DataFrame.from_dict(genres_dict, orient='index')

x = 2
