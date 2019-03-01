##REMOVEABLE IDEAS:
# Genres
# Weekend # (not Week #)
# Re-issues (see data aggregation)
# Missing weeks (see data aggregation)
library(xgboost)
library(data.table)
library(ggplot2)
library(dplyr)
library(plyr)

ape <- function (o, p) {
  ape <- abs((o-p)/o)
  ape <- ape[!(is.na(ape) | is.infinite(ape))]
  ape * 100
}

median.ape <- function(preds, dtrain) {
  labels <- getinfo(dtrain, "label")
  err <- median(ape(preds, labels))
  return(list(metric = "median.ape", value = err))
}
mean.ape <- function(preds, dtrain) {
  labels <- getinfo(dtrain, "label")
  err <- mean(ape(preds, labels))
  return(list(metric = "mean.ape", value = err))
}


modeling.dt = as.data.table(read.csv("./models/modeling_data3.csv"))
# Clean data, rowwise
#lapply(modeling.dt, summary)
modeling.dt <- modeling.dt[bom_Week.. > 0] # We will not need to train on negative weeks. 0 weeks seem to correspond to pre-release or super irrelevant movies.
modeling.dt <- modeling.dt[difftime(Sys.time(), as.Date(paste0(bom_year, "-01-01")), "weeks") >= bom_Week..]
modeling.dt <- modeling.dt[bom_LW.Total.Gross >= 0] # This should not be negative. This would imply missing data for some week that never got tabulated into the total gross
modeling.dt <- modeling.dt[!grepl('re-issue', bom_title, ignore.case = T)] # REMOVEABLE (Doesn't seem to affect model. probably do not need.): Not a re-issue. May be able to train on this, but should probably add a feature if so. Likely won't help for future predictions either...
modeling.dt <- modeling.dt[is.na(bom_Theater.Change) & bom_Week.. > 1, bom_Theater.Change := 0] # TESTABLE: Might want to physically cleanse this data by performing theater change operation. The data seems good though!
modeling.dt <- modeling.dt[is.na(bom_Theater.Count), bom_Theater.Count := 0]
modeling.dt <- modeling.dt[, tmdb_belongs_to_collection := as.numeric(tmdb_belongs_to_collection)]
modeling.dt <- modeling.dt[tmdb_budget == 0, tmdb_budget := NA]
modeling.dt <- modeling.dt[tmdb_vote_average == 0, tmdb_vote_average := NA]

modeling.dt <- modeling.dt[abs(bom_year - tmdb_release_year) <= 2]
modeling.dt <- modeling.dt[bom_Weekend.Gross > 500000]

#BOM.dt <- BOM.dt[!(is.na(`LW`) & `Week #` > 1)] # REMOVEABLE: LW metric seems to be noisy if a movie leaves theaters for a few weeks. might be a bad metric, because this happens often. Can either do this and lose 10% of data or just remove the feature
# Clean data, columnwise
modeling.dt = modeling.dt[ , -c("X", "bom_title", "tmdb_title", "bom_Total.Gross", "tmdb_id"), with=F]
#modeling.dt = modeling.dt[, .(bom_Weekend.Gross, bom_Theater.Count, bom_LW.Ranking, bom_Theater.Change, bom_LW.Total.Gross, tmdb_vote_average, tmdb_runtime, tmdb_popularity, bom_Week..)]

#Transform data
modeling.dt <- modeling.dt[
  , bom_LW.Ranking := bom_LW.Ranking ^ -1
][
  , bom_Week.. := bom_Week.. ^ -1
]


#Inspect data
plot.points <- function(x, y, n = "Plot") {
  ggplot(mapping = aes(x = x, y = y)) + 
    labs(title = n) + 
    geom_point(size = 0.01)
}
lapply(modeling.dt, summary)
#lapply(names(modeling.dt), function(n) hist(modeling.dt[[n]], main = n))
plots <- lapply(names(modeling.dt), function(n) plot.points(modeling.dt[[n]], modeling.dt$bom_Weekend.Gross, n))
names(plots) <- names(modeling.dt)

# XGBOOST----
# gs constants
train_X = as.matrix(modeling.dt[, -"bom_Weekend.Gross"])
train_y = as.matrix(modeling.dt[, bom_Weekend.Gross])
dtrain = xgb.DMatrix(
  data = train_X,
  label = train_y
)
train.objective = "reg:linear"
# gs variants
eta = 0.03 #seq(from = 0.005, to = 0.08, by = 0.005)
max.depth = 11
subsample = 1 
params = expand.grid(
  eta = eta,
  max.depth = max.depth,
  subsample = subsample
)

# perform gs
gs.results = list()
for (row in 1:nrow(params)) {
  p = params[row, ]
  cat("Testing params:\n")
  print(p)
  cv.results <- with(p, xgb.cv(
    params = list(
      objective = objective,
      eta = eta,
      max.depth = max.depth,
      subsample = subsample
    ),
    data = dtrain,
    nrounds = 5000,
    nfold = 4,
    prediction = T,
    showsd = T,
    feval = mean.ape,
    early_stopping_rounds = 40,
    maximize = F
  ))
  gs.results[[row]] <- cv.results
}
gs.mins <- lapply(gs.results, function (x) {
  r = x$evaluation_log[x$best_iteration, ]
  r[, "nrounds"] <- x$best_iteration
  r
})
gs.min.df <- do.call(rbind.fill, args = gs.mins)
params.and.results <- cbind(gs.min.df, params)
min.params <- which(gs.min.df[[4]] == min(gs.min.df[[4]]))
best_params <- c(gs.min.df[min.params, ], params[min.params, ])

xgb <- with(best_params, xgb.train(
  params = list(
    objective = objective,
    eta = eta,
    max.depth = max.depth,
    subsample = subsample
  ),
  data = dtrain,
  nrounds = nrounds,
  feval = mean.ape,
  verbose = 2
))
importance <- xgb.importance(feature_names = colnames(dtrain), model = xgb)
importance

y_pred <- predict(xgb, train_X)
apes = ape(train_y, y_pred)
hist(apes)

#OLD METHOD
if (F) {
  
  # Split train and test data
  set.seed(42)
  test.percentage = 0.05
  test.size = floor(nrow(modeling.dt) * test.percentage)
  all.rows = 1:nrow(modeling.dt)
  test.rows = sample(all.rows, size = test.size)
  
  test = modeling.dt[test.rows, ]
  test_X = as.matrix(test[, -1])
  test_y_actual = test$bom_Weekend.Gross
  
  train = modeling.dt[-test.rows, ]
  train_X = as.matrix(train[, -1])
  train_y = train$bom_Weekend.Gross
  
  xgb <- xgboost(
    data = train_X,
    label = train_y,
    objective = "reg:linear",
    eta = 0.35,
    max.depth = 20,
    nround = 30
  )
  
  test_y_pred <- predict(xgb, test_X)
  pred.dt <- data.table(test_X)
  pred.dt[["actual_y"]] <- test_y_actual
  pred.dt[["pred_y"]] <- test_y_pred
  pred.dt[["residuals"]] <- test_y_actual - test_y_pred
  pred.dt[["abs.residuals"]] <- abs(test_y_actual - test_y_pred)
  pred.dt[["APE"]] <- ape(test_y_actual, test_y_pred)
  xgb_rmse = rmse(test_y_actual, test_y_pred)
  median(xgb_ape)
  mean(xgb_ape)
  
  importance <- xgb.importance(feature_names = colnames(train_X), model = xgb)
  importance
}