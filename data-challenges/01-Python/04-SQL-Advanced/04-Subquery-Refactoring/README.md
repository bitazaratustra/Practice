## Background & Objectives

The goal of this challenge is to use [subquery factoring](https://modern-sql.com/feature/with) which allows you to nest SQL queries within a new one to reduce repetition and simplify complex SQL statements.

This syntax is the following:

```sql
WITH TemporaryTableName AS (
    -- PUT HERE A VALID QUERY LIKE:
    SELECT
      OrderID,
      ProductID,
      UnitPrice * Quantity ProductAmount
    FROM OrderDetails
)
SELECT
  OrderID,
  ProductID,
  ProductAmount
FROM TemporaryTableName

```
## Data
We know the drill, let's get that `ecommerce.sqlite` file in our `data` directory and let's get started. 

## Specs

### Average per customer

- Implement `get_average_purchase` to get the average amount spent per order for each customer, ordered by `CustomerID`.
- This function should return a list of tuples like (`CustomerID`, `AverageOrderedAmount`).

### General average

- Implement `get_general_avg_order` to get the average amount spent per order
- This function should return a simple `float`.

### Best customers

Now let's find the customers who spent more than the average - that is, their average amount spent per order is greater than the general average amount spent per order.

Can you see that the main part has already been done in the 2 previous questions? Let's use our previous queries thanks to the `WITH` clause.

- Implement `best_customers` to get the customers who have an average ordrer greater than the general average order, sorted by descending average ordered amount.
- This function should return a list of tuples like (`CustomerID`, `AverageOrderedAmount`).

### Top ordered products

- Implement `top_ordered_product_per_customer` to get the list of the top ordered product (in terms of amount of money not quantity) by each customer, based on the total ordered amount in **USD** and sorted decreasingly.
- This function should return a list of tuples like (`CustomerID`, `ProductID`, `OrderedAmount`).

### Average number of days between orders

- Implement `average_number_of_days_between_orders` to get the average number of days between two consecutive orders of the same customer.
- This function should return a simple `int`.

## Key learning points

- Subquery factoring allows you create temporary tables which you can then query.
- Use it to decompose a complex query into simpler subqueries!
