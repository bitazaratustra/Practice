
## Objective

Let's create your own toolbox package where you will store all the bits of code that you may want to reuse in the future.

Every time you implement a cool function you will add it to a file inside of your package and add a test function that will check if it works correctly.

## First steps

- Create a project with the `packgenlite` command (remember, all new projects go to `~/code/<user.github_nickname>`)
- Create a repository on GitHub for your package
- Start filling in your package with awesome functions you already used

## Examples

You can add to your repo:
- Feature preprocessing functions that you can use on Time, Distance, or Geohash
- Pipeline blocs
- Functions getting data from BigQuery/Storage
- Functions querying the Weather API
- Functions implementing PCA, Feature Selection, converting categorical features to numerical
- Functions evaluating a Regressor and a Classifier
- Functions implementing your favorite ARIMA forecasts
- Functions calling for help from your TAs
- Functions sending emails
- ...

Enjoy !

**NB: do not forget to add test functions such as**
`len(test_functions) == len(functions)`
