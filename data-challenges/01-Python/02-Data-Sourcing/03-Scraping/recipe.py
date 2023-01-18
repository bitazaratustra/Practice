# pylint: disable=missing-docstring,line-too-long
import sys
from os import path
# $DELETE_BEGIN
import csv
import requests
from bs4 import BeautifulSoup

SEARCH_URL = "https://recipes.lewagon.com/"
PAGES_TO_SCRAPE = 3
# $DELETE_END

def parse(html):
    ''' return a list of dict {name, difficulty, prep_time} '''
    # $CHALLENGIFY_BEGIN
    soup = BeautifulSoup(html, "html.parser")
    return [parse_recipe(article) for article in soup.find_all('div', class_= 'recipe-details')]
    # $CHALLENGIFY_END

def parse_recipe(article):
    ''' return a dict {name, difficulty, prep_time} modelising a recipe'''
    # $CHALLENGIFY_BEGIN
    name = article.find('p', class_= 'recipe-name').string.strip()
    difficulty = article.find('span', class_= 'recipe-difficulty').string.strip()
    prep_time = article.find('span', class_= 'recipe-cooktime').string.strip()
    return {'name': name, 'difficulty': difficulty, 'prep_time': prep_time}
    # $CHALLENGIFY_END

def write_csv(ingredient, recipes):
    ''' dump recipes to a CSV file `recipes/INGREDIENT.csv` '''
    # $CHALLENGIFY_BEGIN
    with open(f'recipes/{ingredient}.csv', 'w') as recipe_file:
        keys = recipes[0].keys()
        writer = csv.DictWriter(recipe_file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(recipes)
    # $CHALLENGIFY_END

def scrape_from_internet(ingredient, start=1):
    ''' Use `requests` to get the HTML page of search results for given ingredients. '''
    # $CHALLENGIFY_BEGIN
    print(f"Scraping page {start}")
    response = requests.get(
        SEARCH_URL,
        params={'search[query]': ingredient, 'page': start}
        )
    # We can check the reponse history to see if there is a re-direct
    if response.history:
        return None
    return response.text
    # $CHALLENGIFY_END

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
        # TODO: Replace scrape_from_file with scrape_from_internet and implement pagination (more than 2 pages needed)
        recipes = parse(scrape_from_internet(ingredient))
        write_csv(ingredient, recipes)
        # $CHALLENGIFY_BEGIN
        # recipes = []
        # for page in range(PAGES_TO_SCRAPE):
        #     response = scrape_from_internet(ingredient, page+1)
        #     if response:
        #         recipes += parse(response)
        #     else:
        #         break
        print(f"Wrote recipes to recipes/{ingredient}.csv")
        # $CHALLENGIFY_END
    else:
        print('Usage: python recipe.py INGREDIENT')
        sys.exit(0)


if __name__ == '__main__':
    main()
