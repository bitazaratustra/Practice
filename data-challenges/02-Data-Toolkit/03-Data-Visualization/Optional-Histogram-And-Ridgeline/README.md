# Histogram and ridgeline plots
### Introduction

Same principle in this exercise, we are going to **recreate** plots from this [article](https://www.data-to-viz.com/story/OneNumOneCatSeveralObs.html).

To learn more **best practices** around bubble plots read these **short articles**.

[Density](https://www.data-to-viz.com/graph/density.html)
[Histogram](https://www.data-to-viz.com/graph/histogram.html)
[Ridgeline](https://www.data-to-viz.com/graph/ridgeline.html)

[Bin Size](https://www.data-to-viz.com/caveat/bin_size.html),
[Multiple Distribution](https://www.data-to-viz.com/caveat/multi_distribution.html)


### Dataset

You will work with the **CIA probability dataset**.

[Download here](https://raw.githubusercontent.com/zonination/perceptions/master/probly.csv)

### First steps

Create a notebook named `exercise05.ipynb` in the **same folder** as this **README**.
Now you can **import** the necessary **libraries**.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
```

Then **import** the **dataset** from the CSV you just downloaded.

### Density

Recreate this plot with **Plotly** in order to be able to **select** and deselect each **categories**.
Here the label are optional.

<img src="https://www.data-to-viz.com/story/OneNumOneCatSeveralObs_files/figure-html/unnamed-chunk-4-1.png" width="760">

### Histogram

Recreate this grid of histogram with **seaborn**.

Make sure the **category name** is displayed for each plot in the grid.

<img src="https://www.data-to-viz.com/story/OneNumOneCatSeveralObs_files/figure-html/unnamed-chunk-6-1.png" width="760">

### Ridgeline

Use **seaborn** to recreate this ridgeline plot.

The plot need to be **horizontal** and show the **category** for each line

<img src="https://www.data-to-viz.com/story/OneNumOneCatSeveralObs_files/figure-html/unnamed-chunk-7-1.png" width="760">
