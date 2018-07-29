import pandas as pd
import numpy as np
from xgboost import *
from models.utils import *
import sklearn
import os
import pickle

pulled_data = pd.read_csv('./modeling_data3.csv', index_col=0)
#apply_to_df(pulled_data, lambda x: parse_digit(x, caster=int), columns=["bom_Theater Change"]) # TODO: THIS SHOULD BE UNECESSARY???
pulled_data = pulled_data.drop(['bom_title', 'bom_Total Gross', 'tmdb_id', 'tmdb_title'], 1)


xgb_data = DMatrix(
    data=pulled_data.drop(['bom_Weekend Gross'], axis = 1),
    label=pulled_data['bom_Weekend Gross'],
    silent=False,
    feature_names=list(pulled_data.columns)[1:]
)

model = cv(
    params={
        'objective': 'reg:linear',
        'eta': 0.35,
        'max_depth': 20,
    },
    dtrain=xgb_data,
    num_boost_round=50,
    nfold=4,
    as_pandas=True,
    verbose_eval=True,
    shuffle=True
)

test_percentage = .05
random_seed = 0
rs = np.random.RandomState(random_seed)
num_rows = pulled_data.shape[0]
num_test_rows = int(num_rows * test_percentage)
rows = range(0, num_rows)
test_rows = rs.choice(rows, num_test_rows, replace=False)
train_rows = set(rows) - set(test_rows)

train = pulled_data.loc[train_rows, :]
train_y = train['bom_Weekend Gross']
train_x = train.drop(['bom_Weekend Gross'], axis=1)
test = pulled_data.loc[test_rows, :]
test_y = test['bom_Weekend Gross']
test_x = test.drop(['bom_Weekend Gross'], axis=1)

model = XGBRegressor(n_estimators=100, max_depth=10)
model.fit(train_x, train_y)

test_y_pred = model.predict(test_x)

residuals = [a - p for a, p in zip(test_y, test_y_pred)]


x = 2
