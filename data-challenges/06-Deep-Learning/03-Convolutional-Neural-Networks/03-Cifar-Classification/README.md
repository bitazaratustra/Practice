# CIFAR Classification
This exercise will strengthen your CNN skills by exploring the ***CIFAR-10 dataset***, which contains images from 10 different categories. You will also learn data augmentation techniques that may help to improve a model's performance.

## 🚨 Open this notebook on Google Colab 🚨
- ❗️ You will need to login to your a Google account to use it
- Go to [https://colab.research.google.com/](https://colab.research.google.com/)
- Choose to upload `cifar_classification.ipynb`.
 <img src='' width=300>
- This will create a copy of your notebook stored on your Google Drive in a folder called `Colab Notebooks`
- Then, **change the runtime type to GPU ("Runtime --> Change runtime --> GPU")**


## Why Colab?
Even quite small images and standard architectures lead to very long computational times. This is because, by default, neural networks are run on your CPU. GPUs, however, can compute large operations in parallel, which is what we are interested in as within each batch, it is theoretically possible to compute the transformation of all the images in parallel (actually, the backpropagation has to be done on all the images at the same time, so no real parallelization here). Let's use Google Colab to accelerate the convergence of CNN models thanks to Google's GPUs.

## What is Google Colab?
Google Colab is nothing more than a way to have online notebooks, with the possibility to use Google's GPUs. The idea here is not to use it in production (as there are some limitations) but to use Google Colab to test and prototype new algorithms. This free access to GPUs allows you to accelerate the computational time.

