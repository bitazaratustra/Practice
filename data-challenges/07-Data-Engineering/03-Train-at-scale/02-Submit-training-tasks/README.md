## Objective

To get familiar with the `AI Platform`, we will use it in order to train a simple model for the Kaggle Taxi Fare Challenge.

This model will be a linear model **`fare_amount ~ C * distance`**.

## Reminders

### Packaging

Remember that a packaged python project is nothing more than:
- a (main) directory containing a set of directories and sub directories containing files
- having a `setup.py` file at the root (the main directory) of the project
- having a `requirements.txt` file at the root of the project listing the packages required in order for the project to function correctly
- having sub directories containing python files (`.py` files also known as modules)
- the sub directories (also known as packages) containing python files should also contain an `__init__.py` file

Having a python project packaged basically means that its code will be able to function in any context, since its `setup.py` and dependencies (`requirements.txt`, `MANIFEST.in`) formally describe how to use it.

In our case we want our packaged project to be run on the servers of the `AI Platform` in order to train our model.

### Running python files from the command line

There are several possibilites to run a `trainer.py` file in the context below:

```bash
.
└── SimpleTaxiFare
    ├── __init__.py
    └── trainer.py
```

The usual way would be to refer to the file by its path relative to our current working directory:

```bash
python SimpleTaxiFare/trainer.py
```

Please note that the preferred way is to use the modular import with the following syntax:
- replace the directory separators (usually `/`) with dots `.` and remove the trailing `.py`

👉 The modular `-m` import makes it very easy in the code to import a python module from within another python module, independently of their location in the subdirectories of the project

```bash
python -m SimpleTaxiFare.trainer
```

⚠️ Of course this assumes that the `trainer.py` contains some code outside of a function or class bootstrapping the code workflow, otherwise nothing fancy will happen. Such a code might be located for example inside of an [`ifmain` block](https://stackoverflow.com/a/419185)

## Project setup

We will start with a clean slate for these challenges. The project on which we will be working is similar to the codebase you worked with until now, but the code is organized in a different way.

First, we will copy the code for the challenges of **Train at scale** in your *projects directory*: `~/code/<user.github_nickname>`.

``` bash
cp -r ~/code/<user.github_nickname>/{{local_path_to("07-Data-Engineering/03-Train-at-scale/02-Submit-training-tasks/SimpleTaxiFare")}} ~/code/<user.github_nickname>/TFM_TrainAtScale
```

Then, we will create a local git repository for the project:

``` bash
cd ~/code/<user.github_nickname>/TFM_TrainAtScale
git init
```

Then, we will install the package so it can be imported:

``` bash
pip install -e .
```

Once this is done, make sure to update the variables in the project so that they match your Google Cloud Platform account.

In `SimpleTaxiFare/trainer.py` :
- `BUCKET_NAME`: name of a bucket in your GCP account
- `BUCKET_TRAIN_DATA_PATH`: should contain the path to an uploaded dataset in your bucket, `data/train_1k.csv` if you followed the instructions

In `Makefile`:
- `BUCKET_NAME`: name of a bucket in your GCP account

You are all set 🎉

## Have a look at the structure of the packaged project

Let's have a look at the provided packaged project structure of our code.

``` bash
.                             # packaged project directory
├── MANIFEST.in
├── Makefile                  # stores bash commands
├── SimpleTaxiFare            # package that will be deployed to the AI Platform server
│   ├── __init__.py
│   └── trainer.py            # module containing our code
├── requirements.txt          # lists dependencies to install so that the SimpleTaxiFare package runs
└── setup.py                  # used by the AI Platform in order to install and run our package
```

Have a look at the code of `trainer.py` and understand how it works.

The functions listed below are quite simple and we have implemented all of them earlier on this week.

The objective is to have a very simple code workflow that we will later run on the AI Plaform server.

``` python
def get_data():
    """ function used in order to get the training data (or a portion of it) from Cloud Storage """
    pass


def compute_distance(df):
    """ function used in order to compute a distance feature for a dataframe """
    pass


def preprocess(df):
    """ function that pre-processes the data """
    pass


def train_model(X_train, y_train):
    """ function that trains the model """
    pass


def save_model(reg):
    """ method that saves the model into a .joblib file and uploads it on Google Storage /models folder """
    pass


if __name__ == '__main__':
    """ runs a training """
```

👉 Get help from the [Cloud Storage documentation](https://pypi.org/project/google-cloud-storage/) to understand how to upload a file to a bucket through your python code

## Run the code locally

Let's verify that the code works correctly with the dataset in your GCP bucket.

We will run this code on our machine.

Let's first install the required packages:

``` bash
pip install -r requirements.txt
```

Then verify that the code runs correctly:

```bash
make run_locally
```

What did we do here?

👉 We loaded the training data stored on your GCP bucket

👉 We trained a simple model on your machine using this data

👉 We saved the trained model locally under `model.joblib`

👉 We uploaded the `model.joblib` trained model to your GCP bucket

Please verify that :
- A `model.joblib` file has been created locally
- This file has been uploaded to your bucket ([select your bucket from here](https://console.cloud.google.com/storage/browser)), in the following path: `models/simpletaxifare/model.joblib`.

This is the first step towards training online. You may not really see any difference yet, since your machine still does the hard work.

But since we retrieve the data for the training from `Cloud Storage` and store the trained model in a bucket as well, we are now able to do the training on GCP.

## Run the code on the AI Platform

Now we will launch the exact same code as before, the only difference is that the code will be executed on a GCP data center through the `AI Platform`.

GCP will:

👉 Copy our code (our package) to an AI Platform machine

👉 Install the package and its requirements thanks to `setup.py`

👉 Run a training on the AI Platform machine through the parameters passed to the `gcloud ai-platform` command in the `Makefile` (that means it will execute `python -m SimpleTaxiFare.trainer` in the cloud)

👉 We can sit back and relax, close our computer, grab a coffee and come back when the training is finished

### Verify the required versions of the packages in `requirements.txt`

One last check before we run a training.

Let's verify the versions of the python libraries that we have installed in our virtual environment:

```bash
pip freeze | grep -E "pandas|scikit|google-cloud-storage|gcsfs"
```

We need to make sure that they match with the versions listed in `requirements.txt`... Or at least if we have a conflict with the versions provided by the GCP [runtime](https://cloud.google.com/ai-platform/training/docs/runtime-version-list?hl=en) we know where to look at.

### Submit a training job to the AI Platform

Finally, let's train our packaged project on the AI Platform.

The GCP Command Line Interface (CLI) `gcloud` installed on your computer allows us to trigger actions on GCP. It provides commands allowing us to use all of its APIs.

In particular it provides a command which allows us to request the online training of the model provided in our packaged project.

Do not be scared by the command below. If you read the below explanations thoroughly, then take a look at the `Makefile`, you will see that it only provides the parameters required in order to describe the environment in which we want the code of our packaged project to run.

The `gcloud ai-platform jobs submit training` command requires:
- `JOB_NAME`: an arbitrary name allowing us to identify a training occurence, which will be visible in the [GCP console](https://console.cloud.google.com/ai-platform/jobs) once it has ran
- `BUCKET_NAME`: the bucket in which GCP will store the code of our packaged project before running it
- `BUCKET_TRAINING_FOLDER`: the bucket directory where GCP will store our packaged project used for the training. If anything goes wrong you might want to have a look at the content and verify that the zipped project contains everything you expect it to
- `PACKAGE_NAME`: the name of the package inside of our packaged project containing the code that will handle the data and train the model
- `FILENAME`: the main code file of the package for the training
- `PYTHON_VERSION`: the version of Python to be used for the training
- `RUNTIME_VERSION`: the version of the machine learning libraries provided by GCP for the training
- `REGION`: the physical region of the server on which to train (we will use the same region as the region we used for our bucket in order to reduce the latency when fetching the data)

``` bash
gcloud ai-platform jobs submit training ${JOB_NAME} \
  --job-dir gs://${BUCKET_NAME}/${BUCKET_TRAINING_FOLDER}  \
  --package-path ${PACKAGE_NAME} \
  --module-name ${PACKAGE_NAME}.${FILENAME} \
  --python-version=${PYTHON_VERSION} \
  --runtime-version=${RUNTIME_VERSION} \
  --region ${REGION} \
  --stream-logs
```

👉 [Full documentation here](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/training)

You can imagine how painful it would be to manually write this very long command every time we want to submit a training task to GCP.

That's where our precious `Makefile` comes into action with its variables and commands.

Variables:

``` bash
BUCKET_NAME=XXXXX

REGION=europe-west1

PYTHON_VERSION=3.7
FRAMEWORK=scikit-learn
RUNTIME_VERSION=1.15

PACKAGE_NAME=SimpleTaxiFare
FILENAME=trainer

JOB_NAME=taxi_fare_training_pipeline_$(shell date +'%Y%m%d_%H%M%S')
```

Fore more information about latest runtimes used by GCP, check out the [runtime documentation](https://cloud.google.com/ai-platform/training/docs/runtime-version-list?hl=en).

Once you understand how the command is ran and have filled the variables with your own GCP details, you can submit your first training job on the AI Platform:

```bash
make gcp_submit_training
```

:bulb: You can now follow the job submission on the command line (the results should be streamed until you hit `Ctrl + C`) or on the [AI Platform console](https://console.cloud.google.com/ai-platform/jobs?hl=en).

When your job is finished, have a look at your [bucket](https://console.cloud.google.com/storage/browser?hl=en) and verify that the `model.joblib` has been updated.

You just trained your first model online! 🎉

Make sure that you are comfortable with the way the `run_locally` and `gcp_submit_training` directives of the `Makefile` work and how and in which context they call `trainer.py` (ask for a TA if you need to).

Next step: we will make a prediction from that online model! 🚀
