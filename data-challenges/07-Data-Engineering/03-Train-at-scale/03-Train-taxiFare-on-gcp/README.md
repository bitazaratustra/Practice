# Objective

In the previous challenge, we trained a basic model on GCP. We will now integrate a complete pipeline and use the trained model to make a prediction - all in the cloud using GCP. No more hard work for your machine!

## Complete `TaxiFareModel/trainer.py` to be trainable and deployable to GCP

Here we go back with the pipeline including:
- Custom encoders
- Mlfow tracking on a remote server

Start from the `TaxiFareModel` package solution of `07-Data-Engineering/02-ML-Iteration/04-MLFlow-quickstart`, but feel free to use your own package as well.

Move the solution to the *projects directory*: `~/code/<user.github_nickname>`.

<details>
  <summary markdown='span'><strong> How to move it to the *projects directory* ? </strong></summary>


  ``` bash
  mv downloaded_solution_package ~/code/<user.github_nickname>/TFM_TrainAtScalePipeline
  cd ~/code/<user.github_nickname>/TFM_TrainAtScalePipeline
  ```
</details>


Modify the `get_data()` function and add a `save_model()` method inside `trainer.py` in order to:
- Get the training data from `Cloud Storage` (still working on 1k data sample for faster runs here)
- Upload your model to `Cloud Storage` just like in the last challenge

💡 For a better organization of your code you can create a new file `params.py` and move there all your variables (`BUCKET_NAME`, etc) which later on you will import in `data.py`, `trainer.py`, `encoders.py`, etc.

Take a step back and ask yourself what information is now stored inside of our `model.joblib` ?

💡 Now we have the `preprocessing` and `model` information stored in our model.joblib object.

## Test your workflow locally first

Let's run `make run_locally` on our local machine:
- Train on a few data samples first in order to verify that everything runs without any errors
- Verify that the trained `model.joblib` is correctly saved on `Cloud Storage`

Once everything is working correctly, make sure that the requirements in `requirements.txt` match the versions of the packages of the virtual environement and that you did not forget any package in the `requirements.txt`.

**This step is very important, most of your errors in the next section will be linked to mismatch between requirements on your machine and requirements you specified in `requirements.txt`.**

## Train your model on the AI Platform

Edit the `Makefile` and run `make gcp_submit_training` to train your model on GCP (go back to the previous exercise for the correct command and to be sure you've set all the required variables).

As before:
- Submit a first training task on a few data samples in order to verify that the code workflow runs correctly on the AI Platform
- Then submit a real training task on more data samples in order to benefit from the capacity of the AI Platform

## Use the trained model for predictions

Now, have a look at `predict.py` and specifically verify how we:
- Load a trained pipeline from `Cloud Storage`
- Apply predictions on test data samples

💡**The code is pretty much the same as yesterday. The only difference is that we get our `model.joblib` from `Cloud Storage` and not from our machine.**

Run and test it:

```bash
python predict.py
```

You just made your first prediction using a pipeline trained on the AI Platform ! 🚀
