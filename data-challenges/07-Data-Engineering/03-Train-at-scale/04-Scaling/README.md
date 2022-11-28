# Scaling

The objective here is to sensitize to scaling issues and how to bypass certain challenges.

# Dataset size optimization

One of the main challenges when dealing with a large dataset is `memory` consumption.
If your dataset does not fit in RAM memory then it can lead to slower performances or even worse `out of memory ERROR`.

A first very simple trick to deal with this issue is to reduce the size of our dataset by optimizing the size of the types of the features.

Below example of different numpy casting:
```bash
int8	Byte (-128 to 127)
int16	Integer (-32768 to 32767)
int32	Integer (-2147483648 to 2147483647)
int64	Integer (-9223372036854775808 to 9223372036854775807)
float_	Shorthand for float64.
float16	Half precision float: sign bit, 5 bits exponent, 10 bits mantissa
float32	Single precision float: sign bit, 8 bits exponent, 23 bits mantissa
float64	Double precision float: sign bit, 11 bits exponent, 52 bits mantissa
```

By default :
- every float is stored under numpy `float64`
- every int as `int64`

Which in some cases is not optimized at all.
For instance downcasting a dataframe containing only integer columns in range [0:20] from `int64` to `int8` would decrease its size four times

## Exercise

Implement a function `df_optimized` optimizing the size of a dataset:

```python
def df_optimized(df, verbose=True, **kwargs):
    """
    Reduces size of dataframe by downcasting numeircal columns
    :param df: input dataframe
    :param verbose: print size reduction if set to True
    :param kwargs:
    :return: df optimized
    """
    in_size = df.memory_usage(index=True).sum()
    # Optimized size here
    for type in ["float", "integer"]:
        l_cols = list(df.select_dtypes(include=type))
        for col in l_cols:
            df[col] = pd.to_numeric(df[col], downcast=type)
            if type == "float":
                df[col] = pd.to_numeric(df[col], downcast="integer")
    out_size = df.memory_usage(index=True).sum()
    ratio = (1 - round(out_size / in_size, 2)) * 100
    GB = out_size / 1000000000
    if verbose:
        print("optimized size by {} % | {} GB".format(ratio, GB))
    return df
```

Now integrate size optimization to your Pipeline.

Here we might want to:
- Optimize the size right after loading the dataset
- Optimize the size after the preprocessing steps of our Pipeline (as usual add a custom Transfomer and add it as a step to your pipeline)

# Memory and parallelisation

It is the trickiest part of `scikit-learn` and Python in general which is not the best Python tool for fast and efficient parallelising tasks.

## Parallelisation
Here are the parameters you can play with on sklearn classes
- `n_jobs` inside `xgboost`, `RandomSearchCV` or `GridSearchCV` for example
👉 When possible, sklearn includes parallel tasks but keep in mind that not all algorithms are parallelisable

## Memory
Memory issues either appear when the size of a dataset is bigger than RAM size or during hyperparameters tuning when sklearn actually duplicates our data many times.

Here are the parameters you can play with on sklearn classes:

- `memory` parameter of sklearn's well known `Pipeline()`
👉 when given `memory="local_path"` to a pipeline, it will keep in cache all the transform parts applied during preprocessing
👉 Doc [here](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html)

- `pre_dispatch` inside `RandomSearchCV` or `GridSearchCV`
👉 From sklearn [doc](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html)

```python
Controls the number of jobs that get dispatched during parallel execution.
Reducing this number can be useful to avoid an explosion of memory consumption when more jobs get dispatched than CPUs can process.

This parameter can be:
- None, in which case all the jobs are immediately created and spawned. Use this for lightweight and fast-running jobs, to avoid delays due to on-demand spawning of the jobs
- An int, giving the exact number of total jobs that are spawned
- A str, giving an expression as a function of n_jobs, as in ‘2*n_jobs’
```

👉 good stackoverflow explanation [here](https://stackoverflow.com/questions/32673579/scikit-learn-general-question-about-parallel-computing)

## Exercise

We have provided the code integrating all these parameters
They are inside the `params` dictionary you feed to your `Trainer()` class:
```python
params = dict(nrows=10000,
              upload=True,
              local=False,  # set to False to get data from GCP (Storage or BigQuery)
              gridsearch=False,
              optimize=True,
              estimator="xgboost",
              mlflow=True,  # set to True to log params to mlflow
              experiment_name=experiment,
              pipeline_memory=None, # None if no caching and True if caching expected
              distance_type="manhattan",
              feateng=["distance_to_center", "direction", "distance", "time_features", "geohash"],
              n_jobs=-1) # Try with njobs=1 and njobs = -1
```
Play with the parameters `n_jobs`, and check the influence on time
