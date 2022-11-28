## Objective

Create your first package called `mlproject`

## Your first package

Navigate outside of your `data-challenges` directory and create a new `mlproject`:

```bash
cd ~/code/<user.github_nickname>
packgenlite mlproject
```

The ultimate goals of our `mlproject` are:
- install it as a package
- install scripts

Get inside of `mlproject`
👉 Inspect the empty generated script in `scripts/mlproject-run`
👉 The code you want to package as a module will be placed in the directory `mlproject/`

You will want to install the dependencies of the package and its script.

To install the package, as seen in lecture, simply run:

```bash
pip install -e .
```

💡 Remember that the `-e` flag tells `pip` to create a symbolic link between the installation directory in the virtual env and the actual code of the package. Therefore the latest version of the code of your package will always be the one loaded on your machine.

💡 Whenever you load your package in __ipython or a notebook__ do not forget to `%load_ext autoreload` and `%autoreload 2` as well. This way the python interpreter will not cache the code or your package and the latest version of the code will be loaded whenever an import is ran.

💡 Thanks to the `setup.py` file, `pip` knows to install the dependencies of the package listed in the `requirements.txt` file.

💡 Once `mlproject` is installed using the `-e` flag on your machine, you __do not need to reinstall it__ in order for the changes in the code to be effective. The only case where you need to reinstall `mlproject` is if you __create new scripts__. Whenever you create a new script it needs to be linked to the virtual env. In this case, you need to `pip install -e .` again.

## Project as a package

Your `mlproject` is now a package, just like `pandas` or `sklearn`.

Go anywhere you want in your machine and run inside either an `ipython` or a `python` interpreter, or use a notebook, and run:

```python
import mlproject
```

For the moment the package does not contain much... But the import works.

## Project as scripts

You also have installed a script, let's test it directly in your terminal:
```bash
mlproject-run
```

For the moment the script does not do much... But it runs.

## Add a first module inside of the package

Create a new python file called `mlproject/distance.py` inside of which you will add the following function:

```python
from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # Radius of earth in kilometers. Use 3956 for miles
    return c * r
```

To check if your function works, a good practice is to add `if __name__ == "__main__"` at the end of `distance.py` and to compute a distance by calling the function:

```python
if __name__ == "__main__":
    # Le Wagon location
    lat1, lon1 = 48.865070, 2.380009
    #Insert your coordinates from google maps here
    #lat2, lon2 = x, y
    distance = haversine(lon1, lat1, lon2, lat2)
    print(distance)
```

🤔 [Here's a link](https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/) to understand what the condition above does if it is not clear...

Then run in your Terminal:

```bash
python -i mlproject/distance.py
```

If you see `>>>` in your terminal after running this commmand, it is completely normal. The `-i` stands for interactive mode. This means that you can explore the variables you created in your python script. To exit the interactive mode either type `exit()` or `CTRL-D`.

👉 Also, there seems to be an error when you run the code... Fix it before continuing 🙏

💡 __You can also use `%run mlproject/distance.py` inside of a notebook or ipython interpreter (do not forget to `import mlproject`, you must be located in the main `mlproject/`)__

Your new tree should look like this:

```bash
.
├── MANIFEST.in
├── Makefile
├── README.md
├── mlproject
│   ├── __init__.py
│   ├── data
│   └── distance.py
├── notebooks
├── raw_data
├── requirements.txt
├── scripts
│   └── mlproject-run
├── setup.py
└── tests
    └── __init__.py
```

Thanks to our initial installation using `pip install -e .` you can directly start using your new function anywhere you want.

```python
from mlproject.distance import haversine
```

👆You should now be able to use your `haversine` function in ipython or in a Jupyter Notebook.

## Fill the script of the package

The objective here is to implement a new script under `scripts/` called `mlproject-computedist` taking 4 parameters (long1, lat1, long2, lat2) and returning the corresponding haversine distance.

Install `termcolor` to allow your script to output colored text:

``` bash
pip install termcolor
```

In order to understand how to pass arguments to a script, you can inspect the code of the `computedist.py` file located in:

```bash
~/code/<user.github_nickname>/{{local_path_to("07-Data-Engineering/01-Code-as-a-Product/02-Package-installation")}}
```

Run :

```bash
python ~/code/<user.github_nickname>/{{local_path_to("07-Data-Engineering/01-Code-as-a-Product/02-Package-installation")}}/computedist.py --coords 48.865 2.380 48.235 2.393
```

Basically you will want to run the exact same command but without `python` and anywhere on your laptop.

In order to do that, simply:

1. Create a `scripts/mlproject-computedist` file with the exact same code as `computedist.py`
👉 __the name of a script file does not end with `.py`__
👉 Add the following lines at the beginning of the file. The first line specifies that the file is a python script. The second line specifies that the file is encoded using UTF-8 characters.

``` python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
```

Your new tree should look like:
```bash
.
├── MANIFEST.in
├── Makefile
├── README.md
├── mlproject
│   ├── __init__.py
│   ├── data
│   └── distance.py
├── notebooks
├── raw_data
├── requirements.txt
├── scripts
│   ├── mlproject-computedist
│   └── mlproject-run
├── setup.py
└── tests
    └── __init__.py
```

2. Modify `setup.py` in order to add `mlproject-computedist` to the list of scripts

Update your `setup.py` so that the script gets installed along with the package:

```python
from setuptools import find_packages
from setuptools import setup

with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content if 'git+' not in x]

setup(name='mlproject',
      version="1.0",
      description="Project Description",
      packages=find_packages(),
      install_requires=requirements,
      test_suite='tests',
      # include_package_data: to install data from MANIFEST.in
      include_package_data=True,
      scripts=['scripts/mlproject-run', 'scripts/mlproject-computedist'],
      zip_safe=False)
```

3. Reinstall the package so that `setup.py` notices the newly created script

```python
pip install -e .
```

You can now run your script anywhere on your machine:

```bash
mlproject-computedist --coords 48.865070 2.380009 48.235070 2.393409
```

To go further on parsing arguments, check [that link](https://realpython.com/python-command-line-arguments/)
