## 🏅 Olympic Winter Games

Now that you have understood the basics of loading data from a CSV, let's work with a real [dataset from Kaggle](https://www.kaggle.com/the-guardian/olympic-games). Run the two lines below to download the datasets we need for this challenge:

```bash
curl https://wagon-public-datasets.s3.amazonaws.com/01-Python/02-Data-Sourcing/olympics_dictionary.csv > data/dictionary.csv
curl https://wagon-public-datasets.s3.amazonaws.com/01-Python/02-Data-Sourcing/olympics_winter.csv > data/winter.csv
```

Go ahead and open those two files in your text editor to try & understand what they contain. The goal of this challenge is to implement the method in `winter_olympic_games.py`:

1. Who won the most winter Olympic games medals (gold/silver/bronze) ever? (Hint: there's just one answer)
2. From `min_year` to `max_year`, which country won the most gold medals?
3. Find the three women with the most 5000 meters medals(gold/silver/bronze).

⚠️ For this challenge, you _can't_ use `pandas` yet 😉. Let's see how far you can go with just Python & the [`csv` module](https://docs.python.org/3/library/csv.html).

For this part of the challenge, you can use `make` to check your implementation of the three questions.

```bash
make
```

After each question is solved, please run the checks and `add`/`commit`/`push` your code. Don't wait to solve all three questions before doing so.
