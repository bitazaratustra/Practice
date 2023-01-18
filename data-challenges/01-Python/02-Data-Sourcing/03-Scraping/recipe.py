
import sys
from os import path

import csv
import requests
from bs4 import BeautifulSoup

SEARCH_URL = "https://recipes.lewagon.com/"
PAGES_TO_SCRAPE = 3


def parse(html):
    ''' return a list of dict {name, difficulty, prep_time} '''
    soup = BeautifulSoup(html, "html.parser")
    return [parse_recipe(article) for article in soup.find_all('div', class_= 'recipe-details')]


def parse_recipe(article):
    ''' return a dict {name, difficulty, prep_time} modelising a recipe'''

    name = article.find('p', class_= 'recipe-name').string.strip()
    difficulty = article.find('span', class_= 'recipe-difficulty').string.strip()
    prep_time = article.find('span', class_= 'recipe-cooktime').string.strip()
    return {'name': name, 'difficulty': difficulty, 'prep_time': prep_time}


def write_csv(ingredient, recipes):
    ''' dump recipes to a CSV file `recipes/INGREDIENT.csv` '''

    with open(f'recipes/{ingredient}.csv', 'w') as recipe_file:
        keys = recipes[0].keys()
        writer = csv.DictWriter(recipe_file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(recipes)


def scrape_from_internet(ingredient, start=1):
    ''' Use `requests` to get the HTML page of search results for given ingredients. '''

    print(f"Scraping page {start}")
    response = requests.get(
        SEARCH_URL,
        params={'search[query]': ingredient, 'page': start}
        )

    if response.history:
        return None
    return response.text


def scrape_from_file(ingredient):
    file = f"pages/{ingredient}.html"
    if path.exists(file):
        return open(file)
    print("Please, run the following command first:")
    print(f'curl "https://recipes.lewagon.com/?search[query]={ingredient}" > pages/{ingredient}.html')
    sys.exit(1)


def main():
    if len(sys.argv) > 1:
        ingredient = sys.argv[1]
        recipes = parse(scrape_from_internet(ingredient))
        write_csv(ingredient, recipes)

        recipes = []
        for page in range(PAGES_TO_SCRAPE):
            response = scrape_from_internet(ingredient, page+1)
            if response:
                recipes += parse(response)
            else:
                break
        print(f"Wrote recipes to recipes/{ingredient}.csv")

    else:
        print('Usage: python recipe.py INGREDIENT')
        sys.exit(0)


if __name__ == '__main__':
    main()
