# imports
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV


class Models:
    '''
    Build an object to process varied models and stow results
    '''

    def __init__(self, X_train, X_test, y_train, y_test):
        '''
        initialize Models object

        params
        ======
        X_train (pandas.core.frame.DataFrame): dataframe of features to train on
        X_test (pandas.core.frame.DataFrame): dataframe of features to test on
        y_train (pandas.core.series.Series): series of target to train on
        y_test (pandas.core.series.Series): series of target to test on

        attrs
        =====
        results_df (pandas.core.frame.DataFrame): empty dataframe to stow 
            testing results
        best_models (list): stows the model with the best hyperparams

        returns
        =======
        None
        '''
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test

        self.results_df = pd.DataFrame(
            columns=['model', 'params', 'r2', 'mse'])
        self.best_models = []

    def build_grid_search(self, model, params):
        '''
        build GridSearchCV object

        params
        ======
        model (class): the type of sklearn model to be employed
        params (dict): contains the hyperparameter names as keys and
            hyperparameters as values

        attrs
        =====
        None

        returns
        =======
        gs (sklearn.model_selection._search.GridSearchCV): object ready to
            iteratively identify the ideal model
        '''
        return GridSearchCV(model, params, n_jobs=-1,
                            scoring='r2', verbose=True)

    def fit_model(self, model, params):
        '''
        fits the model from training data

        params
        ======
        model (class): the type of sklearn model to be employed
        params (dict): contains the hyperparameter names as keys and
            hyperparameters as values

        attrs
        =====
        None

        returns
        =======
        best_gs (sklearn.model_selection._search.GridSearchCV): the model that
            had the highest R2 score
        '''
        gs = self.build_grid_search(model, params)
        print(gs.estimator)
        gs = gs.fit(self.X_train, self.y_train)
        best_gs = gs.best_estimator_

        self.best_models.append(best_gs)

        return best_gs

    def eval_model(self, model, params):
        '''
        evalates the model on the testing data

        params
        ======
        model (class): the type of sklearn model to be employed
        params (dict): contains the hyperparameter names as keys and
            hyperparameters as values

        attrs
        =====
        None

        returns
        =======
        None
        '''
        best_gs = self.fit_model(model, params)

        y_pred = best_gs.predict(self.X_test)
        r2 = r2_score(y_pred, self.y_test)
        mse = mean_squared_error(y_pred, self.y_test)

        model_name = str(model.__class__)
        model_name = model_name.split('.')[-1].split("'")[0]

        best_params = best_gs.get_params()

        # create and add result to results_df
        row = [model_name, best_params, r2, mse]
        self.results_df.loc[len(self.results_df)] = row

        print('\n')
