## Iterate with MLflow

Before carrying on, make sure that you understood:
- The structure of the `Trainer` class from the first challenge
- The way to log a metric and a parameter on a hosted MLflow server such as https://mlflow.lewagon.ai/
- How to pass multiple keyword argument parameters to a function or method using `**kwargs` and how to access them in the function or method

If any of these is unclear, ask for a TA.

In order to iterate, we will need a few packages:

``` bash
pip install category-encoders memoized-property psutil xgboost pygeohash
```

We are going to modify the `trainer.py` in order to push the training parameters and metrics to **MLflow**.

Please add the following method to your trainer (and fill its content):

``` python
    def save_model(self):
        """ Save the trained model into a model.joblib file """
        pass
```

Do not forget to add and import for the `joblib` package and to call the `save_model` method in your `ifmain` block of code (`if __name__ == "__main__":`)

👉 We will call the `save_model` method in order to push data to MLflow, keep it in mind for later
👉 Once you're happy about your final model, you can submit your best model's predictions to Kaggle

Last thing, we suggested a package structure to organize your code and your run, feel free to reorganize it as you wish.

## Set a name for your experiment

As you saw in the previous challenges, it can be pretty hard to identify where your results are stored in a shared hosted MLflow server.

In order to solve this, name your experiment inside of `trainer.py` according to this naming convention:
``` python
experiment = "[country code] [city] [login] model name + version"  # 🚨 replace with your country code, city, github_nickname and model name and version
```

Now that you are all set, have a go at as many runs as you wish for your experiment and try to increase the performance of your model:
- Try other estimators
- Work on feature engineering and selection

## Try different estimators

- Think about the different estimators that you know and that could be used in order to solve prediction problems
- Implement a short script that will loop through the estimators, train the pipeline and evaluate it on a validation set

👉 In order to do that, you might need to tweak the `TaxiFareModel` package

⚠️ Make sure you **cross validate** your trainings

View the results on https://mlflow.lewagon.ai/

And as always, while building the pipeline and updating the code, first train your models on small data samples in order to iterate quickly on code errors, and preferably on your own machine.

Then once your modified code is all set, you can play with the big datasets and train your pipeline in the cloud.

## 2. Features engineering and selection

**Now is the time to be creative!**

You have just tried several estimators and saw that some perform better than others. Another area where you can search for performance is feature engineering.

- Try different combinations of features (by removing or adding features) and track the runs

👉 Play with `direction`, `manhattan distance`, `euclidian distance`, `geohash`

- Use some context knowledge in order to generate new features that you think might be explaining the fare amounts

👉 We may suppose that taxis apply a fixed amount for airport transfers

- Try various methods for outliers removals

- Look at how the size of a training set helps reducing the RMSE on the validation set

## Suggested method used in order to track the influence of feature engineering

Use the benefits of pipelines integrated into our custom class.

We will start with one additional feature: `distance_to_center`:
- Get back to the `{{local_path_to("07-Data-Engineering/02-ML-Iteration/01-Kaggle-Taxi-Fare")}}` notebook with complete feature engineering
- Implement a custom transformer inside of `encoders.py` called `DistanceToCenter` which adds the `distance_to_center` feature
- Adapt the `set_pipeline` method inside our main `Trainer` class so that it integrates this new block
- Modify the parameters fed to our `Trainer` class in order to easily execute 2 runs to compare the influence of the added feature
- Launch 2 new runs and check the influence of the `distance_to_center` feature

Once you've added the new feature, add as many features as you want and analyse the impact on the performances of the trained pipeline

Bonus: use a [PolynomialFeatures](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html) transfomer to generate new features from distance...
