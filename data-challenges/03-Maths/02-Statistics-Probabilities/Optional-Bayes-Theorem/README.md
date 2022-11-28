## Bayes Theorem - a manual proof

In this challenge, we have a dataset of 'Weather' conditions (Rain, Sunny, Overcast), and their corresponding ‘Play’ conditions (Yes or No), suggesting whether or not a sport should be played based on the weather conditions.

```python
weather_data= ['Sunny','Overcast','Rainy','Sunny','Sunny','Overcast','Rainy','Rainy','Sunny',
'Rainy','Sunny','Overcast','Overcast','Rainy']
play_data   =['No','Yes','Yes','Yes','Yes','Yes','No','No','Yes','Yes','No','Yes','Yes','No']
```
Where the index `i` in `weather` corresponds to the index `i` in `play`. For example, for the 2nd game, the weather was 'Overcast' and the game was played.

Our goal is to understand the probability of playing a match or not.

More precisely, we want to compute the probability **$P(play \mid weather)$** in order to anticipate if a new match will be allowed to take place on the next day given a new weather condition.

By doing so, we will also demonstrate the **Bayes Theorem** by calculating each of these 4 probabilities ourselves:

<img src='https://wagon-public-datasets.s3.amazonaws.com/data-science-images/math/bayes-theorem.png'>


Where :
- $P(play)$ is our **prior** belief on the probability of the class (Play = Yes or No) given all data we have seen so far
- $P(weather \mid play)$ is the **likelihood** of observing this type of weather, given whether or not the match was played
- $P(play \mid weather)$ is the **posterior** probability of actually playing or not, given the weather condition
- $P(weather)$ is a constant, from the point of view of our problem: it does not depends on the choice of playing or not

🚀 Let's start!

Open the `bayes_theorem.ipynb` notebook:

> jupyter notebook
