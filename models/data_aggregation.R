# Title     : TODO
# Objective : TODO
# Created by: frankieeder
# Created on: 7/7/18

# Libraries
library(plyr)
library(stringr)
library(data.table)
library(onehot)
library(reticulate)
library(qdapTools)

lists.as.dt <- function(lst, key.col.name='key') {
  args = lapply(
    names(lst),
    function (x) {
      this.df = data.frame(lst[[x]])
      if (nrow(this.df) > 0) {
        this.df$key = x
      } else {
        this.df = data.frame(key = x)
      }
      this.df
    }
  )
  dt = data.table(do.call(what = rbind.fill, args = args))
  names(dt)[1] = key.col.name
  setkeyv(dt, key.col.name)
  dt
}
replace.vals.dt = function(dt, filter, replacement, cols.to.replace = names(dt)) {
  for (col in cols.to.replace)
    dt[filter(get(col)), (col) := replacement]
  return(dt)
}
parse.digit <- function (str) {
  # Simple function to take a string and return the digits in it, accounting for decimals and negatives.
  as.numeric(gsub("[^0-9.-]", "", str))
}
replace.list <- function (list, mappings) {
  for (k in names(mappings)) {
    list[list == k] = mappings[[k]]
  }
  list
}


### BOM as primary response data:
# Pull data
BOM.dirs <- list.files(path = "./data/BoxOfficeMojo/output", full.names = T)
BOM.tables <- lapply(BOM.dirs, function (x) read.csv(x, stringsAsFactors = F))
BOM.dt <- as.data.table(do.call(what = rbind.fill, args = BOM.tables))
# Format Columns
names(BOM.dt) <- replace.list(names(BOM.dt), list(
  `Title..click.to.view.` = "title", 
  `Week..` = "Week #",
  `week` = "weekend"
))
names(BOM.dt) <- gsub("[.]", " ", names(BOM.dt))
names(BOM.dt) <- str_trim(names(BOM.dt))
# Clean, format, and process data - columnwise
BOM.good.cols = c('Weekend Gross', 'LW', 'title', 'Theater Count', 'Theater Change',
                 'Total Gross', 'Week #', 'year', 'weekend')
BOM.numeric.cols = setdiff(BOM.good.cols, "title")
BOM.dt = BOM.dt[, ..BOM.good.cols]
for (col in BOM.numeric.cols) set(BOM.dt, j = col, value = sapply(BOM.dt[, ..col], parse.digit))
BOM.dt[, c("Pre-Weekend Total Gross")] <- BOM.dt[, c("Total Gross")] - BOM.dt[, c("Weekend Gross")]
names(BOM.dt) = paste0("bom_", names(BOM.dt))
setkey(BOM.dt, bom_title)
# Unique Titles:
unique.BOM.movies = unique(BOM.dt[, .(bom_title, bom_year)])


IMDb.dirs <- list.files(path = "./data/IMDb/output", full.names = T, include.dirs = F)
IMDb.tables <- lapply(IMDb.dirs, function (x) read.csv(x, stringsAsFactors = F))
IMDb.all.dt <- data.table(do.call(what = rbind.fill, args = IMDb.tables))
# Filter IMDb results by the ones that we have actual response data for
# TODO: Ideally, this should somehow account for movies that may have been made one year and came out another, or rereleased later, or have multiple names.
IMDb.dt = merge(IMDb.all.dt, unique.BOM.movies, by.x = c("title", "year"), by.y = c("bom_title", "bom_year")) 


# TODO: implement updated imdb scraper instead of using above, in similar manner as the next few lines.
person_score_dir <- paste0(getwd(), "/models/get_imdb_person_data.pkl")
imdb.person.dict <- py_load_object(person_score_dir)
# imdb.people = names(imdb.person.pkl)
# imdb.people.to.process = ...
# Send imdb.people.to.process to python using command line...
imdb.person.data = lists.as.dt(imdb.person.dict, 'person')
imdb.person.data = replace.vals.dt(imdb.person.data, is.na, 0)

get.imdb.people.data.df <- function (str, person.data = imdb.person.data, lookup.on = names(imdb.person.data), sep = ", ", input_name = key(person.data)) {
  #browser()
  dts = lapply(str, function (s) {
    person.data[str_split(s, sep), lapply(.SD, max), .SDcols = lookup.on][, c(input_name) := s]
  })
  data.table(do.call(what = rbind.fill, args = dts))
}

directors_cols = c('num_wins', 'Writer', 'win_nom_ratio', 'num_noms', 'Director', 'Producer', 'Thanks', 'Editor', 'Self', 'Special.effects', 'Art.director', 'star_rank', 'Cinematographer', 'Visual.effects')
cast_cols = c('Actor', 'win_nom_ratio', 'num_noms', 'Self', 'num_wins', 'Actress', 'star_rank', 'Director', 'Producer')
directors.dt <- get.imdb.people.data.df(unique(IMDb.dt[ , directors]), on = directors_cols, input_name = "directors")
names(directors.dt) <- paste0("imdb_directors_", names(directors.dt))
cast.dt <- get.imdb.people.data.df(unique(IMDb.dt[ , cast]), on = cast_cols, input_name = "cast")
names(cast.dt) <- paste0("imdb_cast_", names(cast.dt))

one.hot.encode.df <- function(df, search.cols, split.pattern = ", ", drop.originals = T) {
  for (col in search.cols) {
    #browser()
    encoded = mtabulate(str_split(df[[col]], split.pattern))
    names(encoded) = paste0(col, "_", names(encoded))
    df <- cbind(df, encoded)
  }
  if (drop.originals) df[[search.cols]] <- NULL
  return(df)
}

explanatory.dt <- one.hot.encode.df(IMDb.dt, "genres", drop.originals = T)
explanatory.dt <- merge(explanatory.dt, directors.dt, by.x = "directors", by.y = "imdb_directors_directors")[, !"directors", with=F]
explanatory.dt <- merge(explanatory.dt, cast.dt, by.x = "cast", by.y = "imdb_cast_cast")[, !"cast", with=F]



# Merge data
movie.dt <- merge(
  BOM.dt, 
  IMDb.dt, 
  by.x = key(BOM.dt), 
  by.y = key(IMDb.dt)
)
good.cols <- c("LW", "Studio", "Weekend.Gross", "X..Change", "Theater.Count", "Theater.Change", "Average", "Total.Gross", "Budget.", "Week..", "year", "runtime", "genres", "imdb_rating", "metacritic_rating", "directors", "numvotes")
categorical.cols <- c("Studio", "genres", "directors")
numeric.cols <- setdiff(good.cols, categorical.cols)

movie.dt <- movie.dt[, ..good.cols]
movie.dt <- replace.vals.dt(movie.dt, function (x) x == "-", NA)
movie.dt <- replace.vals.dt(movie.dt, function (x) x == "", NA)
movie.dt[ , (numeric.cols) := lapply(.SD, parse.digit), .SDcols = numeric.cols]

# One hot encoding might have problems here since we have joined the table and the counts of each genre might be too large. This actually could be helpful as well though as it might increase counts for movies that were successful at the box office.
movie.dt <- one.hot.encode(movie.dt, categorical.cols, thresholds = c(100, 10, 20))



