## Objective

Understand how tests work and implement your first test.

Install the [code coverage](https://en.wikipedia.org/wiki/Code_coverage) package:

``` bash
pip install coverage
```

💡 The `coverage` package will be used by the `make` command when we `make test` in order to __assess the amount of code covered by the tests__. How does that work ? The `coverage` command installed by the package will verify whenever we run the tests how much of the code of the package gets executed. This gives us an indication of the risk of our program being buggy (0%: not great, 100% coverage: highly tested)

## Run tests

Create two new files:

```bash
touch mlproject/lib.py
touch tests/test_lib.py
```

and copy paste the below code into them:

```python
# mlproject/lib.py

def hello_world():
    return "Hello world from mlproject"
```

```python
# tests/test_lib.py
from mlproject.lib import hello_world

def test_length_of_hello_world():
    assert len(hello_world()) != 0
```

Inspect `Makefile`, and run:

```bash
make test
```

You just ran all the tests under `test/`.

👉 You might notice that `pytest` indicates that 2 tests ran successfully, while `lib_test.py` only contains one... If you want to avoid that, you need to update the `Makefile` so that `__init__.py` is not called by `pytest`. For example, you could continue to prefix all of your test files with `test_`, then modify the call to `pytest` in the `Makefile` using `tests/test_*.py`. Or you could run `python -m pytest` instead.

## Create your own test

You will now test the `haversine()` function:

- Create a `test_distance.py` file under `tests/` testing your `haversine()` function.
  *But what should I test? 🤔*
  You want to make sure the functionality of your function is correct. You can check if the distance between given coordinates is valid or if the type returned by it is the right one. It's up to you!

Run `make test` again and check if your test passes.
