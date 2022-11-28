# Threshold Adjustments

## Download the dataset

The dataset is available [here](https://wagon-public-datasets.s3.amazonaws.com/Machine%20Learning%20Datasets/ML_Player_performance.csv). Let's download it and store it in the `data` folder in the `03-Threshold-Adjustments` directory with the following commands:

```bash
cd ~/code/<user.github_nickname>/{{local_path_to("05-ML/03-Performance-metrics/03-Threshold-Adjustments")}}
curl https://wagon-public-datasets.s3.amazonaws.com/Machine%20Learning%20Datasets/ML_Player_performance.csv > data/player_performances.csv
```

## The dataset

- Each observation represents a player
- Each column a characteristic of performance
- The target `target_5y` defines whether the player has had a professional career of less than 5 years [0] or 5 years or more [1].

## Exercise

🎯 In this exercise, you are the Data Scientist of a professional basketball team.

The coach wants you to help him in the recruitment process. He needs you to identify players that will last 5 years minimum as professionals. He does not want to take any risks though, and warns you that he wants a 90% guarantee that any player you send his way would actually last 5 years as a pro.

To start the exercise, open `Threshold-Adjustments.ipynb` in `jupyter notebook` and follow the instructions.

🚀 Your turn!


