
[//]: # ( challenge tech stack: vertex-ai workbench )

[//]: # ( challenge instructions )

## Vertex AI Workbench

Let's explore the **Vertex AI Workbench** as an alternative to **Compute Engine** for model training.

_Vertex AI Workbench_ provides managed virtual machines, allowing you to run ML code without having to precisely configure the environment for the code:
- _User-managed notebooks_ provide a customizable environment and allow you to specify package versions
- _Managed notebooks_ use custom containers, can be extended to read or write to BigQuery or cloud storage, and can be scheduled to run at set times

### Create a Workbench Instance

Create a workbench instance:
1. Access the [Vertex AI Workbench page](https://console.cloud.google.com/vertex-ai/workbench)
2. At the top, select the **USER-MANAGED NOTEBOOKS** tab and click on the blue **CREATE NOTEBOOK** button further below
3. Give your notebook the following name: _cloud-training-recap_
4. In the **Environment** section, set the operating system to **Ubuntu 20.04**
5. Still in this section, select **TensorFlow Enterprise 2.8 (with LTS and Intel® MKL-DNN/MKL)** as the environment
6. Scroll down and click on **CREATE**

👉 The workbench should be ready in a couple of minutes

Open the virtual machine
- Click on **OPEN JUPYTERLAB**
- Install [gh](https://github.com/cli/cli/blob/trunk/docs/install_linux.md) for _Ubuntu_

### Install zsh and oh-my-zsh

Install zsh:

``` bash
sudo apt-get install zsh
```

Install oh-my-zsh:

``` bash
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

### Authenticate on GitHub 1/2

Go to the workbench instance and open the Terminal.

Run the `gh auth login` command:
- Account: `GitHub.com`
- Protocol: `HTTPS`
- Authenticate Git with your GitHub credentials: `Yes`
- Authentication method: `Paste an authentication token`

### Create a GitHub Token

Create a GitHub token to allow the workbench to access your account:
1. Access [GitHub Tokens](https://github.com/settings/tokens)
2. Click on **generate new token**
3. Fill in the **Note** field with a meaningful name, such as _Vertex AI Workbench token_
4. Check that these scopes are enabled: 'repo', 'read:org', 'workflow'
5. Click on **generate token**
6. Copy the token (you will not be able to retrieve it later)

### Authenticate on GitHub 2/2

Paste the token in the Vertex AI instance's Terminal

### Clone your project repo

Clone your repo using the `HTTPS` URL:

``` bash
git clone https://github.com/gmanchon/cloud-data-recap-dm
cd cloud-data-recap-dm
cp .env.sample .env
nano .env
```

Edit the project configuration file:
- Set the data source as `DATA_SOURCE="big query"`
- Exit and save `Ctrl + X`, `Y`, `Enter`

Install `direnv`:

``` bash
curl -sfL https://direnv.net/install.sh | bash
eval "$(direnv hook zsh)"
direnv allow .
```

Install package:

``` bash
pip install -e .
mkdir -p training_outputs/params training_outputs/metrics training_outputs/models
```

Run the preprocessing and the training:

``` bash
make run_preprocess run_train
tree training_outputs
```

### New Workbench Terminal

Manually hook `direnv`:

``` bash
eval "$(direnv hook zsh)"
```

### Handling the `.env` in JupyterLab

The easiest solution is to manually define the environment variables from Python:

``` python
import os

os.environ["DATASET_SIZE"] = "10k"
os.environ["VALIDATION_DATASET_SIZE"] = "10k"
os.environ["CHUNK_SIZE"] = "2000"
os.environ["DATA_SOURCE"] = "local"
os.environ["MODEL_TARGET"] = "local"
os.environ["PREFECT_BACKEND"] = "local"
os.environ["PROJECT"] = "le-wagon-dsa"
```

## Compute Engine vs Vertex AI Workbench

In _Compute Engine_ we can see that the _Vertex AI Workbench_ uses a _Compute Engine_ instance behind the scenes:

<img src='https://wagon-public-datasets.s3.eu-west-1.amazonaws.com/data-science-images/07-ML-OPS/mlops/vertex-ai-compute-engine.png'>
