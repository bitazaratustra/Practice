
## Setup

Let's add a `Makefile` to our project:

``` bash
cp ~/code/<user.github_nickname>/{{local_path_to("07-Data-Engineering/02-ML-Iteration/06-Kaggle-submission")}}/Makefile ~/code/<user.github_nickname>/TaxiFareModel
```

## Trained pipeline

We will now create our first Kaggle submission.

In order to do that, we will use the pipeline trained in the last challenge.

## Train on a small sample

Let's train our pipeline on 100_000 lines.

Please verify the value of the parameters inside of `trainer.py`:

```python
params = dict(nrows=100_000,            # number of samples
              local=False,              # get data from AWS
              optimize=True,
              estimator="xgboost",
              mlflow=True,              # set to True to log params to mlflow
              experiment_name=experiment,
              pipeline_memory=None,
              distance_type="manhattan",
              feateng=["distance_to_center", "direction", "distance", "time_features", "geohash"])
```

Then, we will install our package and train the pipeline:

```bash
make install run_locally
```

Wait a bit and verify that your pipeline has been saved as `model.joblib`.

You might wonder why we ran `make install` ?

**This step is important**
👉 Remember that your whole pipeline is integrated inside of your `model.joblib` file
👉 That includes the custom encoders written inside of `encoders.py`
👉 Once we have a trained pipeline, we will use it to make the predictions that we will submit to Kaggle. The quality of these predictions will determine our score
👉 When executing predictions from our loaded pipeline, the pipeline will be looking for the code of the `TimeFeaturesEncoder` and `DistanceTransformer` classes
👉 These classes are imported from the `TaxiFareModel` package
👉 So **they need to be installed as a package** with `pip install . -e`

💡 The main takeaway here is that you cannot use a trained model without the code used in order to generate it
💡 Another takeaway is that you may have trouble using a model trained with old versions of ML packages (numpy, pandas, sklearn, etc) unless you use it in a virtual environment where the same versions are installed

## Use your model to make a prediction on a Kaggle test set

We will use the `predict.py` file provided with the challenge. Copy the file to the location of your `TaxiFareModel` project.

<details>
  <summary markdown='span'><strong> 💡 Hint </strong></summary>

``` bash
cp ~/code/<user.github_nickname>/{{local_path_to("07-Data-Engineering/02-ML-Iteration/06-Kaggle-submission")}}/predict.py ~/code/<user.github_nickname>/TaxiFareModel/TaxiFareModel
```

</details>

Inspect the code inside of `predict.py` and identify the following steps:
- loading the trained pipeline from `model.joblib`
- loading a test sample from `raw_data/test.csv` (this is the test sample from Kaggle)
- applying predictions to the test set and saving the results under `predictions_test_ex.csv`

Once you are confident with the way the code works, make a prediction and store it in a Kaggle submission file. In order to do that, run:

```bash
python predict.py
```

You can now use the output CSV and [submit it to Kaggle](https://www.kaggle.com/c/new-york-city-taxi-fare-prediction/submit)

You might need to login to Kaggle or register [here](https://www.kaggle.com/account/login) if you do not already have an account.

## Train on a bigger sample

Now that your first submission is done, you may want to train on a bigger sample and see how your score evolves.

To do so, modify the parameters used in order to train the model and use 1 000 000 lines. You only need to set `n_rows=1_000_000` inside of `trainer.py`.

Then again:

```bash
make run_locally
```

## Bonus: install the Kaggle CLI in order to automate the submissions

- login to Kaggle
- install the CLI:

``` python
pip install kaggle
```

- get a token following the instructions [here](https://github.com/Kaggle/kaggle-api#api-credentials)
👉 summarized steps : on [Kaggle[(https://www.kaggle.com)], click on _My Account_, then _Create New API Token_. The token should be saved under `~/.kaggle/kaggle.json` (or `C:\Users\<Windows-username>\.kaggle\kaggle.json` for Windows users)

- test the installation

``` python
kaggle competitions list
```
