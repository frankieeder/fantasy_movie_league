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
  # Simple function to take a string and return the digits in it, accounting for decimals and negatives.
  as.numeric(gsub("[^0-9.-]", "", str))
}


# Pull and format scraped data
BOM.dirs <- list.files(path = "./data/BoxOfficeMojo/output", full.names = T)
BOM.tables <- lapply(BOM.dirs, read.csv)
BOM.dt <- data.table(do.call(what = rbind.fill, args = BOM.tables))
names(BOM.dt)[names(BOM.dt) == "Title..click.to.view."] = "Title"
setkey(BOM.dt, Title)

IMDb.dirs <- list.files(path = "./data/IMDb/output", full.names = T, include.dirs = F)
IMDb.tables <- lapply(IMDb.dirs, read.csv)
IMDb.dt <- data.table(do.call(what = rbind.fill, args = IMDb.tables))
setkey(IMDb.dt, title)

# Check data quantities
title.intersect <- intersect(BOM.dt[, Title], IMDb.dt[, title])
not.in.IMDb <- setdiff(BOM.dt[, Title], IMDb.dt[, title])
bad.BOM <- BOM.dt[not.in.IMDb]
unique.BOM <- unique(BOM.dt[, Title])

# Format tables and one-hot encode
one.hot.encode <- function(dt, search.cols, thresholds = rep(0, length(search.cols)), split.pattern = ", ", drop.originals = T) {
  for (i in 1:length(search.cols)) {
    this.search.col <- search.cols[i]
    this.threshold <- thresholds[i]
    this.col <- sapply(movie.dt[, ..this.search.col], as.character)
    all.keywords <- unlist(str_split(this.col, split.pattern))
    counts <- data.table(table(all.keywords))
    good.categorical.values <- counts[N > this.threshold, all.keywords]
    for (keyword in good.categorical.values) {
      dt[ , paste(this.search.col, keyword, sep = ".") := ifelse(grepl(keyword, this.col, fixed = T), 1, 0)]    
    }
    if (drop.originals) dt[ , (this.search.col) := NULL]
  }
  dt
}

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



