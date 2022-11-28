## Background

In this challenge, we will learn the concepts of Mean, Mode, Median and Standard Deviation. In the file `basic_functions.py` there are four functions to implement. Each one of those functions will implement one of the aforementioned concepts.  Python has built-in libraries which can of course already compute these for us, but let's make sure we understand the underlying calculations by coding them ourselves.

## The Mean and Variance
The sample **mean** (mu) is the average and is computed as the sum of all the observed outcomes from the sample divided by the total number of events. Here's the formula:

$\mu = \frac{1}{N}\sum_{i=0}^{N}x_i$

The **standard deviation** (sigma) on the other hand is a statistical metric that describes the spread of the data, or how far the values are from the mean. Here's the formula:

$\sigma = \sqrt{\frac{\sum_{i=0}^N(x_i - \mu)^2}{N - 1}}$

Thanks to these definitions, implement the functions `my_mean(samples)` and `my_standard_deviation(samples)` in the file `basic_functions.py`. These functions take a list as parameters and return the mean and the standard deviation respectively.

## The Median

The median is the value separating the higher half from the lower half of a data sample (a population or a probability distribution). For a dataset, it may be interpreted as the **"middle" value**. For example, in the dataset `{1, 3, 3, 6, 7, 8, 9}`, the median is 6, the fourth largest, and also the fourth smallest, number in the sample. Note that the values in the sample are ordered.

One problem when using the mean, is that it often does not depict the typical outcome. If one element from the sample is very far from the rest of the sample (i.e. also called outliers), then the mean will be affected by this "unusual" data. That's why, in some cases, we use **the Median**.

Read this [wikipedia article](https://en.wikipedia.org/wiki/Median) to see how the **median** is computed.

Implement in the file `basic_functions.py` the function `my_median(samples)`. The function takes a list as a parameter and return the median of the list.

## The Mode

The mode of a set of data values is the value that appears most often. In other words, it is the value that is most likely to be sampled.

Read this [wikipedia article](https://en.wikipedia.org/wiki/Mode_(statistics)) to see how the **mode** is computed.

Implement in the file `basic_functions.py` the function `my_mode(samples)`.

## The Modes (Optional)

Sometimes, a set of data values can have more than one mode.

E.g. A distribution of grades

![grades_distribution](https://wagon-public-datasets.s3.amazonaws.com/data-science-images/math/grades.png)

Implement the function `my_multimodes(samples)` in the `basic_functions.py`

You can try it with:

```python
grades = [8,7,9,9,9,7,10,8,8,6,9,7,4,8,10,6,10,3,5,6,6,8,9,3,6,8,10,5,9,9,8,8,4,8,8,7,7,8,3,7,7,6,7,5,10,8,7,6,9,6,6,8,8,9,9,8,8,10,8,4,8,10,7,8,5,5,8,7,3,8,4,7,4,5,7,9,8,9,7,7,4,7,5,8,6,6,8,6,6,5,6,9,10,6,10,8,6,7,6,5,9,8,5,2,7,9,7,6,9,1,6,7,6,7,7,10,7,5,6,8,6,9,0,9,7,7,7,7,8,8,6,9,7,8,5,2,9,7,6,7,6,5,4]

my_multimodes(samples)
#=> [7, 8]
```
