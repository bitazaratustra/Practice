
**The goal of today's recap is to train a package in Google AI Platform**

## Setup & Configuration

<details>
  <summary markdown='span'><strong> ⚙ Prerequisites </strong></summary>


In order to work on this recap you need to have a configured GCP account.

You need to fetch your project name from the [GCP console](https://console.cloud.google.com/).

👉 In the code of the solution, the name of the project is `le-wagon-data`

You also need to retrieve the name of your bucket from [Cloud Storage](https://console.cloud.google.com/storage/).

👉 In the code of the solution, the name of the bucket is `le-wagon-data`

The bucket must contain a `data` directory containing a [train_1k.csv](https://wagon-public-datasets.s3.amazonaws.com/taxi-fare-ny/train_1k.csv) data file containing 1_000 rows.

👉 You may use any other path in the bucket (`data/train_1k.csv`) and update the code of the solution accordingly

</details>

We will be working on the package from the previous recap. You can download the solution for the previous recap from Kitt in `07-Data-Engineering/02-ML-Iteration/Recap` 👌

<details>
  <summary markdown='span'><strong> How to move it to projects repository </strong></summary>


``` bash
mv downloaded_solution_package ~/code/<user.github_nickname>/taxifare_trainatscale
cd ~/code/<user.github_nickname>/taxifare_trainatscale
```

</details>

👉 Let's open our package in order to edit our code:


```bash
code .
```

👉 Open **another terminal window** for the notebooks. We will use the first terminal window in order to add and commit the code of our package as it evolves using `git` commands

``` bash
cd ~/code/<user.github_nickname>/{{local_path_to("07-Data-Engineering/03-Train-at-scale/Recap")}}
jupyter notebook
```

👉 `gcp boilerplate.ipynb` contains the code that allows to download data from and upload data to Cloud Storage as well as train our model in the AI Platform.

Now that the jupyter server containing the notebooks with the code boilerplate is started, we will only use the first terminal window for our commands.

You are now ready to 🎉

<details>
  <summary markdown='span'><strong> Configuration </strong></summary>


Make sure that your replace in the code that you copy from the notebook:
- The name of the project
- The name of the bucket
- The path to the `train_1k.csv` file inside of the bucket

</details>

Let's go inside of the project (you should be located in the same directory as the `Makefile`).

``` bash
cd taxifare
```

Let's run the solution locally:

``` bash
python -m taxifare.trainer
```

Nothing seems to be happening 🤔

<details>
  <summary markdown='span'><strong> Solution </strong></summary>


That is because in the previous recap we were importing our package in a usage notebook, in which we were instantiating our `Trainer` class.

Now, we want to be able to use our package out of the box.

👉 Let's add an `ifmain` block to our trainer in order to have our package able to train from a call from the command line. This will come in handy when we push our package later to the AI Platform.

``` python
def main():

    trainer = Trainer()
    trainer.train()


if __name__ == '__main__':
    main()
```

Now run our package again:

``` bash
python -m taxifare.trainer
```

👉 You should see a `model.joblib` file having just been created and containing our trained model.

</details>

In order to be able to run our code in the AI Plaform, we need to modify 2 things:
- We need to fetch the data from Cloud Storage rather than locally
- We need to push our trained model to Cloud Storage rather than store it locally

👉 Remember that the AI Platform instance that will be running our code will be shutdown and recycled once its job is over. We had better push our trained model to Cloud Storage if we want to be able to use it later


## Train from data in Cloud Storage

Let's update the `get_data` function in `data.py` so that it downloads the data from Cloud Storage when training.

The code is available in the **gcp boilerplate.ipynb** notebook.
<details>
  <summary markdown='span'><strong> Solution </strong></summary>


You have 2 options here:
- Either use the `get_data_using_blob` function, which downloads the file locally as `train_1k.csv` before loading the DataFrame
- Or use `get_data_using_pandas` function, which only downloads the requested number of rows from the CSV in Cloud Storage in order to create a DataFrame

`get_data_using_blob`:
- *Pros*: just to have a look at the code allowing to download any file from Cloud Storage
- *Cons*: not very efficient to download the full CSV file (especially if it is huge) if you only want to train on a small number of rows

`get_data_using_pandas`:
- *Pros*: allows to read a given number of lines from a CSV file
- *Cons*: does not download the file locally

If you use `get_data_using_blob`, **remember** to update the name of the bucket and the path to the `train_1k.csv` file. You should see the file downloaded locally when running `ls -la`.

If you use `get_data_using_pandas`, **remember** to update the name of the bucket and the path to the `train_1k.csv` file in the URL since the one provided in the notebook (`gs://le-wagon-data/data/train_1k.csv`) is not publicly available. You may update and print the number of rows in the DataFrame in order to make sure that it works as intended (remember the source CSV file contains 1_000 lines).

</details>

Let's train our model:

``` bash
python -m taxifare.trainer
```

👉 Whatever method you choose, you should still be able to train your model and see an updated `model.joblib` file with an update timestamp visible when running `ls -la`

## Save the trained model to Cloud Storage

Now that we are able to train from data in Cloud Storage, either by downloading it using a blob, or through retrieving only a given number of lines, the next step is to push our model to Cloud Storage once it is trained.

Let's add some code in `data.py` allowing us to push our model to Cloud Storage.

<details>
  <summary markdown='span'><strong> Solution </strong></summary>


The `save_model_to_gcp` function is available in the **gcp boilerplate.ipynb** notebook.

**Remember** to update the name of your bucket in the code as well as the path in the bucket in which the model will be stored.

</details>

Now, let's update our `Trainer` so that the model is saved once it is trained.

Let's train our model:

``` bash
python -m taxifare.trainer
```

Once your model is trained, you should be able to see it in Cloud Storage...

👉 Either through the `gsutil` command:

``` bash
gsutil ls -la gs://le-wagon-data/models/  # update the command according to your bucket name and model storage path
```

👉 Or by browsing your bucket in the [Cloud Storage console](https://console.cloud.google.com/storage/) and going inside of your bucket and following the storage path for your model defined in your code

## Train in the AI Platform

Now that our code is able to train from data in Cloud Storage and to save our trained model in Cloud Storage, there is no reason to train our code on our own machine anymore...

Let's add a directive in our `Makefile` in order to train our model in the AI Platform...

<details>
  <summary markdown='span'><strong> Solution </strong></summary>


The code for the `Makefile` is available in the **gcp boilerplate.ipynb** notebook.

**Remember** to update in the `Makefile` the environment variables for:
- The name of your bucket
- The name of the training directory (used by the AI Platform in order to store the package that will be trained)
- Optionally change the region, the version of python, and the version of the runtime
- Adapt the name of the package and of the module if you changed them

If you wish to see where the code of the package is stored in the bucket by the AI Platform, you should clear the content of the training directory in the bucket before submitting a training. This way it will be easier to identify the storage location of the package.

Also, we need to update our `MANIFEST.in` so that the subpackages in our package are correctly uploaded to the AI Platform (code available in the notebook):
- The `graft` instructions allows to upload everything inside of the package to the AI Platform (in particular, we want our `taxifare/transformers` package to be correctly uploaded)
- The `global-exclude` instruction prevents us from uploading `__pycache__` files that are not required to the AI Platform

Optionally, you may add a few `print()` statements in your code in order to see how the model training unfolds. These will end up in the logs of the AI Platform and will allow you to see whether your model trained correctly.

</details>

Your can now submit a training to the AI Platform:

``` bash
make gcp_submit_training
```
<details>
  <summary markdown='span'><strong> Are all the variables filled in correctly? </strong></summary>


You may have a look at the command that is generated by the `Makefile` in order to verify that all the environment variables are correctly filled:

👉 The directive of the `Makefile` should output something similar to this:

``` bash
gcloud ai-platform jobs submit training taxi_fare_training_20210223_175010 \
    --job-dir gs://le-wagon-data/trainings \
    --package-path taxifare \
    --module-name taxifare.trainer \
    --python-version=3.7 \
    --runtime-version=2.2 \
    --region europe-west1 \
    --stream-logs
```

</details>

You may cancel the streaming of the logs in the console at anytime by pressing `Ctrl + C`.

You should now be able to connect to the [AI Platform console](https://console.cloud.google.com/ai-platform/) in order to see your job running.

<details>
  <summary markdown='span'><strong> What should I check on AI Platform? </strong></summary>


In the console, you may want to have a look at:

👉 In **Jobs**, you should see your job being prepared and eventually training (this can be pretty long)

Click on it, then **View Logs** in order to assess what is currently happening.

👉 You will find in the logs any python error that occurs when training your code, such as missing packages not being able to be imported, or any other code error

The training is pretty long... Before coming back here in order to have a look at the trained model, you may move on with the next part of this recap.

Once the job is complete, you should find a trained model saved in your bucket. Have a look at it either using `gsutil` or through the console...

👉 Optionally, you may want to have a look at the content of the package stored in your bucket in the trainings directory once a job has been submitted (download it and extract it) in order to see how it differs from your local package, which files are uploaded and which are not

</details>

## Optional: go through the TaxiFare Deep Learning notebook in Colab

Go to the challenge and follow the instructions in order to open in Google Colab a notebook containing a **Deep Learning** model training for the TaxiFare challenge.

``` bash
cd ~/code/<user.github_nickname>/{{local_path_to("07-Data-Engineering/03-Train-at-scale/06-Google-Colab")}}
```
