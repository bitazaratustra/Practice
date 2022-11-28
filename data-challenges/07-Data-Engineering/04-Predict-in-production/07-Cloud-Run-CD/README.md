
## Objective

Setup **Continuous Deployment** from your **GitHub repository** to **Cloud Run**.

**Cloud Build** will detect the new versions of your code pushed to the production branch of your GitHub repository.

Whenever a new commit is pushed, Cloud Build will build the Docker image for your project, push it to Container Registry and deploy to Cloud Run.

## Context

The goal of this challenge is to setup **Continuous Deployment** from a **GitHub repository** to a **Cloud Run service**.

In order to do that, we will use **Cloud Build** 🛠

## Create a Docker project

We will create a very simple API project with just 3 files...

### Project

Create a new project called `TestCloudRunCD` in your *projects directory*: `~/code/<user.github_nickname>`.

``` bash
cd ~/code/<user.github_nickname>
mkdir TestCloudRunCD
```

Create the `api.py`, `Dockerfile` and `.gitignore` files in the project and fill their content.

``` bash
cd TestCloudRunCD
touch api.py
touch Dockerfile
touch .gitignore
```

Now we need a **git** repository, because:
- We always want our code to be stored in **git**, whatever its use
- The **Continuous Deployment** is going to detect when our commits are pushed to **GitHub** in order to trigger a deployment to production

Let's create a new **git** repository:

``` bash
git init
```

We also need a corresponding repository on **GitHub** on which to sync our code:

``` bash
gh repo create
```

🚨 Pay attention to the name of the repository that you create: **Container Registry** will only work correctly with repositories having a name following the [kebab-case naming convention](https://betterprogramming.pub/string-case-styles-camel-pascal-snake-and-kebab-case-981407998841): `my-repo-name`

Now that the project is setup, let's start coding! 🚀

### api.py

The `api.py` will contain a rudimentary `FastAPI` API with a root endpoint:

``` python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return "Hello from Cloud Run CD"
```

### Dockerfile

The `Dockerfile` is based on a python image and uses `uvicorn` in order to serve the API.

``` dockerfile
FROM python:3.8-buster

COPY api.py api.py

RUN pip install -U pip
RUN pip install fastapi uvicorn

CMD uvicorn api:app --host 0.0.0.0 --port $PORT
```

### .gitignore

The `.gitignore` will contain the list of files we do not want to store in git:

``` python
__pycache__
```

### Create our first commit

Now that the base content of the project is done, we can commit our code:

``` bash
git add --all
git diff --staged
git commit -m "initial commit"
```

And finally push our code to **GitHub**:

``` bash
git push origin master
```

👉 As always, make sure that your container runs locally before attempting to configure the **Continuous Deployment** to **Cloud Run**

Build the image:

``` bash
docker build -t test .
```

Test it locally:

``` bash
docker run -e PORT=8080 -p 8001:8080 test
```

👉 The API should be visible on http://localhost:8001/

## Create and configure a Cloud Run service for Continuous Deployment

First, let's [enable the Cloud Build API](https://console.cloud.google.com/flows/enableapi?apiid=sourcerepo.googleapis.com,cloudbuild.googleapis.com) ⚙️

Then, go to [Cloud Run](https://console.cloud.google.com/run).

Click on the **Create Service** button:
- Enter a name for your service
- Select a region on which to run the container of the project (for example `europe-west1` for Belgium)
- Click **Next**

Select **Continuously deploy new revisions from a source repository**:
- Click on **Set up with Cloud Build**

Connect your GitHub account:
- Select GitHub as a repository provider
- Click on Authenticate to connect to your GitHub account

Install the **Google Cloud Build** app on the project repository:
- Click **Install Google Cloud Build**
- If asked to, select the your GitHub account
- Check **Only selected repositories**
- Select the repository of your project (🚨 **Container Registry** will only work correctly with repositories having a name following the [kebab-case naming convention](https://betterprogramming.pub/string-case-styles-camel-pascal-snake-and-kebab-case-981407998841): `my-repo-name`)
- Click **Install**

Select the source repository:
- Select the configured repository
- Read and check **I understand ...**
- Click **Next**

Configure your project:
- Select the branch of your repository on which new commits will trigger the **CD** (for example `^master$`)
- Select the **Dockerfile** build type and enter the path to the `Dockerfile` in your project if required
- Click **Save**

You may select additional options for your container in the **Advanced settings**, such as container memory or allocated CPUs.

Once you are done fine tuning your configuration, click **Next**.

Select the parameters for the service:
- Allow all traffic
- Allow all unauthenticated invocations
- Click **Create**

Get the production URL from the interface, it should look something like:

``` bash
https://lw-docker-test-xi54eseqrq-ew.a.run.app/
```

Boom, just like that your container is in production and you did not even had to build the image of the container 🎉

If you see a sad unicorn, do not worry, it is just there while **Cloud Build** is building your Docker image before pushing it to **Cloud Run**.

<a href="https://wagon-public-datasets.s3.amazonaws.com/data-science-images/DE/cloud-build-sad-unicorn.png"><img src="https://wagon-public-datasets.s3.amazonaws.com/data-science-images/DE/cloud-build-sad-unicorn.png" width="150" alt="sad unicorn"></a>

Once your application is in production, as usual you will see the built image stored in [Container Registry](https://console.cloud.google.com/gcr).

## Pushing a new version of your code to production

If you selected `master` as the branch for production, a new image will be built each time you push the code of your project to **GitHub**.

Another option could be to create a dedicated `production` branch linked to **Cloud Build**.

👉 This allows you and your team to decorrelate the *GitHub workflow* (merging the *Pull Requests* in the `master` branch) from the production workflow (pushing code to the `production` branch)

Once you have choosen a workflow, as usual:

``` bash
# code some awesome stuff
git add --all
git diff --staged
git commit -m "add awesome stuff"
git push origin master
```

Then watch the magic happen as...

A new image built from your code gets pushed to [Container Registry](https://console.cloud.google.com/gcr):
- Click on the name of the repository
- Click on the name of the image
- See that a new version of your image was just built from the latest version of your code

A new version of your service is put to production on [Cloud Run](https://console.cloud.google.com/run):
- Click on the name of your service
- Click on **Build History**
- See that a new container is in production
- You may have a look at the build steps of the container or verify the logs

## Decommissioning the service

Once you are done using the service, as always, you will decommission it.

🚨 The proper way to decommission the service is not just to delete the **Cloud Run** service, as it will be automatically recreated whenever you push a new version of your code to the production branch of your repository

In order to decommision the service:
- Go to [Cloud Build](http://console.cloud.google.com/cloud-build)
- Click on **Stop streaming build**
- Go to **Triggers** (the trigger is the mechanism detecting when a new version of your code is pushed and triggering a build on **Cloud Build**)
- Select the trigger
- Click on **Delete**
- Go to [Cloud Run](https://console.cloud.google.com/run)
- Select the service
- If you deleted the trigger properly, you should not see any suggestion that you delete the trigger when you click to delete the service
- **Delete** the service
- Go to [Container Registry](https://console.cloud.google.com/gcr)
- Select the build Docker images
- Delete the images

Now you can remove the trigger from **GitHub**:
- Go to your **GitHub** repository
- In **Settings**
- Go to **Integrations**
- Next to the **Google Cloud Build** app, click on **Configure**
- You can either uninstall the app or remove your repository from the list of accessed repositories

You may want to revoke the access of :
- In your GitHub account, in [Applications](https://github.com/settings/apps/authorizations)
- Revoke the access of the **Google Cloud Build** app

## Debugging

You should be able to limit the number of errors occuring on **Cloud Run** by first making sure that your container runs correctly on your machine.

But there are still some errors that will only be visible once your container is in production:

In order to understand what is going on, there are two options:

### Option 1: check the build history

If your service fails to start, you may want to verify that the image build properly.

Checking these logs will also allow you to make sure that everything was build correctly.

The build history is visible in [Cloud Build](http://console.cloud.google.com/cloud-build):
- Click on the commit (such as `db40fd53`) having triggered the build

👉 You now see the logs generated by the build of the image for the commit

``` bash
Step #0 - "Build": Step 1/5 : FROM python:3.8-buster
Step #0 - "Build": 3.8-buster: Pulling from library/python
Step #0 - "Build": d960726af2be: Pulling fs layer
Step #0 - "Build": a181a2736d7a: Pull complete
Step #0 - "Build": Digest: sha256:6dc13b6b1ab55370895d75a2ac5a285abaf8821764c7467b2a52e45c601477b3
Step #0 - "Build": Status: Downloaded newer image for python:3.8-buster
Step #0 - "Build":  ---> e7d3be492e61
Step #0 - "Build": Step 2/5 : COPY api.py api.py
Step #0 - "Build":  ---> 07314cd21657
Step #0 - "Build": Step 3/5 : RUN pip install -U pip
Step #0 - "Build":  ---> Running in 25e3ea8cde29
```

### Option 2: check the logs of your service

This is always the first thing to check once your service is running...

Go to [Cloud Run](https://console.cloud.google.com/run).

Click on **Logs** and look for errors.
