
**The goal of today's recap is to create an API and push it to production in Cloud Run so that anyone on the Internet can use it**

## Setup

<details>
  <summary markdown='span'><strong> Prerequisites </strong></summary>

  In order to work on this recap you need to have a configured GCP account.

  👉 Container Registry API must be enabled

  👉 Cloud Run API must be enabled

</details>

We will be working on the package from the previous recap. You can download the solution for the previous recap from Kitt in `07-Data-Engineering/03-Train-at-scale/Recap` 👌

<details>
  <summary markdown='span'><strong> How to move it to projects respository? </strong></summary>

  ``` bash
  mv downloaded_solution_package ~/code/<user.github_nickname>/taxifare_predictinprod
  cd ~/code/<user.github_nickname>/taxifare_predictinprod
  ```
</details>

Let's open our package in order to edit our code:

```bash
code .
```

👉 Open **another terminal window** for the notebooks. We will use the first terminal window in order to add and commit the code of our package as it evolves using `git` commands

``` bash
cd ~/code/<user.github_nickname>/{{local_path_to("07-Data-Engineering/04-Predict-in-production/Recap")}}
jupyter notebook
```

👉 `api_boilerplate.ipynb` contains the code that allows to create an API_with `FastAPI`

👉 `api_usage.ipynb` contains the code that allows to test our API locally and in Cloud Run

Now that the jupyter server containing the notebooks with the code boilerplate is started, we will only use the first terminal window for our commands.

You are now ready to 🎉

## Create an API for our model

Using **FastAPI**, let's create an API for the model trained by the package.

<details>
  <summary markdown='span'><strong> Solution </strong></summary>


  📐 Let's create an `api/fast.py` file and add a root endpoint for the API

  Run the API locally:

  ``` bash
  uvicorn api.fast:app --reload
```

</details>

Try to connect to your root endpoint!

<details>
  <summary markdown='span'><strong> How can I do it? </strong></summary>

  You should be able to connect to the root endpoint your API, either:

  👉 Open the URL served by **uvicorn** in your [http://localhost:8000/](http://localhost:8000/)

  👉 Use the `docs` endpoint of **Swagger** integrated to **FastAPI** in order to test the root endpoint: [http://localhost:8000/docs](http://localhost:8000/docs)

  👉 Using `curl` in the command line as proposed by **Swagger**

  👉 Using the **api usage.ipynb** notebook

</details>

### Add a predict endpoint

Let's add a `predict` endpoint that will take as parameters the features of our dataset:
- Pickup datetime
- Pickup longitude
- Pickup latitude
- Dropoff longitude
- Dropoff latitude
- Passenger count


<details>
  <summary markdown='span'><strong> 📐 Let's code the endpoint </strong></summary>

  Since we started the `uvicorn` server with the `--reload` flag, we can test the new version of the code without restarting `uvicorn`.

  👉 You should be able to test the predict endpoint using [**Swagger**](http://localhost:8000/docs) or the **api usage.ipynb** notebook

  For the moment, the endpoint returns a hard coded value. Let's change that.

  Now that we have a working prediction endpoint, here are the steps for our API to be complete:
  - convert the API parameters into a DataFrame
  - load our trained model
  - make a prediction
  - return the prediction

</details>

### Convert the API parameters into a DataFrame

We need to convert the parameters provided by the API into a DataFrame so that we can make a prediction.

The DataFrame that we are going to build must contain:
- The exact same columns as the `X_train` that we used for the training
- In the exact same order, because eventhough **pandas** knows to access a column by its name, **NumPy** does not and may be hidden in the implementation of the models
- Using the exact same data types (`dtypes`)

<details>
  <summary markdown='span'><strong> 💡 Hints </strong></summary>

  👉 Have a look at the code of the model in order to make sure what those columns are and what data types they use

  👉 The parameters provided by FastAPI are all strings. You probably need to convert them unless you trained your model with `objects`

  In the code of the endpoint, you should be able to `print()` the DataFrame built from the parameters.

  👉 The output of the print will be visible in the logs of your `uvicorn` server (which by default is the ouput of the terminal window). This allows you to make sure that the DataFrame is built correctly

</details>

<details>
  <summary markdown='span'><strong> 📐 Let's build a DataFrame from the API parameters and print it </strong></summary>

Once the code is done, call the endpoint using the **api usage.ipynb** notebook, and see how the DataFrame gets printed in the console. The output should be similar to this:

Here is the print of our DataFrame:

``` bash
                           key          pickup_datetime  pickup_longitude  pickup_latitude  dropoff_longitude  dropoff_latitude  passenger_count
0  2009-06-15 17:26:21.0000001  2009-06-15 17:26:21 UTC        -73.844311        40.721319          -73.84161         40.712278                1
```

Here we can see the call to our API that we just made using the notebook (notice how we see the parameters passed in the URL):

``` bash
INFO:     127.0.0.1:52224 - "GET /predict?pickup_datetime=2020-12-12+12%3A12%3A12+UTC&lon1=41.123456&lat1=41.123456&lon2=41.123456&lat2=41.123456&passcount=3 HTTP/1.1" 200 OK
```

</details>

### Load our trained model and make a prediction

Now that your API is able to convert the provided parameters into a DataFrame, the last step in order to make a prediction is to load the model/pipeline that we trained.

<details>
  <summary markdown='span'><strong> Solution </strong></summary>

  You may train the model locally in order to retrieve a trained `model.joblib` file, or use the one provided with the solution.

  👉 You may encounter issues loading the model provided in the solution if your version of python or of the packages required in order to train the model substantially differ from the ones used when the model of the solution was trained

  ``` bash
  python -m taxifare.trainer
  ```

  Let's load the model using `joblib` and make a prediction using our DataFrame.

  Now that you can make a prediction, the last step is to return it through the API.

  🚨 FastAPI is going to convert whatever is returned by the function of your endpoint into `json`. This will allow the API response to be retrieved by the caller of the API. In particular, this means that the function of your endpoint cannot return a `ndarray`, because `ndarrays` cannot be converted into `json`... The prediction returned by your model may be contained in a `ndarray`. If this is the case, you need to return the prediction in a basic python code structure composed only of dictionaries, lists, and simple data types such as integers, strings, booleans, or datetimes

</details>

📐 Let's make a prediction and test our API using the **api usage.ipynb** notebook

👉 You now have an API running on your machine and able to make predictions for your model

Let's put this API in production so that any developer on the Internet can play with it.

## Create a docker image for our API

Let's create a docker image that we will deploy in Cloud Run.

<details>
  <summary markdown='span'><strong> Solution </strong></summary>

  First, create a `Dockerfile` containing the instructions allowing to building a docker image:
  - Based on a recent version of python (you may explore [Docker Hub](https://hub.docker.com/))
  - Containing the code for the API + the code for your model/pipeline + your trained model (`model.joblib`)
  - Do not forget to add the list of packages required in order to run your code and make a prediction (`requirements.txt`)
  - Add the steps required in order to install the packages listed in `requirements.txt` in the image
  - Add the instruction allowing to run your API when the container starts
  - Do not forget that we want to deploy this image in Cloud Run, therefore `uvicorn` needs to be told on which port to listen using the `$PORT` environment variable

  🚨 Before you try to run your container, you might want to make sure that all the packages required in order to run the code of the API (which includes loading the model) are present in your `requirements.txt` (for example `fastapi` and `uvicorn`, which allow to create and serve your API)

  📐 Let's write the `Dockerfile`

  You should now be able to build your image and run your container locally.

</details>

Since we intend to push our image to Container Registry, let's define a few environment variables that we will reuse accross the commands that we will use:

<details>
  <summary markdown='span'><strong> 👉 adapt these to your project id, multi-region and region </strong></summary>

  ``` bash
  export GCP_PROJECT_ID="le-wagon-data"
  echo $GCP_PROJECT_ID
  ```

  ``` bash
  export DOCKER_IMAGE_NAME="name-of-my-image-in-kebab-case"
  echo $DOCKER_IMAGE_NAME
  ```

  ``` bash
  export GCR_MULTI_REGION="eu.gcr.io"  # replace with the appropriate multi-region
  echo $GCR_MULTI_REGION
  ```

  ``` bash
  export GCR_REGION="europe-west1"  # replace with the appropriate region
  echo $GCR_REGION
  ```

</details>

Make sure you start docker:

<details>
  <summary markdown='span'><strong> MacOS </strong></summary>

Start the Docker app

</details>

<details>
  <summary markdown='span'><strong> Linux </strong></summary>

  ```bash
  sudo service docker start
  ```

  Once you are done, you will be able to stop docker:

  ```bash
  sudo service docker stop
  ```

</details>

🧹 If you wish to have a clearer idea of what docker is doing as you build and run the image, you may clean your existing images and containers:

``` bash
docker rm $(docker ps -aq)              # delete all containers
docker rmi $(docker images -q)          # delete all images
```

👉 What this does is clean your machine from all existing containers and docker images. You would normally be more specific in order to keep containers and images that you might want to reuse or build upon in the future

<details>
  <summary markdown='span'><strong> Let's build our image! 🔥 </strong></summary>

  ``` bash
  docker build -t $GCR_MULTI_REGION/$GCP_PROJECT_ID/$DOCKER_IMAGE_NAME .
  ```

  👉 See all the instructions (`FROM`, `COPY`, `RUN`, `CMD`) of the Dockerfile being executed one after the other

</details>

We can now see the base image and our image:

``` bash
docker images
```

The output should be similar to this one (notice how we could have changed the name of the image):

``` bash
REPOSITORY                                               TAG          IMAGE ID       CREATED          SIZE
eu.gcr.io/le-wagon-data/name-of-my-image-in-kebab-case   latest       01f1801a00fa   18 seconds ago   1.62GB
python                                                   3.8-buster   9b9126f2a963   40 hours ago     883MB
```
<details>
  <summary markdown='span'><strong> Let's run our API in our container to make sure that everything is ok 🎸 </strong></summary>

  ``` bash
  docker run -e PORT=8000 -p 8000:8000 $GCR_MULTI_REGION/$GCP_PROJECT_ID/$DOCKER_IMAGE_NAME
  ```

  How cool is that that you can connect to your API inside of the container with [Swagger on port 8000](http://localhost:8000/docs) 🎉

  Pretty nice, but the easiest way to test our container is through the **api usage.ipynb** notebook...

</details>

Want to shutdown your container? Open a **new terminal window** and:

``` bash
docker ps
```

Then:

``` bash
docker stop 6d38cbecf5ec  # replace with your container id
```

<details>
  <summary markdown='span'><strong> 🤔 How can I make sure that the API that I am contacting is running within the container? </strong></summary>

  Just restart the container with a different port, and connect to it:

  ``` bash
  docker run -e PORT=8000 -p 8001:8000 $GCR_MULTI_REGION/$GCP_PROJECT_ID/$DOCKER_IMAGE_NAME
  ```

  👉 Here we still use the port 8000 inside of the container: the `-e PORT=8000` flag tells `uvicorn` to listen to this port inside of the container, the `-p 8001:8000` flag maps the `8001` port oustide of the container (in your machine) to the `8000` port inside of the container, which allows you to connect to your `localhost` on the port `8001` in order to contact the API inside of the container

  👉 Connect with [Swagger on port 8001](http://localhost:8001/docs) 🎉

</details>

## Push our API to production

Now that we verified that our API is up and running in our container, a few last steps are required in order to push our API to production...
<details>
  <summary markdown='span'><strong> Let's push our image to Container Registry: </strong></summary>

  ``` bash
  docker push $GCR_MULTI_REGION/$GCP_PROJECT_ID/$DOCKER_IMAGE_NAME
  ```

  👉 This step may take some time is your network connection is not that fast

  Your image now lives in the cloud, you may visit it using the [Container Registry console](https://console.cloud.google.com/gcr)

  Let's deploy our image from Container Registry to Cloud Run:

  ``` bash
  gcloud run deploy --image $GCR_MULTI_REGION/$GCP_PROJECT_ID/$DOCKER_IMAGE_NAME --platform managed --region $GCR_REGION
  ```

  👉 Choose a service name

  👉 **Allow unauthenticated invocations** so that any developer can play with your API

  Your API is now live on the address provided by Cloud Run 🔥

  The URL of your production API is output by the command line and should be similar to:

  ``` bash
  https://name-of-my-image-in-kebab-case-xi54eseqrq-ew.a.run.app
  ```

</details>

Your container is visible in the [Cloud Run console](https://console.cloud.google.com/run).

You may use your API in the cloud:
- By pasting the URL in a browser (you will see the response of the root endpoint)
- By using the **Swagger** `/docs` endpoint
- Through the **api usage.ipynb** notebook

👉 Observe how the prediction of the API is the same for the parameters that the notebook provides, whether the API runs on your machine, in a container on your machine, or in the cloud...

Congratulations 🎉

👉 Once your are done, do not forget to stop the docker app on your machine...

🚨 **Do not forget** to delete your container from Cloud Run if you do not intend to keep your API in production (and save some 💸)
