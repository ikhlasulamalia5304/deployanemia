from fastapi import FastAPI
from app.schemas import BloodInput
from fastapi.middleware.cors import CORSMiddleware
from app.predictors import predict_blood

app = FastAPI(
    title="Blood Prediction API",
    description="Prediksi kondisi menggunakan model XGBoost Pipeline",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Untuk development, allow semua origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Blood Prediction API is running"}

@app.post("/predict")
def predict(data: BloodInput):
    return predict_blood(data)
