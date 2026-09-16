# PMLDL Assignment 1

MLOps pipeline for predicting median house values using the California Housing dataset.

The project contains three stages:

1. Data processing
2. Model training and evaluation
3. Model deployment

The stages are connected using DVC and the complete pipeline is automatically checked every 5 minutes using cron.

## Project Structure

```text
.
├── code
│   ├── datasets
│   │   ├── download_data.py
│   │   └── process_data.py
│   ├── models
│   │   └── train.py
│   └── deployment
│       ├── api
│       │   ├── Dockerfile
│       │   └── main.py
│       ├── app
│       │   ├── Dockerfile
│       │   └── app.py
│       └── docker-compose.yml
├── data
│   ├── raw
│   └── processed
├── models
├── dvc.yaml
├── run_pipeline.sh
└── requirements.txt
```

## Setup

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Data Engineering

The project uses the California Housing dataset from scikit-learn.

Download the raw dataset:

```bash
python code/datasets/download_data.py
```

Process the data:

```bash
python code/datasets/process_data.py
```

The processing stage removes missing values, removes outliers using the IQR method, and creates an 80/20 train-test split.

The processed datasets are saved to:

```text
data/processed/train.csv
data/processed/test.csv
```

## Model Engineering

The model is a `RandomForestRegressor` with 100 trees.

Train and evaluate it with:

```bash
python code/models/train.py
```

The following metrics are calculated:

* MAE
* RMSE
* R²

The experiment parameters, metrics, and model are also logged with MLflow.

Example results:

```text
MAE:  0.2931
RMSE: 0.4322
R2:   0.7769
```

The trained model is saved as:

```text
models/model.pkl
```

The model file is not stored in Git because it is larger than GitHub's file-size limit. It can be reproduced by running the training stage or the complete DVC pipeline.

## Deployment

The deployment consists of two separate Docker containers:

* FastAPI prediction API
* Streamlit web application

Build and start both containers:

```bash
sudo docker compose -f code/deployment/docker-compose.yml up -d --build
```

The services are available at:

```text
Web application: http://localhost:8501
API:             http://localhost:8000
API docs:        http://localhost:8000/docs
```

The Streamlit application sends the entered housing features to the FastAPI service and displays the predicted median house value.

## DVC Pipeline

The three stages are connected through DVC:

```text
process -> train -> deploy
```

Run the complete pipeline with:

```bash
dvc repro
```

DVC tracks dependencies between the stages and skips stages whose inputs have not changed.

## Automation

The pipeline is automatically checked every 5 minutes using cron.

The pipeline runner is:

```bash
./run_pipeline.sh
```

The cron configuration used for the project is:

```text
*/5 * * * * /home/abdullloh/PMLDL-A1/run_pipeline.sh
```

Every five minutes, cron starts the runner, which executes `dvc repro`. DVC then reruns the required stages when their dependencies have changed.

Pipeline output is written to:

```text
pipeline.log
```

## Stop Deployment

To stop the API and web application:

```bash
sudo docker compose -f code/deployment/docker-compose.yml down
```
