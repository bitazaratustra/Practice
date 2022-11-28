# Objective

Let's improve our model either by
- training it on a bigger sample
- tuning its hyperparameters

This last part obviously takes longer than the time you have left today, the aim of the exercise is for you to see how you can take advantage of GCP's big machines

## Deploy to GCP and evaluate performance

GCP AI Platform gives you the possibility to change machine types
🚨 Be careful, bigger machines are obviously more expensive 🚨

Try changing the machine types to speed the training up on a bigger sample
Check [GCP VM pricing](https://cloud.google.com/ai-platform/training/pricing?hl=fr), then add these parameters to your `gcp_submit_training` make command:

```bash
gcp_submit_training:
    @gcloud ai-platform jobs submit training ${JOB_NAME} \
    ... \
    --scale-tier CUSTOM \
    --master-machine-type n1-standard-16
```
Check [documentation](https://cloud.google.com/ml-engine/docs/machine-types) if needed

⚠️ Before launching training task, make sure you have set the correct parameters to your `Trainer()` class inside `trainer.py` (n_jobs=-1 for instance).


## HyperParameter tuning

If you have time try and run a RandomSearch on a larger data sample.
⚠️ Don't use more than 1 000 000 lines here, otherwise it will take too much time ⚠️

- Open `trainer.py`
- Implement a grid search using [RandomizedSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html) to find the best parameters for your estimator.
- Respect naming of parameters dict to feed to RandomizedSearchCV, check [medium article](https://medium.com/@yoni.levine/how-to-grid-search-with-a-pipeline-93147835d916)
- With a GBM model, you can search for the best `learning_rate` for example, while choosing a fixed value for number of trees.

How much did your model improve vs without grid search?
