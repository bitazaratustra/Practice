## Background & Objectives

The goal of this challenge is to use [Window Functions](https://mode.com/sql-tutorial/sql-window-functions/) like `RANK` or `SUM` with the `OVER` keyword.

`OVER` clause can be used with:
- `PARTITION BY` to select the scoped rows
- `ORDER BY` to define the order of the rows in which the window function should be applied

## Data
We know the drill, let's get that `ecommerce.sqlite` file in our `data` directory and let's get started. 

## Specs

### Order rank per customer

- Implement `order_rank_per_customer` to rank the orders of each customer according to the order date.
- For each customer, the orders should be ranked in the chronological order.
- This function should return a list of tuples like (`OrderID`, `CustomerID`, `OrderDate`, `OrderRank`).

### Order cumulative amount per customer

- Implement `order_cumulative_amount_per_customer` to compute the cumulative amount (in USD) of the orders of each customer according to the order date.
- For each customer, the orders should be ranked in the chronological order.
- This function should return a list of tuples like (`OrderID`, `CustomerID`, `OrderDate`, `OrderCumulativeAmount`).

**Hint** There are two sums to compute here: the total amount for a given order and the cumulative amount of orders. Which one is a window function?

## Key learning points

- Window functions allow you to compute data from different rows **without aggregating the rows**.
- If you want to aggregate the rows, use `GROUP BY`.
- If you don't use, `OVER` with `PARTITION BY` and `ORDER BY` instead.
