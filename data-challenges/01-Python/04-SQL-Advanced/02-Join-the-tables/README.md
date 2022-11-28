## Background & Objectives

Now we are going to dive into `JOIN` queries to read data from multiple tables. Again, [this picture](http://stackoverflow.com/questions/17946221/sql-join-and-different-types-of-joins) on `JOIN` queries is really helpful.

## Data
We know the drill, let's get that `ecommerce.sqlite` file in our `data` directory and let's get started. 

## Specs

👉 Complete the code in `join_queries.py`. Each method takes a `db` argument, which is a Cursor Object on which you can call the `execute` method. Exactly like in the previous exercise.

There are four methods to implement:

### Detailed Orders

👉 Implement `detailed_orders` to get the customer contact name and the employee first name of all the orders made.

### Spend per Customer

👉 Implement `spent_per_customer` to get the total amount spent per customer - in ascending order. 👌

### Who sells the most?

Implement `best_employee method` to determine who's the best employee! By "best employee", we mean the one who sells the most. 👑<br>
We expect the function to return a value like: `('FirstName', 'LastName', 6000 (the sum of all purchase))`. The order of information is irrelevant.

### Who doesn't buy anything?
Implement `orders_per_customer` to get the amount of Orders made by each Customer. As you can guess with the title, you should also display customers with no order?
