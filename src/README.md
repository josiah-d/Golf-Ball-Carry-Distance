# Running the Models

**Note:** The docstrings are relatively complete and should be easy to follow.

## Cleaning the Data

`clean_json.py` contains a class that grabs all file paths, segments the
relevant data, and turns them into a `.csv`. It uses `data_to_csv.py` as the
action file that calls `CleanJSON`, utilizes its methods, performs some minor,
and data cleaning.

## Exploratory Data Analysis

`eda.ipynb` loads the `master.csv` data file to build and save various plots to
the `img` directory. The heavy lifting is being done by `plot.py` which contains
numerous functions to create various plots.

## Model Building & Evaluation

`model.py` contains a class that builds, fits, predicts, and evaluates various
models. The models are all passed through `GridSearchCV` and this class is rather
agnostic to the bodel being use (so long as it is from
[SKLearn](https://scikit-learn.org/stable/index.html)). Each of the models is
stowed with that class with the properly tuned hyperparameters for additional
use/exploration.

`run_models.ipynb` creates an instance of `Models`. The class is passed the
desired model and the hyperparameters to be grid search.

Example of the best performing model

```python
xgb_params = {'max_depth': [3, 7, 9, 15],
              'subsample': [0.01, 0.1, 0.5, 0.9, 0.99],
              'colsample_bytree': [0.01, 0.1, 0.5, 0.9, 0.99],
              'n_estimators': [10, 100, 1000, 10000]}

models.eval_model(model=xgb.XGBRegressor(objective='reg:squarederror'),
                  params=xgb_param)
```

Lastly (and a bit sloppy), `run_models.ipynb` makes a quick plot of the feature
importances and stows it in the `img` directory.
