Let's recap the `git` commands you need to remember in order to work on the challenges during the bootcamp.

## Status

First, let's make sure that our working directory is **clean**:

```bash
git status
```

If you get the following result, then you're all set and can start working on this challenge:

```text
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
```

If you do not get this message, you need to first commit / clean some other challenges before you can start. Do not hesitate to raise a ticket to get some help from a TA over the first few days. `git` can be hard, so please do ask!

## First commit

Let's create a Python file:

```bash
touch today.py
```

Open this file in your text editor. You will need to declare and implement a function called `my_name_is`, which doesn't take any parameter and returns a constant of type `str`. The value of this constant will be your GitHub nickname.

Run `make` until one test passes (no need for the second one to be successful, we'll take care of it in a second).

```text
tests/test_git.py::TestGit::test_hi_my_name_is PASSED
tests/test_git.py::TestGit::test_my_buddy_is   FAILED
```

Good, you made some progress. It's time to pause and save your progression. Just like a checkpoint!

```bash
git add today.py
git commit -m "Implement my_name_is function"
git push origin master
```

Kitt should pick up the change and show 50% progress. Good job!

## Second commit

Let's start solving the second test. To do so, you need to declare and implement a function called `my_buddy_is`, which doesn't take any parameter and returns a constant `str`. The value of the constant will be your buddy's GitHub nickname (or yours if you don't have a buddy today :().

You can use this useful command to check what has changed in the file:

```bash
git diff
```

If you are satisfied, you can now commit & push to GitHub:

```bash
git add today.py
git commit -m "Implement my_buddy_is function"
git push origin master
```

## Making `pylint` happy

At this point of the challenge, you should have 3 style errors:

```text
C0114: Missing module docstring (missing-module-docstring)
C0116: Missing function or method docstring (missing-function-docstring)
C0116: Missing function or method docstring (missing-function-docstring)
```

You are missing [docstrings](https://www.python.org/dev/peps/pep-0257/). One for the module, and one for each function. A docstring gives context / documentation to a module or function.

To fix the first error, add a docstring on the **first line** of `today.py`:

```python
"""A module computing buddy pair names for the day"""
```

Run `make` again, you should have one less style error.

Repeat this by adding a [one-line docstring](https://www.python.org/dev/peps/pep-0257/#one-line-docstrings) for the two functions.


When you are done, time to perform the third commit of the challenge:

```bash
git diff
```

```bash
git add today.py
git commit -m "Fix style issues, should get a 'Good Style' now :pray:"
git push origin master
```

## Conclusion

You now know how to navigate Kitt, position yourself on a challenge, open it in a text editor and work on it, switching to the terminal to run `make` and some git commands. Congratulations!
