
[//]: # ( presentation of the module )

## Welcome to the `TaxiFare` project team at `WagonCab` 🚕

In this module, you will impersonate a **ML Engineer** at `WagonCab`, a new taxi-app startup opening in New York!

`WagonCab` is willing to launch a new ML-product in production called `TaxiFare`. It's goal is to integrate into its app the prediction of the price of conventional taxi rides in new york, in order to show its user how much money they would gain by comparison!

Your company has at its disposal the huge public [NYC Trip Record Dataset](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page) which weights around 170 Go, and looks as follow

A team of **Data Scientists** has been staffed to create and fine-tune a machine learning model to predict the price of a ride.
They have been working in a isolated notebook context, hand-crafting & fine-tuning the best possible model, trained on a small, manageable subset of this dataset.

<img src='https://wagon-public-datasets.s3.amazonaws.com/data-science-images/07-ML-OPS/taxifare-head.png' width=400>


## Plan of the module (5 units)

**Unit 1) - Train at Scale**
- Understand data scientists' notebooks
- **Package** your python code
- Master your **IDE** (bye bye jupyter, hello VS Code)
- Train at scale (locally) via **incremental** processing techniques

**Unit 2) - Train on Cloud**
- Store model weights on **Google Cloud Storage**
- Store & query data on **Google Big Query**
- Use cloud power with **Google Compute Engine** (Virtual Machines)
- Use a cloud managed solution with **Google Vertex AI Workbench** (Jupyter Lab on the cloud)

**Unit 3) - Model Lifecycle**
- Store model versions and monitor performance with **MLflow**
- Retrain on fresh new data using **Prefect** to manage your DAG (Direct Acyclic Graph)

**Unit 4) - Predict in production**
- Develop your **API** with **FastAPI** and **uvicorn**
- Create a **Docker image** for your app
- Deploy Docker containers to production using **Google Cloud Run**

**Unit 5) - User interface**
- Develop a user interface with **Streamlit**
- **Plug** a user interface to your FastAPI
- **Deploy** your front end on **Streamlit Cloud** (or Cloud Run or Heroku)
