# YOUR CODE HERE

@task
def preprocess_new_data(experiment):
    """
    Run the preprocessing of the new data
    """
    pass  # YOUR CODE HERE

@task
def evaluate_production_model(status):
    """
    Run the `Production` stage evaluation on new data
    Returns `eval_mae`
    """
    pass  # YOUR CODE HERE

@task
def re_train(status):
    """
    Run the training
    Returns train_mae
    """
    pass  # YOUR CODE HERE

def build_flow():
    """
    build the prefect workflow for the `taxifare` package
    """
    pass  # YOUR CODE HERE
