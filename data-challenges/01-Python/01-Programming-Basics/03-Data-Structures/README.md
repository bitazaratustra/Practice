In this exercise, we will cover the most useful built-in data structures.
Before diving into the code, take some time to read the following:

- [Lists](https://docs.python.org/3.7/tutorial/introduction.html#lists), called _array_ in other languages
- [More on lists](https://docs.python.org/3.7/tutorial/datastructures.html#more-on-lists)
- [List Comprehensions](https://docs.python.org/3.7/tutorial/datastructures.html#list-comprehensions)
- [Tuples](https://docs.python.org/3.7/tutorial/datastructures.html#tuples-and-sequences)
- [Dictionaries](https://docs.python.org/3.7/tutorial/datastructures.html#dictionaries), called _hash_ or _hashmap_ in other languages
- [Looping Techniques](https://docs.python.org/3.7/tutorial/datastructures.html#looping-techniques) with the `for` keyword

All done? Let's code!

## Exercise

### Currencies

Let's build a currency converter in the `currencies.py` file. In this exercise, we will manipulate lists, dictionaries and tuples.

1. Create a new constant dictionary called `RATES` at the top of `currencies.py`. Keys will be 6-letter strings like `"USDEUR"`, `"GBPEUR"`, `"CHFEUR"`, and the values will be their rate stored as a simple Python [`float` number](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex). You can find this information on [Google](https://www.google.com/search?q=USDEUR)
2. Implement the `convert(amount, currency)` function. The first parameter is a **tuple** of two elements: a float and a currency (e.g. `(100, "USD")`). The second parameter is a `String`, the currency you want to convert the amount into.
3. You should _round_ the results.
4. When called with an unknown rate (e.g. `"RMBEUR"`), the `convert` function should return `None`.

Run the tests with:

```bash
make
```

You may notice some tests failing. Update your rates with the following values as results have been hard-coded in the tests:

- `USDEUR`: `0.85`
- `GBPEUR`: `1.13`
- `CHFEUR`: `0.86`
- `EURGBP`: `0.885`
