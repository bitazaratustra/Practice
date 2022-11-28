# Hyperparameters tuning
Finally, once you are satisfied with your features engineering work, **let's fine tune your model.**

For this, we recommend you choosing a `Gradient Boosting Tree` estimator ([Xgboost](https://xgboost.readthedocs.io/en/latest/get_started.html) or [LightGBM](https://lightgbm.readthedocs.io/en/latest/) or [GradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html)).

The idea is to tune the hyperparameters of this estimator. The most important parameters to tune are:
- `learning_rate`
- `max_depth`
- `n_estimators`

# Prerequisite
Please keep in mind that the `save_model` method saves locally your model under the `model.joblib` file.

You may want to upload to **Google Cloud Storage** the different trained models in separate bucket directories in order to save them. In order to do that, you may have a look at the content of the `gcp.py` file.

You will later load your best performing model to submit your predictions to Kaggle.


# Reminder on Hyperparameter tuning
To perform hyperparameters search, you have the choice between three `search` mechanisms:
- [GridSearch](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html)
👉 Run all pipeline for each parameter combination
➕ Exaustive
➖ Very slow on large datasets
- [RandomSearch](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html)
👉 Run pipeline for a random subset of parameter combinations
➕ Faster than Gridsearch for large dataset
➖ Not exhaustive, might not find optimal parameter combination
- [Hyperopt](http://hyperopt.github.io/hyperopt/)
👉 Bayesian optimization technique that uses information from past trials to inform the next set of hyperparameters to explore
➕ Faster than Gridsearch
➕ Exhaustive and going through all parameter space
➕ Often leading to better results


## Useful links
- [XGboost hyperparameters](https://xgboost.readthedocs.io/en/latest/parameter.html)

#### Exercise
- First, try to adjust the hyperparameters manually and do a few runs that you can track with MLFlow. Then [with MLFlow UI you can visually see how these parameters affect the performance metric](https://mlflow.org/docs/latest/tracking.html#visualizing-metrics).
- Once you have an idea of how the parameters impact RMSE, try to implement both  `RandomSearch` as part of your pipeline to fully tune the model.

## Final Step
Once you are satisfied with your tuned model, keep preciously your last `model.joblib`, and you can submit your new submissions on kaggle
