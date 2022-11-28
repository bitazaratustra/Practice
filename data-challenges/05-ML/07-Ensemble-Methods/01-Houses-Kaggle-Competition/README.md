<img src='https://wagon-public-datasets.s3.amazonaws.com/data-science-images/ML/kaggle-batch-challenge.png' width=600>

Welcome to your first Kaggle Competition!

Your objective is to **submit online an answer** to the open competition 🔥

Your whole class will compete as a group against the team of TAs!

Download the datasets in the `data` folder and upgrade sklearn to its latest version

```bash
cd ~/code/<user.github_nickname>/{{local_path_to("05-ML/07-Ensemble-Methods/01-Houses-Kaggle-Competition")}}
curl https://wagon-public-datasets.s3.amazonaws.com/houses_train_raw.csv > data/train.csv
curl https://wagon-public-datasets.s3.amazonaws.com/houses_test_raw.csv > data/test.csv
curl https://wagon-public-datasets.s3.amazonaws.com/houses_sample_submission.csv > data/sample_submission.csv
pip install --upgrade pip
pip install --upgrade scikit-learn
```

Open `houses_kaggle_competition.ipynb` and follow instruction
