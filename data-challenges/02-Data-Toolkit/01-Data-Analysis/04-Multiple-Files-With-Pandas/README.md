It's very common that the data we need is scattered around many files, especially CSVs. Or it could be that it's in one file but in multiple worksheets. So far we have been using the [`pandas.read_csv()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) function which is straightforward: give it a CSV, and it will create a dataframe with all columns and rows found in the CSV.

When you have multiple files, it's a bit different. Sure you can load 10 files into 10 different dataframes, but what if you want to **reconciliate** the data? Welcome to the wonderful world of **Pandas Merging**.

## Context & Documentation

Pandas provides three functions to "add" two dataframes:

- [`pandas.concat()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html)
- [`pandas.DataFrame.merge()`](https://pandas.pydata.org/pandas-docs/version/0.22/generated/pandas.DataFrame.merge.html)
- [`pandas.DataFrame.join()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.join.html)


Everything is explained in the [Merge, join and concatenate](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html) article of the documentation, still it's a _very_ (very!) long article that can't really be read at once hoping to understand/remember everything.

## A bit of Theory

Before we load actual CSVs and try to merge/join/concatenate them, we are going to work with Dataframes created from dictionaries. This will limit the amount of data we manipulate and will make the concepts easier to understand.

Open the `multiple_files.ipynb` notebook in this exercise folder and start with the usual following `import` as the first cell:

```python
import numpy as np
import pandas as pd
import matplotlib
```
Insert a new **markdown** cell in your notebook:

```markdown
## Merge Practice
```
Then let's create a first DataFrame storing information about Countries picked up on Google:

```python
a_df = pd.DataFrame({
    'Country': ['Germany', 'France', 'Belgium', 'Finland'],
    'Population (M)': [82.8, 67.2, 11.4, 5.5],
    'Capital': ['Berlin', 'Paris', 'Brussels', 'Helsinki']
})
a_df
```

Let's suppose we now have a table of [HDI](https://en.wikipedia.org/wiki/Human_Development_Index), in a new cell:

```python
b_df = pd.DataFrame({
    'Country': ['Germany', 'France', 'Belgium', 'Canada'],
    'HDI': [0.936, 0.901, 0.916, 0.926]
})
b_df
```

### Inner Merge
Insert a new **markdown** cell in your notebook:

```markdown
### Inner Merge Practice
```

Try to [**`merge`**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html) `a_df` and `b_df` resulting in a dataframe that has no `null` values. Assign the merged dataframe to a variable called `inner_merged_df`.  Read the documentation for the function, especially about the `on` parameter. Which option should it be? Just pass this argument, and no others, what can you say about Canada? Finland?

### Test your code

Add a new **markdown** cell:

```markdown
#### Check your code
```

and then a code cell to test your new dataframe:

```python
from nbresult import ChallengeResult

result = ChallengeResult('inner_merge',
    inner_merged_shape=inner_merged_df.shape,
    inner_merged_nulls=sum(inner_merged_df.isnull().sum())
)
result.write()

print(result.check())
```

We just performed an **inner** merge, meaning that we **only** kept the rows that had a value in the `Column` we merged on that exists in both`a_df` and `b_df`.

![](https://res.cloudinary.com/wagon/image/upload/v1562058697/inner_ugz2wa.png)

In our example, the `a_df` has a line about `Finland` but `b_df` does not, so this row is not included in the inner merge. Same thing for `Canada`, it's present in `b_df` but not in `a_df` so it's not present in the inner merge.


#### Left Merge

There are four possible merges, the previous section covered the _inner_ merge. Let's try to do the **left** merge:

![](https://res.cloudinary.com/wagon/image/upload/v1562058697/left_jrs58n.png)

Insert a new **markdown** cell in your notebook:

```markdown
### Left Merge Practice
```

Create a new cell and build the `left_merged_df` variable where `a_df` is treated as the "left" dataset. What do you see? What about `Finland`? `Canada`?

### Test your code

Add a new **markdown** cell:

```markdown
#### Check your code
```

and then a code cell to test your new dataframe:

```python
from nbresult import ChallengeResult

result = ChallengeResult('left_merge',
    left_merged_shape=left_merged_df.shape,
    left_merged_nulls=sum(left_merged_df.isnull().sum())
)
result.write()

print(result.check())
```

### Right Merge

You probably get where we are going now. We just did a _left_ merge, so now let's have a look at the **right** merge!

![](https://res.cloudinary.com/wagon/image/upload/v1562058696/right_lm5ivj.png)

Insert a new **markdown** cell in your notebook:

```markdown
### Right Merge Practice
```

Same idea, create a new cell and build the `right_merged_df` variable still treating `a_df` as your "left" dataset. What do you see? What about `Finland`? `Canada`?

### Test your code

Add a new **markdown** cell:

```markdown
#### Check your code
```

and then a code cell to test your new dataframe:

```python
from nbresult import ChallengeResult

result = ChallengeResult('right_merge',
    right_merged_shape=right_merged_df.shape,
    right_merged_nulls=sum(right_merged_df.isnull().sum())
)
result.write()

print(result.check())
```


### Outer Merge

Finally, there is a merge which will keep **all** the rows from both `a_df` and `b_df`, the **outer** merge.

![](https://res.cloudinary.com/wagon/image/upload/v1562058696/outer_q76gh9.png)

Insert a new **markdown** cell in your notebook:

```markdown
### Outer Merge Practice
```

Then create a new cell and build the `outer_merged_df`.

### Test your code

Add a new **markdown** cell:

```markdown
#### Check your code
```

and then a code cell to test your new dataframe:

```python
from nbresult import ChallengeResult

result = ChallengeResult('outer_merge',
    outer_merged_shape=outer_merged_df.shape,
    outer_merged_nulls=sum(outer_merged_df.isnull().sum())
)
result.write()

print(result.check())
```

:information_source: Pandas has a whole article in the documentation about [Working with missing data](https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html). Again it's a pretty long article that you don't need to read now, but keep it in mind next time you are exploring a Dataset with a lot of `NaN`.

---

### Join

The `merge` function was useful to merge based on a given **column**. We will now see another use case where you want to merge based on the **index** (the rows).

Insert a new **markdown** cell in your notebook:

```markdown
## Join Practice
```

Next, let's create two new dataframes `aa_df` and `bb_df`, updating our `Country` column to be the new index.

```python
aa_df = a_df.set_index("Country")
aa_df
```

```python
bb_df = b_df.set_index("Country")
bb_df
```

Let's now use [`pandas.DataFrame.join()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.join.html):

```python
aa_df.join(bb_df)
```

:question: What's your conclusion? Was it a left, right, inner or outer join?

<details><summary markdown='span'>View solution
</summary>

By default, `.join()` does a **left** join. Try the other types of join:

```python
aa_df.join(bb_df, how='inner')
aa_df.join(bb_df, how='right')
aa_df.join(bb_df, how='outer')
```

</details>

:question: You see that `.merge()` and `.join()` give the same outcome in the end. So when should you use one or the other?

<details><summary markdown='span'>View solution
</summary>

You can use `.merge()` when you want to merge based on a given **column** and `.join()` when you want to join on the **index**.

</details>

---

### Concat

There's a third way to put two dataframes together, using [`pandas.concat()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html). Let's jump right into it:

Insert a new **markdown** cell in your notebook:

```markdown
## Concat Practice
```

```python
concat_df = pd.concat([a_df, b_df], axis="index", sort=False)
concat_df
```

This method is a bit more "dumb", it just combines the two dataframes into one by **stacking** their rows. This might prove useful in some situations though, so it's worth to know how to use it.

---

## Loading data from multiple CSVs

Let's put our new skills to the test.  To practice loading multiple CSVs and merging them, we're going to use the [Olympic Sports and Medals, 1896-2014](https://www.kaggle.com/the-guardian/olympic-games) which contains 3 files:

- `dictionary.csv`
- `summer.csv`
- `winter.csv`

1. Download these three files from Kaggle
2. Place them in your current folder (which should be `~/code/<user.github_nickname>/{{ local_path_to("02-Data-Toolkit/01-Data-Analysis/04-Multiple-Files-With-Pandas") }}`)

Let's continue to keep our work clean and insert a new **markdown** cell in your notebook:

```markdown
## Olympic Sports and Medals, 1896-2014
```

Go ahead and write the code to load:
- `dictionary.csv` into a dataframe called `countries_df`
- `summer.csv` into a dataframe called `summer_df`
- `winter.csv` into a dataframe called `winter_df`

On which column should we merge `countries_df`, `summer_df`, and `winter_df`?


<details><summary markdown='span'>Hint
</summary>

You will have to use [`pandas.DataFrame.rename()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rename.html) function on your winter and summer dataframes.

</details>

### Merging the data

insert a new **markdown** cell in your notebook:

```markdown
### Combining The Data
```

Time to perform a merge of `countries_df` and `summer_df` (into a new dataframe `summer_countries_df`). As we'll want to merge all games into one DataFrame at the end, **add a `Season`** column to the `summer_countries_df`.

Repeat the same approach to create a `winter_countries_df`, be sure to **add a `Season`** column.

Now we can concatenate `summer_countries_df` and `winter_countries_df` (they have the same columns!) into an `all_df` DataFrame.

### Test your code

Add a new **markdown** cell:

```markdown
#### Check your code
```

and then a code cell to test your new dataframe:

```python
from nbresult import ChallengeResult

result = ChallengeResult('all_df',
    all_df_shape=all_df.shape,
    all_df_columns=set(all_df.columns)
)
result.write()

print(result.check())
```

### Top 10 Countries since 1984

insert a new **markdown** cell in your notebook:

```markdown
### Top Countries Analysis
```

Use boolean indexing, grouping & sorting to create a new dataframe consisting of the Top 10 countries who won the most **total** medals _since 1984_.
- Save it in a variable named `top_10_df`
- The dataframe should consist of ten rows and one column named `Medal Count`

To plot the result with a barchart you can do:

```python
top_10_df.plot(kind="bar");
```


### Test your code

Add a new **markdown** cell:

```markdown
#### Check your code
```

and then the code to test your dataframe:

```python
from nbresult import ChallengeResult

result = ChallengeResult('olympic_games',
    top_country_1=top_10_df.iloc[0]['Medal Count'],
    top_country_10=top_10_df.iloc[9]['Medal Count']
)
result.write()

print(result.check())
```


### Top 10 Countries (by Season) since 1984

Let's take the analysis one step further, this time we don't just want to count the total number of medals for each country, we want to count the number of medals for Winter Games on the one hand, and for Summer Games on the other hand. Then we want to plot them (sorting should still be based on the _total_ number of medals).

- The dataframe should be saved as a variable called `top_10_season_df`
- The dataframe should have 10 rows and 3 columns named `Summer` `Winter` `Total`

:bulb: **Hint 1** The [`pandas.DataFrame.groupby()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html) can group over a **`list`** of columns.

:bulb: **Hint 2** You need to use the [`pandas.DataFrame.unstack()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.unstack.html) function

To plot the result with a barchart you can do:

```python
top_10_season_df[['Summer', 'Winter']].plot(kind="bar");
```

### Test your code

Add a new **markdown** cell:

```markdown
#### Check your code
```

and then the code to test your dataframe:

```python
from nbresult import ChallengeResult

result = ChallengeResult('olympic_games_season',
    top_country_season_shape=top_10_season_df.shape,
    top_country_1_summer=top_10_season_df.iloc[0]['Summer'],
    top_country_10_winter=top_10_season_df.iloc[9]['Winter']
)
result.write()

print(result.check())
```


### Optional - Top 10 Countries event wins since 1984

If you are a big fan of the olympics you may have noticed that the medal counts don't look quite right.  Add a new cell into your notebooks and run the following:

```python
all_df[(all_df.Year==2008) & (all_df.Event=='Basketball') & (all_df.Medal=='Gold')]
```

It looks like team sports are being overcounted in our analysis.  How can we remove the additional rows for team sports?

Create a new dataframe showing the top ten countries by total **event** wins _since 1984_.

- assign the new dataframe to a variable named `top_10_events_df`
- The dataframe should have 10 rows and 1 column called `Event Count`

:bulb: **Hint 1** The [`pandas.DataFrame.drop()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html) can help us remove columns that are too specific for our analysis.

:bulb: **Hint 2** With a more generalized dataset we can get help from the [`pandas.DataFrame.drop_duplicates()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html) function

Once complete view your results with:

```python
top_10_events_df.plot(kind='bar');
```

### Test your code

Add a new **markdown** cell:

```markdown
#### Check your code
```

and then the code to test your dataframe:

```python
from nbresult import ChallengeResult

result = ChallengeResult('olympic_games_event',
    top_country_event_shape=top_10_events_df.shape,
    top_country_1_event=top_10_events_df.iloc[0]['Event Count'],
    top_country_10_event=top_10_events_df.iloc[9]['Event Count']
)
result.write()

print(result.check())
```

### Optional - Merged results

Combine the `top_10_events_df` and `top_10_df` into a new dataframe named `top_10_combined`.  Combine them in a way which will include all countries that rank in **either** the top 10 for medal wins or top 10 for event wins, sort the dataframe by total `Medal Count`.

Plot your findings
```python
top_10_combined.plot(kind='bar');
```

### Test your code

Add a new **markdown** cell:

```markdown
#### Check your code
```

and then the code to test your dataframe:

```python
from nbresult import ChallengeResult

result = ChallengeResult('olympic_games_combined',
    top_combined_shape=top_10_combined.shape,
    top_combined_1_event=top_10_combined.iloc[0]['Event Count'],
    top_combined_1_medal=top_10_combined.iloc[0]['Medal Count'],
    top_combined_10_event=top_10_combined.iloc[9]['Event Count'],
    top_combined_10_medal=top_10_combined.iloc[9]['Medal Count']
)
result.write()

print(result.check())
```
