# Bonus

## Download the dataset

The dataset is available [here](https://wagon-public-datasets.s3.amazonaws.com/Machine%20Learning%20Datasets/ML_creditcard_fraud.csv). Let's download it and store it in the `data` folder in the `04-Bonus` directory with the following commands:

```bash
cd ~/code/<user.github_nickname>/{{local_path_to("05-ML/03-Performance-metrics/04-Bonus")}}
curl https://wagon-public-datasets.s3.amazonaws.com/Machine%20Learning%20Datasets/ML_creditcard_fraud.csv > data/creditcard.csv
```

## The dataset

Due to confidentiality issues, the original features of the dataset have been preprocessed and renamed `V1` to `V28`. There is only one features which has not been transformed, `Amount` which is the transaction Amount. `Class` is the target and it takes value 1 in case of fraud and 0 otherwise.

## Exercise

🎯 You are a Data Scientist for a bank. You are asked to develop a model that is able to detect at least 95% of fraudlent transactions. Go!

To start the exercise, open `Bonus.ipynb` in `jupyter notebook` and follow the instructions.

🚀 Your turn!


