## Objective

Let's start the day with a **Warm-Up** challenge and a quick `SELECT` statement.

## Data
We will work with the `school.sqlite` database available at this URL:  
`https://wagon-public-datasets.s3.amazonaws.com/sql_databases/school.sqlite`

Using your preferred method, place the `school.sqlite` file in the `data` directory of this challenge.

## Database Discovery

Open the `data/school.sqlite` with DBeaver and have a look at the schema.

- How many tables do you have?
- For each table, what are the columns?

Once you are comfortable with the schema, let's write an SQL Query

## Students from a City

In DBeaver, open the SQL Editor and write an SQL query to select all students from `'Paris'`.

Once you are happy with your query, open the `school.py` file and put that SQL query into the Python file. We want this query to be **dynamic** (i.e. work with any city, given as a parameter to the `students_from_city` function), so don't forget to update it.

To test your code, don't run `make` just yet, instead try to run the code yourself:

1. Uncomment the lines at the bottom (from `import sqlite3`)
1. Open the terminal and run `python school.py`
1. Try with different values for the city argument (`'Paris'`, `'London'`, etc.)

If something feels weird, you can **debug** your code by adding a **breaking point** with:

```python
breakpoint()
```

That way you can inspect the local variables at the breaking point and check your assumption about the code (what variables hold what? what are the types?). Getting good as debugging code is a critical skill to develop throughout the bootcamp!

In the end, check your challenge with `make`. Be careful not to commit any `breakpoint()` as you would mess up the tests (locally and on Kitt!)

Have fun!
