If you managed to complete all the challenges of the day so far, congratulations!

Let's finish the day with a kind of **advanced scraping**. In this challenge, we'll be using a _real_ browser. You will see that this technique can be used to perform **web automation** (like submitting forms for instance!)

Some websites don't work the way HTTP & HTML were intended to work. They use a technique called **client-side rendering** where the HTML starts almost empty, and all the DOM on the page is generated thanks to JavaScript.

This means that if you use the traditional technique where you look into the HTML (`curl`-style), you won't find anything! You need the JavaScript to be fully rendered, and to do so you need a browser, like Chrome.

To drive Chrome from code, you need a pilot. We will use [**Selenium**](https://www.seleniumhq.org/). With Selenium, you can navigate to a page, scroll down, click on a link, fill in a few inputs, click on a button, etc. Anything a human can do with a browser can also be done with Selenium.

⚠️ There is no `make` on this challenge.

## Example

Imagine you want to get some information about a recipe. The URL structure is easy to understand. `251` is the id of the recipe we are looking for:

```bash
https://recipes.lewagon.com/recipes/251/advanced
```

Go to [that URL](https://recipes.lewagon.com/recipes/advanced?search[query]=carrot&page=1), disable JavaScript in your browser, and reload. To disable JS quickly you can install these extensions:

- [Disable JavaScript](https://addons.mozilla.org/en-US/firefox/addon/disable-javascript/) for Firefox 🦊
- [Disable JavaScript](https://chrome.google.com/webstore/detail/disable-javascript/jfpdlihdedhlmhlbgooailmfhahieoem) for Chrome 🎈

See how the page loads indefinitely? We can't scrape with just `requests` + `BeautifulSoup` from the server-side generated HTML. We need Selenium and a browser!

## Setup

For this challenge, we will use Selenium + Chrome. If you want to try another browser (Firefox), you can do that as well but the instructions will need to be adapted.

Open Google Chrome on your computer (if you don't have it, install it), then go to "About Google Chrome". You should see the version you are on.

Based on that version, install the right [`chromedriver-binary`](https://pypi.org/project/chromedriver-binary/77.0.3865.40.0/#history) and [`selenium`](https://pypi.org/project/selenium/) modules:

```bash
pip install selenium
pip install chromedriver-binary==77.0.3865.40.0 # Version might be different!
```

OK! Now that this is done, open the `test_advanced_scraping.py` file and copy/paste the following code:

```python
from selenium import webdriver
import chromedriver_binary

driver = webdriver.Chrome()
driver.get("https://recipes.lewagon.com/recipes/advanced")

# driver.quit()
```

Open your terminal and run:

```bash
python test_advanced_scraping.py
```

🚀 It should open a Chrome window, navigate to the page and stay like that! If you uncomment the last line `driver.quit()` then you will see that Chrome will close automatically  when the script is done.. You need to do that otherwise you'll have plenty of Chrome windows open after a while!

## Searching Chocolate-Based recipes 😋

We will now simulate user interaction with the page. Something a user can do is click on the search bar and type a location. Go ahead and try it: type `chocolate`. Now click on the magnifying glass button to launch the search.

This is what we want to simulate! We will use the [`find_element_by_id`](https://selenium-python.readthedocs.io/locating-elements.html#locating-by-id) method to locate the input which we want to search.

```python
from selenium.webdriver.common.keys import Keys

search_input = driver.find_element_by_id('TODO') # Open the inspector in Chrome and find the input id!
search_input.send_keys('chocolate')
```

With that piece of code, you should see your Chrome browser opening on the specified URL and filling the location input with `chocolate`

## Submitting the Form

The next step will be to submit the form to get the chocolate-based recipes back. To do that, we can add the following line to our code:

```python
search_input.submit()
```

Just like that, you should see the updated list of recipes.

## Retrieving the URLs of Each Recipe

As you can see, the list of updated recipes is also fetched using Javascript and we have to wait a little bit to see the results. This means we need to wait for the recipes to appear before being able to gather the recipes' URLs.

To do that we will use [**explicit wait**](https://selenium-python.readthedocs.io/waits.html):

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# [...]
wait = WebDriverWait(driver, 15)
wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='recipes']")))
```

The weird string in the method uses an [XPath](https://en.wikipedia.org/wiki/XPath) search in the DOM. It locates the `<div/>` with an `id` that has the value `recipes`. After exploration of the website's DOM, we found that this `<div/>` is the element that contains all the recipes fetched by the search.

Now that we waited for the filtered recipes to appear, it's time to collect the URL of each recipe to be able to scrape each one of them.

```python
recipe_urls = []
cards = driver.find_elements_by_xpath("//div[@class='recipe my-3']")
print(f"Found {len(cards)} results on the page")
for card in cards:
    url = card.get_attribute('data-href')
    recipe_urls.append(url)

print(recipe_urls)
```

Run the code from the terminal. You should get back 12 URLs (i.e. all the recipes on the first page).

## Scraping Each Recipe

Now that we have a list of URLs, we can now navigate to each page, wait for the result to appear, and give it to BeautifulSoup to gather the data we need!

For each recipe, the following code will gather:

- the name of the recipe
- the cooking time of the recipe
- the difficulty of the recipe
- the price range of the recipe
- the description of the recipe

We start with an empty list, `recipes`, that we will populate with a `dict`, storing the desired information about each recipe:


```python
from bs4 import BeautifulSoup

# [...]

recipes = []
for url in recipe_urls:
  print(f"Navigating to {url}")
  driver.get(url)
  wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='p-3 border bg-white rounded-lg recipe-container']")))

  soup = BeautifulSoup(driver.page_source, 'html.parser')
  name = soup.find('h2').string.strip()
  cooktime = soup.find('span', class_='recipe-cooktime').text.strip()
  difficulty = soup.find('span', class_='recipe-difficulty').text.strip()
  price = soup.find('small', class_='recipe-price').attrs.get('data-price').strip()
  description = soup.find('p', class_='recipe-description').text.strip()
  recipes.append({
    'name': name,
    'cooktime': cooktime,
    'difficulty': difficulty,
    'price': price,
    'description': description
  })
```

Finally, we can save the results in a CSV file using the techniques we learned earlier in the day:

```python
import csv

# [...]

with open('data/recipes.csv', 'w') as file:
  writer = csv.DictWriter(file, fieldnames=recipes[0].keys())
  writer.writeheader()
  writer.writerows(recipes)

driver.quit()
```

## Going Headless

Launching a web scraping script with Selenium opens a Google Chrome window which gets in the way and prevents you from doing anything else (you might have seen this, interacting with the page using the mouse or keyboard while the script is running breaks it). There's a solution for that: [Headless Chrome](https://developers.google.com/web/updates/2017/04/headless-chrome). The idea is to use Chrome without its user interface. This is how you can do it:

Replace this line:

```python
driver = webdriver.Chrome()
```

With the following lines:

```python
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
```

Add a few `print()` statements (as you won't see what's going on anymore!) and re-start:

```python
python test_advanced_scraping.py
```
