# Outline day 3
Again here, quite a dense day, don't be discouraged if you don't go through the end

**Every one should get to exercise 5 at 16:00 even if first exercises are not finished**

## 01-Notebook-to-package
- Creation of a minimal package structure to get rid of the notebook
- Learn how to test individually each module in order to work faster
- Implementation of `Trainer()` class, central point of our package


##  02-MlFlow-quickstart
- Install and run first mlflow ui
- Run first simple experiment to log parameters
- Log parameters and metrics on remote Mlflow instance


## 03-Iterate-with-Mlflow
Exercise mainly about tweeking `Trainer()` class to make it as generic as possible
- Implement more feature engineering Pipeline blocs
- Integrate them in main `Trainer()` class
- Check influence of feature engineering thanks to Mlflow


## 04-HyperparameterTuning
Here first aprehension of Hyperparameter Tuning
- First play manually with a few parameters of xgboost and check influence
- Then integrate `RandomizedSearchCV` into `Trainer()` class for full tuning
- logs output to Mlflow


## 05-Kaggle-submission
Now that we have good feature Engineering and Hyperparameter tuning we can submit a first respectable submission to kaggle
- Either manually
- Or via kaggle cli
