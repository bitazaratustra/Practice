## Background & Objectives

Now it is time to make advanced SQL requests to an `ecommerce` database!

## Data
We will work with the `ecommerce.sqlite` database available at this URL:  
`https://wagon-public-datasets.s3.amazonaws.com/sql_databases/ecommerce.sqlite`

Using your preferred method, place the `ecommerce.sqlite` file in the `data` directory of this challenge.

## Specs

Open the file `queries.py` to answer the following questions. Don't forget you can look inside the database by using DBeaver.

There are three methods to implement:


- Implement `query_orders` to get all the orders by ascending OrderID.
- Implement `get_orders_range` to get all the orders made between two given dates by ascending OrderDate (excluding date_from and including date_to).
- Implement `get_waiting_time` to get all the orders with the delivery time in ascending order (from the smallest timedelta to the largest). 👌

👉 **As a reminder**: Each method takes a `db` argument, which is a connection to the database, on which you can call the `execute` method. This `db` is **built by the test and passed along to the function**. No need to create one yourself to satisfy `make`. As a reminder your method will look like this:

```python
def the_method(db):
    results = db.execute("YOUR SQL QUERY")
    results = results.fetchall()
    # results in a list (rows) of lists (columns)
    print(results)  # Inspect what you get back! Don't guess!

    # Then you'll need to return something.
    return ?
```

## Tools

You can use [DBeaver](https://dbeaver.io/) to visualize the database.
