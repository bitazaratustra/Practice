In this challenge, we will learn how to load data from a CSV file with pure Python.

## 🔥 Warm-up - Read CSV file line by line with the header

⚠️ For this warm-up, there is no `make` to run, so please read & follow the instructions closely!

Before we use a proper dataset, let's practice on something very simple. First, run the line below to download the CSV file we are going to use for this challenge.

```bash
curl https://wagon-public-datasets.s3.amazonaws.com/01-Python/02-Data-Sourcing/phone_book.csv > data/phone_book.csv
```

Now, open the `data/phone_book.csv` file and add some lines to it. Keep the header!

As an example, it should look like this:

```csv
first_name,last_name,phone_number
John,Lennon,123
George,Harrisson,456
Ringo,Starr,789
```

The goal now is to load that data into a Python script, to use it. We are going to use the [`csv`](https://docs.python.org/3/library/csv.html) built-in module.

Open the `phone_book.py` file and copy/paste the following code:

```python
import csv

with open('data/phone_book.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        print(row)
        line_count += 1
```

In your terminal, run the file:

```bash
python phone_book.py
```

Does that seem correct to you? What is the type of the `row` variable line 7 in the `print(row)` statement? Compare your guess with your buddy, and check the actual result with `type()` as well.


## Read CSV file line by line without header

In the previous example, we iterated through all the rows of the CSV file including the header. Suppose, however, that we want to skip the header and iterate over the remaining rows of the CSV file.
Try updating the code of `phone_book.py` to ignore the header (first line) and only print the last name + phone number. This is the output you should get:

```bash
Lennon: 123
Harrisson: 456
Starr: 789
```

## Read CSV file line by line using `csv` module `DictReader` object

Now try refactoring the code using the [`csv.DictReader`](https://docs.python.org/3/library/csv.html#csv.DictReader) class. You should no longer need the `line_count` variable. Also, what is the type of `row` now? Is it still the same as before? Which way do you think is the most readable? As usual, discuss the code with your buddy and check your understanding with `type()`.

After each question is solved please `add`/`commit`/`push` your code.

Have fun!
