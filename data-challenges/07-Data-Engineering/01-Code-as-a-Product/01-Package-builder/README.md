## Install Package builder with pip

Before doing anything here, please make sure _**you are inside of the `lewagon` virtual environment**_.

Now you can install the `packgenlite` tool:

```bash
pip install git+ssh://git@github.com/krokrob/packgenlite
```

As seen in this morning's lecture, quite a lot of things have happened. You have installed:
- the `packgenlite` package and its modules:
```python
from packgenlite.lib import get_data
get_data()
```
- the `packgenlite` script

This script will be your package builder.

# Use the package builder

Now let's suppose that you start a new ML project, you want to package your code somewhere.

You now have access to a cool script that you can run from anywhere on your laptop...

Go to `/tmp` to test the script, and build your first package:

```bash
cd /tmp && packgenlite first_project
```

Get inside you newly created package:

```bash
cd first_project
```

Below you can see the structure of the project that was generated.
Check how your package is structured by running `tree` in the terminal:

```bash
.
├── MANIFEST.in
├── Makefile
├── README.md
├── first_project
│   ├── __init__.py
│   └── data
├── notebooks
├── raw_data
├── requirements.txt
├── scripts
│   └── first_project-run
├── setup.py
└── tests
    └── __init__.py
```

In case `tree` is not installed you can run `brew install tree` for macOs and `sudo apt-get install tree` for Linux to install it on your machine.
