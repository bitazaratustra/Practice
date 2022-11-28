
## Objective

Use **Docker** in order to build a Docker image for your API project.

Start on your machine a container hosting your API.

## Context

We now have a working **Prediction API**, but it is not much use if it can only be queried from our local machine.

We want to make it available to the world. In order to do that, the first step is to create a **Docker image** that will contain both the environement required in order to allow our code to run + the code of our API. Of course, remember that we still need the code of our pipeline along with the code of the API in order to be able to load our `model.joblib` file.

In the next exercise we will see how to put the Docker image in production so that it can be accessed from any machine on the Internet 🌍

For now let's focus on creating a **Docker image** allowing us to run the code of our Prediction API on our machine.

You can see the Docker image as some sort of runnable virtual environment containing all the packages for the app + our code.

## Build a Docker image for our API

Let's create a Docker image for our prediction API and use it locally.

Let's start by creating the `Dockerfile` that will contain the instructions telling Docker how to build the image.

In order to do so copy the provided `Dockerfile` in your project (or create an empty one).

Your project should look like this:

``` bash
.
├── api
│   ├── __init__.py
│   └── fast.py
├── notebooks
│   └── API\ usage.ipynb
├── TaxiFareModel
│   ├── __init__.py
│   ├── data.py
│   ├── encoders.py
│   ├── gcp.py
│   ├── params.py
│   ├── trainer.py
│   └── utils.py
├── Dockerfile
├── Makefile
├── MANIFEST.in
├── model.joblib
├── predict.py
├── requirements.txt
└── setup.py
```

Now let's fill the content of the `Dockerfile` in order to create a recipe that will allow us to **build** our **Docker image** 👌

The most common instructions that we will meet in a `Dockerfile` are the following:
- `FROM`: select a base image for our image (the environment in which we will run our code), this is usually the first instruction
- `COPY`: copy files and directories inside of our image (our package and the associated files for example)
- `RUN`: execute a command **inside** of the image being built (for example, install the package dependencies)
- `CMD`: execute the **main** command that will be executed when we run our **Docker image**. There can be only one `CMD` instruction inside of a `Dockerfile`. It is usually the last instruction

### FROM instruction

First let's select the first layer on top of which we will build our **Prediction API** image.

Search for a base image in [Docker Hub](https://hub.docker.com/) which would contain a suitable version of python.

👉 [List of Docker Hub available python images](https://hub.docker.com/_/python)

Use the name of the base image in order to create the `FROM` instruction which will be the first instruction of our `Dockerfile`.

We have built a `Dockerfile` able to create an image based on a Linux distribution and that is able to run python code.

### COPY instructions

Secondly, we want to add our code to the image so that the image can run our package.

Let's add `COPY` instructions in order to tell Docker to copy into the image the following files / code:
- the trained model
- the code of the project which is required in order to load the model
- the code of our API
- the list of requirements

We are now able to build an image able to run our code but what about the dependencies of our code? 🤔

### RUN instruction

We need to tell Docker to install the dependencies of our code when the image is built.

Let's use a `RUN` instruction in order to ask Docker to install the python packages required by our package.

Looks like we are almost finished. Our `Dockerfile` now enables us to build an image:
- based on a linux distribution
- running python code
- with the copy of our code
- and having the dependencies of our code installed

### CMD instruction

We now need to tell Docker what the image should do when it is instantiated inside of a **Docker container** and started. Otherwise we will only have started a container with our code and its dependencies which actually does nothing.

Let's add a `CMD` instruction in order to tell Docker to run our **Prediction API** at the bottom of the `Dockerfile`. Our Prediction API will be served by **uvicorn**.

💡 We need to provide the following **host** and **port** parameters to the **uvicorn** run command:
- The **host** parameter will tell **uvicorn** to listen to all network connections
- The **port** parameter will tell **uvicorn** to listen to HTTP requests on the `PORT` environment variable configured by the cloud service running our Docker container

If we fail to provide any of these parameters our container will run but the **uvicorn** server will be unable to receive incoming HTTP requests.

⚠️  Since we will be running **uvicorn** inside of our container, do not forget to add it to the `requirements.txt` as well as **fastapi**!

## Make sure the Docker daemon is running on your machine

Now that we have created a `Dockerfile` we are going to use **Docker** in order to build an image.

In order to run the Docker commands, you need to make sure that your **Docker daemon** is running on your machine. The Docker daemon is the program that will allow us to run the Docker commands in order to build a Docker image and instantiate it into a runnable Docker container on our machine.

### MacOSX

Make sure that the `Docker.app` is running (you should see a whale in your menu bar).

<img src="https://wagon-public-datasets.s3.amazonaws.com/data-science-images/DE/macos-docker-desktop-running.png" width="150" alt="verify that Docker Desktop is running">

### Linux

Start the Docker service:

``` bash
sudo service docker start
```

### WSL2

Make sure the Docker application is running (you should see a whale in your menu bar).
If you prefer a "command line" way :point_right: you can also use the below command to start the Docker service:

```bash
sudo service docker start
```

## Make sure the Docker image works on our machine

Now let's build the image with a Docker **build** command! ⏰

`docker build --tag=image-name .`

Once built, the image should be visible in the list of images:

``` bash
docker images
```
Your should see a `image-name` image in the **REPOSITORY** column.

Let's run it with a Docker **run** command 👌

Now we can run on our machine a **container** based on the image we created... 🔥

First, we will run the container **interactively** in order to see what was created inside of it...

``` bash
docker run -it -e PORT=8000 -p 8000:8000 image-name sh
```

Let's have a look a the content of the container:

``` bash
ls -la
ls -la TaxiFareModel
```

Note that the autocompletion in the command line does not work...

Once we are done, let's exit the terminal and stop the container

``` bash
exit
```

Now we can run the container as we would in production, without interactivity:

``` bash
docker run -e PORT=8000 -p 8000:8000 image-name
```


💡 *Remember*, since we configured the image with a `$PORT` environment variable, we need to provide it now. We also need to specify the mapping between the port inside of the image and the port at which we will contact the image.

Once we have a running *Docker container*, let's look at the status of the image.

``` bash
docker ps
```

You can now go to [the main page](http://localhost:8000/) of the API and see a magnificent "{"key": "value"}".

Let's play with the API an receive your first prediction!

*Hint*: you may use the `notebooks/API usage.ipynb` notebook, or customize this code:

``` python
import requests

taxifare_api_url = "http://127.0.0.1:8000/predict?FILL&THE&PARAMS&HERE"

response = requests.get(
    taxifare_api_url
).json()

print(response)
```

It's Alive! 😱 🎉

You may stop (or kill) the image...

``` bash
docker stop 152e5b79177b  # ⚠️ use the correct CONTAINER ID
docker kill 152e5b79177b  # ☢️ only if the image refuses to stop (did someone create an ∞ loop?)
```

## Once you are done with Docker...

Remember to stop the Docker daemon in order to free ressources on your machine once you are done using it...

MacOS:
- Stop the `Docker.app` with **Quit Docker Desktop** in the menu bar

Linux/WSL2:
- stop the Docker service

``` bash
sudo service docker stop
```

Windows
- Stop the Docker application
