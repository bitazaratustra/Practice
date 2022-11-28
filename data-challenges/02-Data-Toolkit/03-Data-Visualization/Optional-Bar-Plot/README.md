# Bar plot

### Introduction

In this exercise we are going to **recreate** bar plots from this [article](https://www.data-to-viz.com/graph/barplot.html).
Read the **article** to **learn more** about bar plot.

And to learn more **best practices** around bar plot read these **3 short articles**.

[Hard Label](https://www.data-to-viz.com/caveat/hard_label.html),
[Grouped Bar](https://www.data-to-viz.com/caveat/grouped_bar.html),
[Color Selection](https://www.data-to-viz.com/caveat/color_com_nothing.html)


### Dataset

You will use a dataset about the **evolution** of **first name** popularity in the US.  
You can [download it here](https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/5_OneCatSevNumOrdered.csv)


### First steps

Open the notebook named `bar-plot.ipynb` in the **same folder** as this **README**.
**Import** the necessary **libraries**.

```python
import numpy as np
import pandas as pd
import matplotlib
%matplotlib inline
import seaborn as sns
```

Then **import** the **dataset** from the CSV you just downloaded.

### Simple bar plot

Create a simple bar plot of the **frequency** of each **name** overall.

### Grouped bar plot

Now let's re-create this plot from the article using **seaborn**.
Make sure you are using a similar **color palette**, the same **years** and **names**.

<img src="https://www.data-to-viz.com/graph/barplot_files/figure-html/unnamed-chunk-2-1.png" width="760">

### Stacked bar plot

Same thing here, recreate the following **stacked bar** plot using **matplotlib**.


<img src="https://www.data-to-viz.com/graph/barplot_files/figure-html/unnamed-chunk-3-1.png" width="760">
