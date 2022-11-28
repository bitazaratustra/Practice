Once you are in the proper folder, please run:

```bash
jupyter notebook Recap.ipynb
```

---

In this reboot, we are going to use:

- The [Goodreads books](https://www.kaggle.com/jealousleopard/goodreadsbooks) dataset from Kaggle (a CSV to download)
- The [Open Library Books API](https://openlibrary.org/dev/docs/api/books)

The goal of this reboot is to load the data from the CSV + loop over rows to enrich each row with information such as:

- List of subjects (Science, Humor, Travel, etc.)
- The cover URL of the book
- Other information you'd find useful in the JSON API
