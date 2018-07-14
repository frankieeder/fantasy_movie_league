import pandas as pd
import numpy as np
from models.utils import *
import os
import models.metascraping as ms

pd.set_option('display.max_rows', 50)
pd.set_option('display.max_columns', 50)

cwd = os.getcwd()
#### BOM
# Get and populate raw data
BOM_path = "../data/BoxOfficeMojo/output"
BOM_dirs = [os.path.join(cwd, BOM_path, f) for f in os.listdir(BOM_path) if f[-4:] == ".csv"]
BOM_tables = [pd.read_csv(f) for f in BOM_dirs]
for dirname, table in zip(BOM_dirs, BOM_tables):
    table.loc[:, "year"] = int(dirname[-8:-4])
BOM_table = pd.concat(BOM_tables)

# Format, Cleans, and Select Data
BOM_table.columns = replace_list(list(BOM_table.columns), {'Title (click to view)': "title", "LW": "LW Ranking"})
BOM_good_cols = ['title', 'year', 'LW Ranking', 'Weekend Gross', 'Total Gross', 'Theater Count', 'Theater Change']
BOM_table = BOM_table.loc[:, BOM_good_cols]
BOM_table = BOM_table.replace(["-", "", "N"], value=np.NaN)
BOM_table.loc[:, 'Total Gross'] = [parse_digit(tg) - parse_digit(wg) for tg, wg in zip(BOM_table['Total Gross'], BOM_table['Weekend Gross'])]
BOM_table.columns = replace_list(list(BOM_table.columns), {'Total Gross': "LW Total Gross"})
unique_BOM_movies = BOM_table.loc[:, ["title", "year"]].drop_duplicates()
BOM_table.columns = replace_list(BOM_table.columns, {e: "bom_" + e for e in ["year", "LW Ranking", "Weekend Gross", "Total Gross", "Theater Count", "Theater Change"]})




IMDb_path = "../data/IMDb/output"
IMDb_dirs = [os.path.join(cwd, IMDb_path, f) for f in os.listdir(IMDb_path) if f[-4:] == ".csv"]
IMDb_tables = [pd.read_csv(f) for f in IMDb_dirs]
IMDb_table = pd.concat(IMDb_tables)
unique_IMDb_movies = IMDb_table.loc[:, ["title", "year"]].drop_duplicates()
IMDb_table = IMDb_table.merge(unique_BOM_movies, on=["title", "year"])
IMDb_table.columns = replace_list(IMDb_table.columns, {e: "imdb_" + e for e in ["year", "runtime", "genres", "directors", "cast", "numvotes"]})

# Process and attach Actors, Directors, and Genres
directors = IMDb_table.loc[:, "imdb_directors"].drop_duplicates()
cast = IMDb_table.loc[:, "imdb_cast"].drop_duplicates()
genres = IMDb_table.loc[:, "imdb_genres"].drop_duplicates()
directordf = function_results_to_df(directors, ms.get_imdb_people_data, input_name="imdb_directors")
castdf = function_results_to_df(cast, ms.get_imdb_people_data, input_name="imdb_cast")
genresdf = function_results_to_df(genres, one_hot_encode, input_name="imdb_genres")

meta_table = IMDb_table.merge(directordf).drop("imdb_directors", 1)
meta_table = meta_table.merge(castdf).drop("imdb_cast", 1)
meta_table = meta_table.merge(genresdf).drop("imdb_genres", 1)

train_data = BOM_table.merge(meta_table)
good_cols = [
    'bom_Weekend Gross', 'bom_LW Ranking', 'LW Total Gross', 'bom_Theater Count', 'bom_Theater Change',
     'imdb_year', 'imdb_runtime', 'imdb_rating', 'metacritic_rating', 'imdb_numvotes',
     # director vbls
     'imdb_directors_num_wins', 'imdb_directors_Writer', 'imdb_directors_win_nom_ratio',
     'imdb_directors_num_noms', 'imdb_directors_Director', 'imdb_directors_Producer',
     'imdb_directors_Thanks', 'imdb_directors_Editor', 'imdb_directors_Self', 'imdb_directors_Special effects',
     'imdb_directors_Art department', 'imdb_directors_Art director',
     'imdb_directors_Camera and Electrical Department', 'imdb_directors_star_rank',
     'imdb_directors_Cinematographer', 'imdb_directors_Visual effects',
     # cast vbls
     'imdb_cast_Actor', 'imdb_cast_win_nom_ratio', 'imdb_cast_num_noms', 'imdb_cast_Self', 'imdb_cast_num_wins',
     'imdb_cast_Actress', 'imdb_cast_star_rank', 'imdb_cast_Director', 'imdb_cast_Producer',
     # genres
     'imdb_genres_Biography', 'imdb_genres_Comedy', 'imdb_genres_Drama', 'imdb_genres_Thriller',
     'imdb_genres_Action', 'imdb_genres_Crime', 'imdb_genres_Sport', 'imdb_genres_Family',
     'imdb_genres_History', 'imdb_genres_Mystery', 'imdb_genres_Horror', 'imdb_genres_Western',
     'imdb_genres_Adventure', 'imdb_genres_Romance', 'imdb_genres_Fantasy', 'imdb_genres_Animation',
     'imdb_genres_Sci-Fi', 'imdb_genres_Musical', 'imdb_genres_War', 'imdb_genres_Music'
]
train_data = train_data.loc[:, good_cols]
train_data = train_data.replace(np.NaN, value=0)
train_data = train_data.applymap(parse_digit)



x = 3


