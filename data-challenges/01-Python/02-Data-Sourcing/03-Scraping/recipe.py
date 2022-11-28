# pylint: disable=missing-docstring,line-too-long
import sys
from os import path


def parse(html):
    ''' return a list of dict {name, difficulty, prep_time} '''
    pass  # YOUR CODE HERE

def parse_recipe(article):
    ''' return a dict {name, difficulty, prep_time} modelising a recipe'''
    pass  # YOUR CODE HERE

def write_csv(ingredient, recipes):
    ''' dump recipes to a CSV file `recipes/INGREDIENT.csv` '''
    pass  # YOUR CODE HERE

def scrape_from_internet(ingredient, start=1):
    ''' Use `requests` to get the HTML page of search results for given ingredients. '''
    pass  # YOUR CODE HERE

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
        recipes = parse(scrape_from_file(ingredient))
        write_csv(ingredient, recipes)
        pass  # YOUR CODE HERE
    else:
        print('Usage: python recipe.py INGREDIENT')
        sys.exit(0)


if __name__ == '__main__':
    main()
