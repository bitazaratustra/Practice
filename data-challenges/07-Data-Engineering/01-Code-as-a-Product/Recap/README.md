**The goal of the first part of today's recap is to go over the process of creating a new package, understand the purpose of different files inside it and practice Continuous Integration and the Continuous Deployment.**
**The second part is an introduction to the TaxiFare Challenge.**
<br><br>


## Package creation

### 🤔 How can you create a new package?

Let's create a **bbquote** package that will allow us to retrieve Breaking Bad quotes...

<details>
  <summary markdown='span'><strong>💡 Hint </strong></summary>

<br>

``` bash
packgenlite package-name
```

In order to create a new package you can run:

``` bash
packgenlite bbquote
cd bbquote
tree
```

You should see the entire project structure created by the `packgenlite` tool.
</details>

<br>

### 🤔 Where can you create a new method that will belong to the package?

Let's use the [Breaking Bad API](https://breaking-bad-quotes.herokuapp.com/v1/quotes) in order to create a **get_quote** method and add it to our package.

Alternatively, use the [Le Wagon Breaking Bad Quotes API](https://wagon-breaking-bad-quotes.herokuapp.com/v1/quotes).

<details>
  <summary markdown='span'><strong>💡 Hint </strong></summary>

<br>

**You can create a new `*.py` file within the `bbquote` directory containing an `__init__.py` file.**

```bash
touch bbquote/lib.py
```

```python
# bbquote/lib.py
import requests


def get_quote():
    # url = 'https://breaking-bad.lewagon.com/v1/quotes'  # alternative API
    url = 'https://breaking-bad-quotes.herokuapp.com/v1/quotes'
    response = requests.get(url).json()[0]

    return f"'{response['quote']}' \n> {response['author']}"


if __name__ == "__main__":
    print(get_quote())
```
</details>

<br>

### 🤔 Can you call the method from anywhere on your machine at this point?

Let's call our method from the terminal using **python** and **ipython**, and from a notebook...

<details>
  <summary markdown='span'><strong>💡 Hint </strong></summary>

<br>

**No.**

You can't as long as the package is not **installed** on your system.
In order to be able to do that you have to run:
`pip install -e .`
which will make the package executable from any location and will also listen to **any updates of the package files** (similar to `%autoreload`)

**👉 You can now call the method by importing it from `bbquote.lib` anywhere on your machine or you can execute the `lib.py` file directly by running: `python -m bbquote.lib`.**
</details>

<br>

### 🤔 What can you do to be able to run `bbquote-run` in the Terminal at any location and achieve the same result?

Let's create a script displaying a breaking bad quote.

<details>
  <summary markdown='span'><strong>💡 Hint </strong></summary>

<br>

**You can create a script which will import and call the method.**

A script is an executable file that you can run from the Terminal. They are useful with automation of the engineering tasks.
In order to convert a python file into a script you have to add two additional headers to the file and then the code which should be executed upon running the script.

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
```

Do not forget to add the script to your `setup.py` file!
</details>
<br>

### 🤔 Optional: how to start every new terminal window with a nice productive quote?

Anyone has an idea?

<details>
  <summary markdown='span'><strong>💡 Hint </strong></summary>

<br>

Edit your `~/.zshrc` and add the name of your `bbquote-run` script at the very bottom...

Now open a new terminal window and see what happens!
</details>
<br>

### 🤔 Let's now write a test for our `get_quote` method. But wait, why do we even need a test?

Let's write some tests and play with Continuous Integration...

<details>
  <summary markdown='span'><strong>💡 Hint </strong></summary>

<br>

There are multiple reasons for introducing testing in our projects and all of the below reasons are valid. The right question is: why _wouldn't_ you introduce testing? 🤔

- We want to make sure our package and its methods are working correctly in different circumstances
- In case our teammate is updating the code, we are making sure the updates will not crash the package functionality
- Tests are part of Continuous Integration - it helps to maintain the quality of our code before committing the merge on a remote repository.
</details>
<br>

### 🤔 Let's expose our project through a public url. How you we do it?

Let's release our package to the world!

<details>
  <summary markdown='span'><strong>💡 Hint </strong></summary>

<br>

**We can create a new app on Heroku and push our code with additional configuration.**

In order to be able to display our project on an accessible url we have to use a cloud platform enabling us to build, run and operate applications. Heroku is one of such providers. In order to deploy our application and display the functionality of the `get_quote` method we can:

<details>
  <summary markdown='span'><strong> 1. Create an `app.py` file with simple frontend calling the method </strong></summary>

<br>

app.py:
``` python
import streamlit as st

from bbquote.lib import get_quote

author, quote = get_quote()  # assuming the function returns an author and a quote

f"{quote}, {author}"
```
</details>


<details>
  <summary markdown='span'><strong> 2. Add `streamlit` to the `requirements.txt` </strong></summary>

<br>

requirements.txt:
``` python
streamlit
```
</details>


<details>
  <summary markdown='span'><strong> 3. Add a `setup.sh` and `Procfile` for Heroku configuration </strong></summary>

<br>

setup.sh:
``` bash
mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"your-email@domain.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
```

Procfile:
``` bash
web: sh setup.sh && streamlit run app.py
```
</details>


<details>
  <summary markdown='span'><strong> 4. Create a new app on heroku </strong></summary>

<br>

``` bash
heroku keys:add ~/.ssh/id_ed25519.pub  # in order to authentify using SSH
```

``` bash
heroku create --ssh-git <unique-app-name>  # using a SSH remote
```

</details>


<details>
  <summary markdown='span'><strong> 5. Push our code to Heroku </strong></summary>

<br>

``` bash
git push heroku master
```

</details>


<details>
  <summary markdown='span'><strong> 6. Set the dynos to run our web application </strong></summary>

<br>

``` bash
heroku ps:scale web=1
```

</details>


<br>

In case the application has an error, don't forget to check the logs: `heroku logs --tail`.

</details>
<br>

### 🤔 Ok, this seems like a lot of pushing: `git push origin`, `git push heroku`... Can we automate it somehow?

Let's activate Continous Deployment...

<details>
  <summary markdown='span'><strong>💡 Hint </strong></summary>

<br>

Yes, this process is called Continuous Deployment. With additional configuration in the `pythonpackage.yml` we can ask GitHub to deploy the latest code to Heroku for us if all the tests will pass.


⚠️ Do not forget to fill `HEROKU_API_KEY` and `HEROKU_EMAIL` in the GitHub secrets of the repository

</details>
<br>

## TaxiFare Challenge

Let's open the first challenge of tomorrow and go through the code together! Whenever you leave off today, continue from there in the morning after the lecture. Going through entire challenge shouldn't take you longer than 45 minutes.
