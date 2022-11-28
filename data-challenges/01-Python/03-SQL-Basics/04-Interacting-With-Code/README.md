## Background & Objectives

The goal of this challenge is to query the database **from our Python code**.

## Data
We will work with the `movies.sqlite` database available at this URL:
`https://wagon-public-datasets.s3.amazonaws.com/sql_databases/movies.sqlite`

Download and save the database file in this challenge `data` directory.

**Alternatively** you can make a copy of the `movies.sqlite` located in the previous challenge `data` directory, using the command below:

```bash
cp ~/code/<user.github_nickname>/{{local_path_to("01-Python/03-SQL-Basics/03-Interacting-with-db")}}/data/movies.sqlite \
~/code/<user.github_nickname>/{{local_path_to("01-Python/03-SQL-Basics/04-Interacting-With-Code")}}/data/movies.sqlite
```

## Tool

For that we will use a library that comes with Python, called **sqlite3**.

To connect to the `movies.sqlite` database from **IPython** or from a Python file, use the following instructions:

```python
import sqlite3

conn = sqlite3.connect('data/movies.sqlite')
db = conn.cursor()
db.execute("YOUR SQL QUERY")
rows = db.fetchall()
print(rows)
# => list (rows) of tuples (columns)
```

## Specs

Open DBeaver, connect to the `data/movies.sqlite` database and use a SQL Editor to build and test the SQL queries which answer the following questions.

Once your satisfied with the results, copy-paste your queries in the dedicated function in the `queries.py` file.

**IMPORTANT**: Each function takes a `db` argument, which is a cursor connected to the database, on which you can call the `execute` function. This `db` is **built by the test and passed along to the function**. No need to create one yourself to satisfy `make`. Your function will look like this:

```python
def your_function(db):
    query = ""
    db.execute(query)
    results = db.fetchall()
    # results in a list (rows) of tuples (columns)
    print(results)  # Inspect what you get back! Don't guess!
    # Then you'll need to return something.
    return ?
```

### Number of directors

How many directors are in this database?

### List of directors

What is the list of all the names of all the directors sorted in alphabetical order? Return a list of names (as `str`ings).

### List of movies about "love"

What are the movies which contain the exact word "love" in their title, sorted in alphabetical order? Return a list of movie titles.

### Number of directors named like...

How many directors contain a word, given by a user, in their name?

### List of movies longer than...

What are the movies which are longer than a duration, given by a user, sorted in the alphabetical order? Return a list of movie titles.

## Tips

👉 When you take input from a user to build a SQL query, make sure you protect your SQL query from **SQL injection** with [parameter substitution](https://docs.python.org/3.7/library/sqlite3.html).

👉 SQL queries tend to get pretty long pretty quickly. In Python, you can use the [triple-quote](https://docs.python.org/3.2/tutorial/introduction.html#strings) syntax to write **multi-line** strings:

```python
query = """
    SELECT
      title,
      minutes
    FROM movies
    WHERE title LIKE "%Z%"
    ORDER BY title
    LIMIT 3
"""
rows = db.execute(query)
# [...]
```
