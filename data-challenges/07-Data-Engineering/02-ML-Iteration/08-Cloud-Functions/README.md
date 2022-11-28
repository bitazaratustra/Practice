
## Objective

Setup a recurring production job using **Cloud Scheduler** and **Cloud Functions**.

**Cloud Scheduler** will regularly trigger the execution of the job.

**Cloud Functions** will run the job.

## Context

The goal of this challenge is to create a daily scraping job that:
- retrieves the top 3 stories from [Hacker News](https://news.ycombinator.com/)
- stores them in a **Cloud Storage** bucket

This demonstrates a simple recurring production job.

## Project

We will create a simple project in order to store the code executed by **Cloud Functions**.

### Project setup

First, let's copy the code of the **Cloud Functions** challenge in your *projects directory*: `~/code/<user.github_nickname>`.

``` bash
cp -r ~/code/<user.github_nickname>/{{local_path_to("07-Data-Engineering/02-ML-Iteration/08-Cloud-Functions/CloudFunctionCode")}} ~/code/<user.github_nickname>/CloudFunctionCode
```

Then, we will create a local git repository for the project:

``` bash
cd ~/code/<user.github_nickname>/CloudFunctionCode
git init
```

👉 It is now up to you to handle the git lifecycle of the project

## Create a Cloud Function

The purpose of the **Cloud Function** will be to host a piece of code that can be triggered at will.

Go to [Cloud Functions](https://console.cloud.google.com/functions):
- Press *CREATE FUNCTION*
- Enter a *Function name*
- Select a *Region* on which to host and run your code
- Select for *Trigger type* the *HTTP* option
- Select *Require authentication*
- Press *SAVE*

You may configure additional options for your runtime:
- *Memory allocated* will determine the amount of memory available for your code to run (trying to use more memory will terminate the function)
- *Timeout* will determine the maximum amount of time that your function is allowed in order to take to complete its job (exceeding this delay will terminate the function)
- You may select a specific *Runtime service account* determining the credentials of your code against other **GCP** services
- You may fill *Runtime environment variables* required by your code in order to execute (those may contain credentials to third party providers for example)
- Press *NEXT*

## Configure the Cloud Function

Let's select a *Runtime* for our function:
- *Python 3.9* seems to be a good option

👉 The *runtime* defines the [language interpreter](https://en.wikipedia.org/wiki/Interpreter_(computing)) (and its version) used in order to run your code

You can keep the existing *Entry point* or use a different name. The *Entry point* is the name of the main function that will be called when the **Cloud Function** is triggered.

As you see in the *docstring* of the default function created for you, the *Entry point* called when the **Cloud Function** is triggered will receive as parameters a [Flask request](https://flask.palletsprojects.com/en/2.0.x/api/#flask.Request) object. **Flask** is a python web microframework allowing to create websites and API.

👉 The content of the *Flask request* allows the function to adapt its behavior to the parameters passed by the called. We will not need to use this at the moment

We will now be editing the content of the 2 files generated for the Cloud Function:
- `main.py` will contain the *Entry point* of the **Cloud Function** as well as all the code required to run the function
- `requirements.txt` will contain the list of packages required for our code to run

## Daily scraper

Using the `requests` and `beautifulsoup4` packages, create a *function* that retrieves the top 3 news of the day on [Hacker News](https://news.ycombinator.com/).

The function, which will be called by the *Entry point* of the **Cloud Function** will not require any parameters and will return a list of results (or an empty list if an error occurs).

``` python
def top_3_from_hackernews():
    """
    return top 3 news from hackernews
    """
    pass
```

Use an `ifmain` block in order to test that your code runs correctly on your machine before editing your Cloud Function.

Once your code works on your machine, copy it to your **Cloud Function** (select `main.py` in the interface and edit the content).

🚨 Do not forget to fill `requirements.txt` with the list of required packages:

``` bash
requests
bs4
google-cloud-storage
```

When you are done editing the code of your function, press *DEPLOY* 🚀

👉 Your function can now be called from anyone with the proper permissions

## Test the Cloud Function

Once the Cloud Function is deployed, go to [Cloud Functions](https://console.cloud.google.com/functions):
- Select your function
- Click on *TESTING*
- Click on *(...) TEST THE FUNCTION*

👉 You should see the json response of your Cloud Function returned by the entry point

``` bash
{"response": "the Cloud Function json response, if any"}
```

The json response returned by the Cloud Function allows the caller of the Cloud Function to know whether everything ran correctly.

👉 In the logs bellow, you should see the output of the print of your code

``` bash
it works!
```

The print output visible in the logs allows to give context if an error occurs in the code during the process of the Cloud Function.

## Create a Cloud Scheduler

The purpose of the **Cloud Scheduler** will be to trigger your **Cloud Function** periodically.

Go to [Cloud Scheduler](https://console.cloud.google.com/cloudscheduler):
- Press *CREATE JOB*
- Enter a job *Name*
- Enter a *Frequency* for the job to run

👉 The syntax used in order to define the periodicity of the job is called the [crontab syntax](https://en.wikipedia.org/wiki/Cron). Have a look at [crontab guru](https://crontab.guru/) in order to understand the syntax

A few common configurations:
- `0 8 1 * *`: monthly on the first day at 8AM
- `0 8 * * *`: daily at 8AM
- `0 * * * *`: every hour
- `* * * * *`: every minute

Continue with the configuration:
- Enter the *Timezone* for the job
- Click on *CONTINUE*
- Select the target *HTTP*
- Enter the *URL* of the **Cloud Function** you just built (similar to https://europe-west1-le-wagon-data.cloudfunctions.net/test)

If you do not know which URL to use:
- Go to [Cloud Functions](https://console.cloud.google.com/functions)
- Select the function you want to trigger
- Click on *TRIGGER*
- Copy the *Trigger URL*

- Optionally select the *HTTP method* with which to call your function and add *headers*
- Select for *Auth header* the *Add OIDC token* option
- Enter the name of a service account having access to your **Cloud Function** (similar to le-wagon-data@le-wagon-data.iam.gserviceaccount.com)
- Click on *CONTINUE*
- Click on *CREATE*

If you do not know which service account to use:
- Go to [Cloud Functions](https://console.cloud.google.com/functions)
- Select the function you want to access
- Click on *PERMISSIONS*
- Have a look at the list of *Member* service accounts and their *Role*

You have created a Cloud Scheduler that will trigger your function periodically 🎉

👉 You may manually run the scheduler using *RUN NOW* or wait for the **Cloud Function** to be triggerred by the **Cloud Scheduler** in order to verify that everything works correctly

🚨 Do not forget to **Delete** or **Pause** the **Cloud Scheduler** if you do not intend on actively using the linked **Cloud Function** 💸

The *View* link allows you to have a look at the logs of the **Cloud Scheduler** in order to verify when the **Cloud Function** was triggered and if everything ran correctly.

👉 You may also want to have a look at the logs of the **Cloud Function** in order to verify that the code runs smoothly

## Command line interface

Another option is to go the jedi way with the CLI 🧙‍♀️

👉 Have a look at the content of the `Makefile` and edit the variables

Then, create a Cloud Function from your code (fill `main.py` and `requirements.txt`):

``` bash
make deploy_function
```

👉 Your *Entry Point* should be located in a file called `main.py` for **Cloud Functions** to find it

And schedule a reccurent trigger:

``` bash
make deploy_trigger
```

Then pause it if you do not use it:

``` bash
make pause_trigger
```
