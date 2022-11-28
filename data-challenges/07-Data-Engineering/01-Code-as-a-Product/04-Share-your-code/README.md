## Objective

You have learned how to create a package, now we will see one of the benefits of packaging:
👉 Sharing a package with your colleagues

## How do I share my code ?

Remember the `packgenlite` package right ?
You were able to install it in your virtual environment by running:

```bash
pip install git+ssh://git@github.com/krokrob/packgenlite
```

Well, the parameter provided to `pip` is just the decorated URL address of the [packgenlite GitHub repo](https://github.com/krokrob/packgenlite). Follow the link and inspect its code... Very similar to the one of our packages 👌

Once `packgenlite` is installed, as with any package, you are able to import its modules in any python file or through ipython or a notebook:

```bash
from packgenlite.lib import get_data

get_data()
```

You are also able to play with its scripts. We will do the same thing with our package so that it allows you to share your code with other developers.


🤔 So why can't your classmates install your package by using:

```bash
pip install git+ssh://git@github.com/<user.github_nickname>/mlproject
```

👉 You haven't created a public GitHub repository for your package yet!

## Share your own library

You just saw how to opensource your package.

You will now share your package with all of your colleagues.

Your colleagues will install your package and run:

```python
from yourpackage.lib import try_me
```

Create a project with the `packgenlite` command:
- Create it outside of the `data-challenges` folder (`cd ~/code/<user.github_nickname>`)
- Name it as you please (avoid using dashes `-` or dots `.` in the name of your package, since this is against [package naming conventions](https://docs.python-guide.org/writing/structure/#modules) and makes importing your package harder)
- Create a `lib.py` file in the `yourpackage` directory

Your package should be structured as follows:

``` bash
.
├── MANIFEST.in
├── Makefile
├── README.md
├── notebooks
├── raw_data
├── requirements.txt
├── scripts
│   └── yourpackage-run
├── setup.py
├── tests
│   └── __init__.py
└── yourpackage
    ├── __init__.py
    ├── data
    └── lib.py
```

Then add some content:
- Add a `try_me()` function to the `lib.py` file
- Insert some code in that function, try to be creative 🎉
👉 Make sure that everything works correcly on your machine before sharing your code... You do not want other developers to discover your bugs before you 😉

## Now lets publish your code:

### Option 1 - using GH CLI (the hacker way)

Let's make sure our new package doesn't have any remote connections already:

```bash
git remote -v
```

Nothing should be returned in the terminal. If it does you may have created your new package inside an existing git hub repository! (...like `data-challenges`.)

Now it's time to use some terminal magic to create a new **public** repository on github linked to our local repository, run:

```bash
gh repo create
```

- enter a repository name (this should mirror your package name)
- enter a brief description of your package
- select public as the type
- enter Y to confirm


Let's check our remote connections again, this time we should see an _origin_ connection:

```bash
git remote -v
```

You can also view the repository directly on github with:

```bash
gh browse
```

🤔 Doesn't look like any of our code is there yet?  We still need to push our work from the local repository on our machine up to github!

```bash
git add .
git commit -m "Initial Push"
git push -u origin master
```


### Option 2 - manually create and link

- Create a [new public repository](https://github.com/new) on GitHub named after the name of your package
👉 The repository needs to be public, otherwise you will not be able to share your package easily with anyone...
- Follow the instructions in the `... or push an existing repository from the command line` section:

```bash
git remote add origin git@github.com:<user.github_nickname>/PACKAGE_NAME
git push -u origin master
```

🚨 Depending on the way `git` and `GitHub` are configured, the default branch of your repository may be called `master` or `main`:

The command line invite in your terminal will look either like:
``` bash
➜  yourpackage git:(master)
```

or like:
``` bash
➜  yourpackage git:(main)
```

👉 If your default branch is called main, use the command `git push -u origin main` instead 👌

Publish the `pip install` command on the slack channel of the batch, for your colleagues to install your package and run your function 🥳

💡 __the command should look like `pip install git+ssh://git@github.com/<user.github_nickname>/PACKAGE_NAME`__

Your colleagues must have done the same thing... Add all their packages to a `requirements.txt` file and test their functions 🔥

If you wish to do that:
- Create a `requirements.txt` file at the root of your project
- List the decorated URLs of the packages of your classmates in the file
- Learn more about [requirements files](https://pip.pypa.io/en/stable/user_guide/#requirements-files) and find out how to install all of the packages specified in the file in your virtual environment with a single command

<details>
  <summary markdown='span'><strong> 💡 Hint </strong></summary>

``` bash
pip install -r requirements.txt
```

</details>

Now that all their packages are installed in your virtual environment, write some code in order to call functions or classes from their packages.

## Bonus: Pypi, the last layer to Open Source

You can skip the following section as it is a pure bonus, but definitely worth reading.

This section is for your general knowledge and will not be useful until you really want to opensource a package.

You probably wondered how to install your package with the `pip install PACKAGE_NAME` command rather than `pip install git+ssh://git@github.com/<user.github_nickname>/PACKAGE_NAME`...

### Process to fully opensource your package:

- Create two accounts, one on [PyPI](https://pypi.org/account/register/) and one on [TestPyPI](https://test.pypi.org/account/register/)
💡 __PyPI allows to officially opensource your package. TestPyPI allows to test your package before pushing to PyPI__
- Follow [this tutorial](https://anweshadas.in/how-to-upload-a-package-in-pypi-using-twine/) in order to upload your package to PyPI using [twine](https://twine.readthedocs.io/en/latest/)
