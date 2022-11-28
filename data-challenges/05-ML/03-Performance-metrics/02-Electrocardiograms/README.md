# Electrocardiograms

## Download the dataset

The dataset is available [here](https://wagon-public-datasets.s3.amazonaws.com/Machine%20Learning%20Datasets/ML_Electrocardiograms_dataset.csv)). Let's download it and store it in the `data` folder in the `02-Electrocardiograms` directory with the following commands:

```bash
cd ~/code/<user.github_nickname>/{{local_path_to("05-ML/03-Performance-metrics/02-Electrocardiograms")}}
curl https://wagon-public-datasets.s3.amazonaws.com/Machine%20Learning%20Datasets/ML_Electrocardiograms_dataset.csv > data/electrocardiograms.csv
```

## The dataset

- Each obervation of the dataset is a numerically represented heartbeat, taken from a patient's electrocardiogram (ECG).
- The `target` is binary and defines whether the heartbeat is at risk of cardiovascular disease [1] or not [0].

## Exercise

🎯 Your task is to flag heartbeats that are at risk of cardiovascular diseases. You will:

- Investigate the class balance of the dataset
- Evaluate and compare two models: KNN and LogisticRegression
- Use Confusion matrix and Classification report to get insight on the models' performances
- Choose the optimal model based on the appropriate metric

To start the exercise, open `Electrocardiograms.ipynb` in `jupyter notebook` and follow the instructions.

🚀 Your turn!

