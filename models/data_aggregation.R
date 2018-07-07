# Title     : TODO
# Objective : TODO
# Created by: frankieeder
# Created on: 7/7/18
install.packages(c("stringr", "data.table"), repos = "http://cran.us.r-project.org")
library(stringr)
library(data.table)
dirs.BOM <- list.dirs(path = "../data/BoxOfficeMojo/output/", full.names = TRUE, recursive = TRUE)




# Establish known Keyword Mappings
keyword.implication.mappings <- {list(
  `online` = list(
    channelType = "online"
  ),
  `offline` = list(
    channelType = "offline"
  ),
  `tv` = list(
    channel = "tv"
  ),
  `display` = list(
    channel = "display"
  ),
  `retargeting` = list(
    campaignStrategy = "retargeting"
  ),
  `search` = list(
    campaignStrategy = "search"
  ),
  `15` = list(
    spotType = "15"
  ),
  `30` = list(
    spotType = "30"
  ),
  `60` = list(
    spotType = "60"
  ),
  `post` = list(
    spotType = "post"
  ),
  `pre` = list(
    spotType = "pre"
  ),
  `facebook` = list(
    publisher = "facebook",
    channel = "display"
  ),
  `instagram` = list(
    publisher = "instagram"
  ),
  `hulu` = list(
    publisher = "hulu"
  ),
  `carryOver` = list(
    responseType = "carryOver"
  ),
  `saturation` = list(
    responseType = "saturation"
  ),
  `gross` = list(
    grossOrNet = "gross"
  ),
  `net` = list(
    grossOrNet = "net"
  ),
  `groupon_grossbookings` = list(
    kpi = "grossbookings"
  )
)}

# Find all known keywords that might show up in model. Important for error catching and future scalability
implicationKeywords <- unlist(lapply(names(keyword.implication.mappings), function (x) str_split(x, pattern = "[|]")))
subKPIstoIgnore <- c("clicks")
uniqueKPIs <- union(historical.responses$kpi, daily.responses$kpi)
dummyKeywords <- c("all")
keywordsAccountedFor <- unique(c(implicationKeywords, subKPIstoIgnore, dummyKeywords, uniqueKPIs))

# Check in case there are new keywords. We must establish additional mappings if any are not yet accounted for. TODO: Update this!!!
uniqueChannelNames <- unique(historical.responses$rawchannelname)
uniqueKeywords <- unique(Reduce(c, strsplit(uniqueChannelNames, split = "_")))
unaccountedKeywords <- setdiff(uniqueKeywords, keywordsAccountedFor)
if (length(unaccountedKeywords) > 0) {
  stop(paste0("There are keywords unaccounted for. Place the following keyword mappings in the top of r script: \n", paste(unaccountedKeywords, collapse = ", ")))
}

# Perform keyword implication mappings ----------------------------------- TODO: Figure out what to do with this...
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
