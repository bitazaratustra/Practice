In this exercise, we are going to play around with the stock market API [iexcloud.io](https://iexcloud.io/).

The goal here is to get comfortable reading API documentation.

---

## Apple stock the last 3 months

Let's find the API documentation page of [iexcloud.io](https://iexcloud.io/)

<details><summary markdown='span'>Solution
</summary>
Documentation pages are often hidden in the footer or in some menu.<br/>
Typing <i>'the_website_name API documentation'</i> in the google search bar is a quick way to find it too.
<br>
solution: <a href="https://iexcloud.io/docs/api/">https://iexcloud.io/docs/api/</a>
</details>

### API setup

The endpoints of the API we want to use are protected **behind a paywall**.

As Le Wagon, we kindly provide you with a **proxy** to that API for you to use _only during the challenge today_. We trust you!

Here's how it works:

1. API would say: use `https://cloud.iexapis.com/stable/stock/aapl/stats?token=...`
1. Copy this URL, and replace `cloud.iexapis.com` with `iex.lewagon.com`
1. You can [try it now](https://iex.lewagon.com/stable/stock/tsla/stats)

### Using the API

Now let's find in the IEXCloud API the **URL** for the last 3 months of Apple stock prices.

When you find the URL copy and paste it in a new tab and look at the data you get from the API.
It should be a JSON looking like this:
<details><summary markdown='span'>Show example
</summary>

```js
[
    {
        date: "2014-04-17",
        open: 68.2926,
        high: 69.3117,
        low: 68.1875,
        close: 68.9414,
        volume: 71106721,
        unadjustedVolume: 10158103,
        change: 0.778798,
        changePercent: 1.143,
        vwap: 68.8375,
        label: "Apr 17, 14",
        changeOverTime: 0
    },
    {
        date: "2014-04-21",
        open: 68.9939,
        high: 69.8869,
        low: 68.8127,
        close: 69.7596,
        volume: 45668931,
        unadjustedVolume: 6524133,
        change: 0.8182,
        changePercent: 1.187,
        vwap: 69.5143,
        label: "Apr 21, 14",
        changeOverTime: 0.011868050257174998
    },
// [...]
]
```
</details>

⚠️ Take your time before reading the solution, finding what we want in an API documentation can usually take **10 to 15 minutes of reading**

<details><summary markdown='span'>Solution
</summary>
You can find this information here in the documentation:
<a href="https://iexcloud.io/docs/api/#historical-prices">https://iexcloud.io/docs/api/#historical-prices</a>
<br>
The URL is:
<pre>
https://iex.lewagon.com/stable/stock/aapl/chart/3m
</pre>
</details>

------

## Using API data in pandas

### Setup

For this exercise we will work in a Notebook.

```sh
jupyter notebook
```

Go ahead and **create** a new Python Notebook named `stock.ipynb` in the ~/code/<user.github_nickname>/{{local_path_to("02-Data-Toolkit/02-Data-Sourcing/01-Stock-Market-API")}} folder.

Start with the usual imports in the first cell:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
```

We will reuse the **API URL** for the **last 3 months of Apple stock prices** here.<br>
To make a **call** to the API you can use the following code:

```python
import requests

url = "YOUR_API_URL"
api_data = requests.get(url).json()
```

You can now **create a dataframe** `apple_df` from this data.

<br>
<details><summary markdown='span'>Solution
</summary>
<code>apple_df = pd.DataFrame(api_data)</code>
</details>

With this dataframe we can **plot** the evolution of the stock price.
But before doing that, we need to do 2 things:
- Convert the `date` column to a datetime object
- Set the `date` column as the index

### Converting the date to a datetime object

To do this, you can use `Pandas.to_datetime()`

- **pd.to_datetime** documentation: [http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html#pandas.to_datetime](http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html#pandas.to_datetime)
- **Format** documentation: [http://strftime.org/](http://strftime.org/)

<details><summary markdown='span'>Solution
</summary>
<code>apple_df['date'] = pd.to_datetime(apple_df['date'], format="%Y-%m-%d")</code>
</details>

### Set the date column as the index

To do this you can use the DataFrame method **set_index**

- documentation: [https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.set_index.html](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.set_index.html)


<details><summary markdown='span'>Solution
</summary>
<code>apple_df = apple_df.set_index('date')</code>
</details>

### Now we can plot 🎉

First let's plot with only the values in the **`close`** column

<details><summary markdown='span'>Solution
</summary>
<code>apple_df['close'].plot()</code>
</details>

Now we can make a plot with the values in the **`open`, `close`, `high`, and `low`** columns

<details><summary markdown='span'>Solution
</summary>
<code>apple_df[['open', 'close', 'high', 'low']].plot()</code>
</details>

As we can see, our plot is really hard to read. We can improve its readability with the `figsize` argument of the `plot()` method.
- documentation: [https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html)

<details><summary markdown='span'>Solution
</summary>
<code>apple_df[['open', 'close', 'high', 'low']].plot(figsize=(12,4))</code>
</details>

### Test your code!

Add and run the following cell to your notebook:

```python
from nbresult import ChallengeResult

result = ChallengeResult('apple',
    index_name=apple_df.index.name,
    index_type=apple_df.index.dtype,
    columns=apple_df.columns
)
result.write()
print(result.check())
```

You can `commit` and `push` your code :rocket:

---

## Back to the API

Let's find out what kind of data we can get from this API 🕵️‍♂️

### What is the URL for the:

1. Amazon stock prices since last year?
2. Facebook market cap?
3. Apple research and development spendings quarterly?
4. Most recent news about Tesla?
5. Performance of the 'Energy' sector?

<details><summary markdown='span'>All Solutions
</summary>
<ol>
    <li><code>https://iex.lewagon.com/stable/stock/amzn/chart/1y</code></li>
    <li><code>https://iex.lewagon.com/stable/stock/fb/stats</code></li>
    <li><code>https://iex.lewagon.com/stable/stock/aapl/financials</code></li>
    <li><code>https://iex.lewagon.com/stable/stock/tsla/news/last/1</code></li>
    <li><code>https://iex.lewagon.com/stable/stock/market/sector-performance</code></li>
</ol>
</details>

---

:bulb: Don't forget to **push your code to GitHub**

## (Optional) Plotting  _multiple_  line charts

We'd like to **compare** the evolution of the GAFA stocks (Google, Apple, Facebook, Amazon) by plotting them on the _same_ chart.
Reuse the code from above to build a dataframe with one column per stock and keeping the dates as the index.
Maybe you can use some normalization technique at `t = 0` to better compare the relative performance of each stock!
