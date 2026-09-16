import os

import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel


MODEL_PATH = os.getenv("MODEL_PATH", "../../../models/model.pkl")

app = FastAPI(title="California Housing API")

model = joblib.load(MODEL_PATH)


class HouseFeatures(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float


@app.get("/")
def root():
    return {"status": "API is running"}


@app.post("/predict")
def predict(features: HouseFeatures):
    data = pd.DataFrame([features.model_dump()])
    prediction = model.predict(data)[0]

    return {
        "prediction": float(prediction),
        "prediction_usd": round(float(prediction) * 100000, 2),
    }
