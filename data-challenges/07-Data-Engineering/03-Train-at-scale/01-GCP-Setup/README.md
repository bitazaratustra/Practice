# Objective

In this series of exercises, you will learn how to deploy your code to [Google Cloud Platform](https://cloud.google.com/) aka **GCP** and in particular how to use **[AI Platform](https://cloud.google.com/ai-platform/)** in order to leverage the power of distributed computing and speedup your ML experimentation.

Beyond training models, you will see how you can make your models available to the world, manage different versions and serve predictions at scale.

<details>
  <summary> 🚨 If you are a student of the <strong>Part-Time Bootcamp</strong>, go back to the setup to create a GCP account now </summary>


👉 Go to the **Google Cloud Platform setup** section of the `data-setup` repo:
- [macOSX](https://github.com/lewagon/data-setup/blob/master/macOS.md#google-cloud-platform-setup)
- [Ubuntu/WSL2](https://github.com/lewagon/data-setup/blob/master/LINUX.md#google-cloud-platform-setup)

</details>

# Google Cloud Platform services

Now that you have a working setup, we are going to start using the products provided by the GCP platform.

GCP provides tens of products, but we will be interested mainly in three products:
- `Cloud Storage` allows to store data in the cloud. We will use it in order to store our datasets and our trained models
- `AI Platform` allows to train models in the cloud. We will use it in order to train our models
- `Cloud Run` allows to run containerized applications in the cloud. We will use it in order to host our API

In order to navigate quickly in GCP, you should scroll through the list of products in the left pane and maybe pin the most used ones (using the pin icon).

## Bucket setup

`Cloud Storage` provides the capability of hosting files online in storage locations called `buckets`.

You can consider that the bucket is like a disk or flash drive that would be accessible anywhere in the world, and is identified by a `BUCKET_NAME`. Inside the bucket, you can organize your data in directories (folders) and subdirectories as you would any disk or flash drive.

Contrary to a disk or drive, you do not need to create intermediate directories before writing a file because `Cloud Storage` uses a [[flat hierarchical structure]](https://cloud.google.com/storage/docs/gsutil/addlhelp/HowSubdirectoriesWork).

For now, lets play with the `buckets` in order to make sure that everything works.

You will need a bucket to store data, code and trained models.

⚠️ **IMPORTANT**: Bucket names must be **globally unique** since they are accessible worldwide. Please respect the naming convention `wagon-data-[BATCH_NUMBER]-[YOUR_LAST_NAME]`

In the same way as the `PROJECT_ID` is used in your code in order to identify your project, the `BUCKET_NAME` is used in your code in order to identify an online storage location where you store your data and your models.

You can list the buckets of your project in [Navigation menu / Storage / Browser](https://console.cloud.google.com/storage/browser).

💡 Let's use the `train_1k.csv` training file in order to test the upload and the model training quickly. Eventually you are going to want to upload the full dataset in order to create a better model.

First, we will download the `train_1k.csv` file:

``` bash
curl --silent 'https://wagon-public-datasets.s3.amazonaws.com/taxi-fare-ny/train_1k.csv' > ~/code/<user.github_nickname>/TaxiFareModel/raw_data/train_1k.csv
```

❓ You will need to reference the location of the file in your code, how to find the local path to `train_1k.csv`?

<details>
  <summary markdown='span'><strong> 💡 Hint </strong></summary>

From your terminal, go to the TaxiFareModel project that you created:

``` bash
cd ~/code/<user.github_nickname>/TaxiFareModel
```

From there, go to the `raw_data` directory. You should see the [train_1k.csv](https://wagon-public-datasets.s3.amazonaws.com/taxi-fare-ny/train_1k.csv) file inside.

In order to reference it, print the local path with `pwd`.

</details>
<br>

There are 2 ways to create a bucket:

### The hacker's way (**recommended**)

- Open `Makefile` in your `TaxiFareModel` project and copy the following lines.

``` bash
# project id - replace with your GCP project id
PROJECT_ID=XXX

# bucket name - replace with your GCP bucket name
BUCKET_NAME=XXX

# choose your region from https://cloud.google.com/storage/docs/locations#available_locations
REGION=europe-west1

set_project:
    @gcloud config set project ${PROJECT_ID}

create_bucket:
    @gsutil mb -l ${REGION} -p ${PROJECT_ID} gs://${BUCKET_NAME}
```

We need to fix the indentations as you copied the code with __spaces__ and we need to replace them with __tabs__. If you do not do it you will probably see an error about `missing separator` while running the commands. If you cannot figure it out yourself, ask for a TA.

- Use the predefined bash commands from `Makefile` to create your bucket

```bash
make set_project
make create_bucket
```

👉 Check on [Storage](https://console.cloud.google.com/storage) that your bucket has been created.

### The UI way (alternative)

- Go to [Storage](https://console.cloud.google.com/storage) and create a bucket from there
- Select `Location type`: `Region` since we will not need to access our bucket from all over the world
- Buckets should be created in the nearest region (`europe-west1` for France)
- Keep other options default

## Upload your dataset

- Add the following lines to your `Makefile` (do not forget about the indentation)

``` bash
# path to the file to upload to GCP (the path to the file should be absolute or should match the directory where the make command is ran)
# replace with your local path to the `train_1k.csv` and make sure to put the path between quotes
LOCAL_PATH="XXX"

# bucket directory in which to store the uploaded file (`data` is an arbitrary name that we choose to use)
BUCKET_FOLDER=data

# name for the uploaded file inside of the bucket (we choose not to rename the file that we upload)
BUCKET_FILE_NAME=$(shell basename ${LOCAL_PATH})

upload_data:
    # @gsutil cp train_1k.csv gs://wagon-ml-my-bucket-name/data/train_1k.csv
    @gsutil cp ${LOCAL_PATH} gs://${BUCKET_NAME}/${BUCKET_FOLDER}/${BUCKET_FILE_NAME}
```

- Finally use the predefined bash command from `Makefile` to upload your file

```bash
make upload_data
```

👉 Check on [Storage](https://console.cloud.google.com/storage) that your file was correctly uploaded. You should see a `train_1k.csv` file in the `data` folder of your bucket. Look at the content of the `Makefile`. You can see how the command used in order to upload the file was built

🚀 Congrats!
