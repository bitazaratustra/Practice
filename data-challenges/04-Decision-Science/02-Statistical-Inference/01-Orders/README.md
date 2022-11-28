## Our approach

Before answering Olist's CEO request (_"how to improve business margin, given that bad reviews costs a lot of money ?"_), we should investigate what causes bad `review_score`.

A good practice for such problem is compute various intermediary tables called **Dimension Tables**, each containing **unique_id** for that dimension, and list **all possible properties of these dimensions** as columns.

For instance:
- `orders` table (**id**, review_score, amount, distance between seller and customer...)
- `sellers` table (**id**, mean_review_score, mean wait time, ...)
- `products` table: (**id**, mean_review score, categories, colors, sizes...)
- `customers` table (**id**, some properties of this customer)
- `reviews` table (**id**, translated text, properties of this text...)

You can think of these as training sets for machine-learning algorithms!

## Let's start with `Orders` 🏋🏽‍♂️

We will create a single DataFrame storing unique `order_id` as index, and all possible properties of these orders as columns.

We will save our logic needed to return a training set at the order level in `olist/order.py`. This will come in handy for our next modeling phase.

👉 Open `orders.ipynb` and follow the instructions
