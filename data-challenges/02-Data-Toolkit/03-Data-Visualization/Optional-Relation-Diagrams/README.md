# Optional - Relation diagram
### Introduction

Congratulations for reaching the optionals 🎉, we will now experiment with more **exotic plots**!
Same principle in this exercise, we are going to **recreate** plots from this [article](https://www.data-to-viz.com/story/AdjacencyMatrix.html).

To go further and learn more best practices you can read this **article**.

[Heatmaps](https://www.data-to-viz.com/graph/heatmap.html)

### Dataset

You will work with the **world migration** dataset.

[Download here](https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/13_AdjacencyDirectedWeighted.csv)

### First steps

Open the `relational_diagram.ipynb` notebook in the **same folder** as this **README**.
Now you can **import** the necessary **libraries**.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
```

Then **import** the **dataset** from the CSV you just downloaded.

### Sankey diagram with plotly

Recreate this interactive plot with [Plotly's Sankey diagram](https://plot.ly/python/sankey-diagram/)

<img src="https://i.ibb.co/XWvYpvT/Screen-Shot-2019-10-16-at-11-19-33.png" width="560">

### Heatmaps

Try to reacreate an heatmap either in [Seaborn](http://seaborn.pydata.org/generated/seaborn.heatmap.html) or with [Plotly](https://plot.ly/python/heatmaps/).

<img src="https://i.ibb.co/tQrTP05/Screen-Shot-2019-10-16-at-11-29-20.png" width="560">


