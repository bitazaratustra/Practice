
## Objective

Use **Container Registry** in order to store in the cloud the Docker image built for your API.

Deploy on **Cloud Run** a container exposing your API to the world.

## Context

In the previous exercise, we have built a **Prediction API** Docker image that we are able to run on our local machine.

There are 2 remaining steps in order to enable the developers from anywhere around the world to play with it:
- Push the **Docker image** to **Google Container Registry**
- Deploy the image on **Google Cloud Run** so that it gets instantiated into a **Docker container**

The role of **Container Registry** will be to act as a storage for our Docker image.
The role of **Cloud Run** will be to run a Docker container instantiated from our image.

🚨 If you are an **Apple Silicon** user, skip this challenge and proceed with the **CD to Cloud Run** challenge.

<details>
  <summary markdown='span'><strong> 💡 How do I know whether my Mac is an Apple Silicon computer ? </strong></summary>

Copy-paste the following command in the terminal and hit `Enter` to execute the command.

``` bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/lewagon/setup/master/utils/macos_list_processor_type.sh)"
```

☝️ The result of the command should indicate whether your computer uses Apple Silicon or Intel.

</details>

<details>
  <summary markdown='span'><strong> 💡 Why ? </strong></summary>

If your computer uses Apple Silicon, the images built by Docker are using ARM processor instructions. The machines running in Google Cloud Platform are running on x86 compatible processors, as are the vast majority of the machines of the cloud service providers. Because ARM and x86 processor instructions are not compatible with one another, it will not be possible to run an image built from Docker running on an Apple Silicon machine in Cloud Run.

</details>

## Push our prediction API image to Google Container Registry

**Google Container Registry** is a service storing Docker images on the cloud with the purpose of allowing **Cloud Run** or **Kubernetes Engine** to serve them.

It is in a way similar to **GitHub** allowing you to store your git repositories in the cloud (except for the lack of a dedicated user interface and additional services such as `forks` and `pull requests`).

First, let's make sure to enable [Google Container Registry API](https://console.cloud.google.com/flows/enableapi?apiid=containerregistry.googleapis.com&redirect=https://cloud.google.com/container-registry/docs/quickstart) for your project in GCP.

Once this is done, let's ensure that your GCP credentials are correctly registered for the command line.

``` bash
gcloud auth list
```

If your account is not listed then you have to authenticate:

``` bash
gcloud auth login
```

Now let's configure the gcloud command for the usage of Docker.

``` bash
gcloud auth configure-docker
```

And verify your config. You should see your GCP account and default project.

``` bash
gcloud config list
```

You can now define an environment variable for the name of your project.
This environment variable will be used accross following commands.

``` bash
export PROJECT_ID=replace-with-your-gcloud-project-id
echo $PROJECT_ID
gcloud config set project $PROJECT_ID
```

And an environment variable for the name of your docker image.
This environment variable will be used accross the following commands.

``` bash
export DOCKER_IMAGE_NAME=define-some-container-image-name
echo $DOCKER_IMAGE_NAME
```

Now we are going to build our image again.
This should be pretty fast since Docker is pretty smart and is going to reuse all the building blocks used previously in order to build the prediction API image.

``` bash
docker build -t eu.gcr.io/$PROJECT_ID/$DOCKER_IMAGE_NAME .
```

Again, let's make sure that our image runs correctly, so that we avoid spending the time on pushing an image that is not working to the cloud.

``` bash
docker run -e PORT=8000 -p 8000:8000 eu.gcr.io/$PROJECT_ID/$DOCKER_IMAGE_NAME
```

We can now push our image to Google Container Registry.

``` bash
docker push eu.gcr.io/$PROJECT_ID/$DOCKER_IMAGE_NAME
```

The image should be visible in the GCP console [here](https://console.cloud.google.com/gcr/).

## Deploy the Container Registry image to Google Cloud Run

We have pushed the Docker image for our Prediction API to **Google Container Registry**. The image is now available for deployment by Google services such as **Cloud Run** and **Kubernetes Engine** (for massive scaling).

We are going to deploy our image to production using **Google Cloud Run**. Cloud Run will be more than enough for our first few hundreds of users. Cloud Run will instantiate the image into a container and run the `CMD` instruction inside of the `Dockerfile` of the image. This last step will start the `uvicorn` server serving our **Prediction API** to the world 🌍

Let's run one last command 🤞

``` bash
gcloud run deploy --image eu.gcr.io/$PROJECT_ID/$DOCKER_IMAGE_NAME --platform managed --region europe-west1
```

After confirmation, you should see a similar output indicating that the service is live 🎉

``` txt
Service name (wagon-data-tpl-image):
Allow unauthenticated invocations to [wagon-data-tpl-image] (y/N)?  y

Deploying container to Cloud Run service [wagon-data-tpl-image] in project [le-wagon-data] region [europe-west1]
✓ Deploying new service... Done.
  ✓ Creating Revision... Revision deployment finished. Waiting for health check to begin.
  ✓ Routing traffic...
  ✓ Setting IAM Policy...
Done.
Service [wagon-data-tpl-image] revision [wagon-data-tpl-image-00001-kup] has been deployed and is serving 100 percent of traffic.
Service URL: https://wagon-data-tpl-image-xi54eseqrq-ew.a.run.app
```

Any developer in the world 🌍 is now able to browse to the deployed url and make a prediction using the API 🤖!

⚠️ Keep in mind that you pay for the service as long as it is up 💸

## Writing to Google Cloud Storage from Google Cloud Run

Do you need to write to GCS from GCR ?

You will be needing to add your credentials to your image so that your code is allowed to push data to your bucket.

In your `Dockerfile`, you will need to put the path to the Google Cloud Plaform credentials you created during setup day.

Hint: you can find the path using:

``` bash
echo $GOOGLE_APPLICATION_CREDENTIALS
```

Now, update your `Dockerfile` with the correct path to your credentials file:

``` bash
COPY /path/to/your/credentials.json /credentials.json
```

And deploy the new image that is able to write to GCS:

``` bash
gcloud run deploy \
    --image eu.gcr.io/$PROJECT_ID/$DOCKER_IMAGE_NAME \
    --platform managed \
    --region europe-west1 \
    --set-env-vars "GOOGLE_APPLICATION_CREDENTIALS=/credentials.json"
```
