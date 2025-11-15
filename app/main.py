from fastapi import FastAPI
from app.schemas import BloodInput
from app.predictors import predict_blood

app = FastAPI(
    title="Blood Prediction API",
    description="Prediksi kondisi menggunakan model XGBoost Pipeline",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Blood Prediction API is running"}

@app.post("/predict")
def predict(data: BloodInput):
    return predict_blood(data)
