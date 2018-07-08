# Title     : TODO
# Objective : TODO
# Created by: frankieeder
# Created on: 7/7/18

# Libraries
library(plyr)
library(stringr)
library(data.table)
library(onehot)

replace.vals.dt = function(dt, filter, replacement, cols.to.replace = names(dt)) {
  for (col in cols.to.replace)
    dt[filter(get(col)), (col) := replacement]
  
  return(dt)
}

parse.digit <- function (str) {
  as.numeric(gsub("[^0-9-]", "", str))
}

# Pull and format scraped data
BOM.dirs <- list.files(path = "./data/BoxOfficeMojo/output", full.names = T)
BOM.tables <- lapply(BOM.dirs, read.csv)
BOM.dt <- data.table(do.call(what = rbind.fill, args = BOM.tables))
names(BOM.dt)[names(BOM.dt) == "Title..click.to.view."] = "Title"
setkey(BOM.dt, Title)
BOM.dt.clean <- replace.vals.dt(BOM.dt, function (x) x == "-", NA)


IMDb.dirs <- list.files(path = "./data/IMDb/output", full.names = T)
IMDb.tables <- lapply(IMDb.dirs, read.csv)
IMDb.dt <- data.table(do.call(what = rbind.fill, args = IMDb.tables))
setkey(IMDb.dt, title)

# Check for missing IMDb results
title.intersect <- intersect(BOM.dt[, Title], IMDb.dt[, title])
not.in.IMDb <- setdiff(BOM.dt[, Title], IMDb.dt[, title])
bad.BOM <- BOM.dt[not.in.IMDb]
unique.BOM <- unique(BOM.dt[, Title])

# Merge data
movie.dt <- merge(
  BOM.dt, 
  IMDb.dt, 
  by.x = key(BOM.dt), 
  by.y = key(IMDb.dt)
)

numeric.cols <- c("Weekend.Gross", "TW")
BOM.dt.clean <- BOM.dt.clean[ , (cols) := lapply(.SD, parse.digit), .SDcols = ]

make.true.mappings <- function (keywords) {
  mappings <- lapply(keywords, function (x) setNames(list(T), x))
  names(mappings) <- keywords
  mappings
}

# Make Genre Mappings
all.genres <- data.table(table(unlist(str_split(movie.dt$genres, pattern = ", "))))
good.genres <- all.genres[N > 100 & V1 != "", V1]
mappings.genre <- make.true.mappings(good.genres)

all.cast <- data.table(table(unlist(str_split(IMDb.dt$cast, pattern = ", "))))
good.cast <- all.cast[N > 15 & V1 != "", V1]

all.directors <- data.table(table(unlist(str_split(IMDb.dt$directors, pattern = ", "))))
good.directors <- all.directors[N > 2 & V1 != "", V1]

movie.explanatory.df <- movie.dt[, .(TW, Studio, )]


map.keyword.implications <- function(dt, mappings, search.by = names(dt), fixed = F, useBytes = F) {
  # Uses mappings, a list structure containing knowledge about the implications of certain keywords, and populates a data.table
  # row by row accordingly.
  #
  # Args:
  #   dt: A data.table to populate
  #   mappings: A mappings list structure specifying how to populate data frame. The structure is as follows:
  #             The names of the contents of mappings should be the keywords that we are searching for.
  #             Each corresponding sub-list should contain named values, the name being the name of the column we want
  #             to create or populate, the value being the value to populate it with.
  #   search.by: The columns in dt to search for keywords in. Default is names(dt)
  #
  # Returns:
  #   The populated data.frame
  #TODO: might want raise warning when multiple keywords overlap same area

  #Input checking
  common.columns <- intersect(names(dt), search.by)
  if (length(common.columns) < length(search.by)) {
    warning("Some columns in search.by are not in dt. Moving forward only with those that are in dt.")
    search.by <- common.columns
  }
  if (!fixed) {
    setkeyv(dt, search.by) #Setting keys empirically optimizes. weird.
  }
  for (keyword in names(mappings)) {
    #cat("Mapping keyword: ", keyword, "\n")
    #cat("  Finding keywords...\n")
    #browser()
    rows.w.keyword <- dt[, Reduce(function(x,y) x | y, lapply(.SD, function(x) grepl(keyword, x, fixed = fixed, useBytes = useBytes))), .SDcols = search.by]
    #cat("  Populating DT...\n")
    for (mapping in names(mappings[[keyword]])) { # perform mappings
      dt[rows.w.keyword, mapping] <- mappings[[keyword]][[mapping]]
    }
  }
  #cat("\n")
  dt
}

populated.movie.dt <- map.keyword.implications(
  dt = movie.dt,
  mappings = mappings.genre,
  search.by = "genres",
  fixed = T
)
