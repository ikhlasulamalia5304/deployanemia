import pickle
import pandas as pd
from app.config import MODEL_PATH, FEATURES
from app.utils import map_result

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

def predict_blood(data):

    # Mapping API -> nama fitur training
    mapped = {
        "Gender": data.gender,
        "Hemoglobin": data.hemoglobin,
        "MCH": data.mch,
        "MCHC": data.mchc,
        "MCV": data.mcv,
        "Hb_MCV_ratio": data.hb_mcv_ratio
    }

    # Convert ke DataFrame dengan kolom EXACT seperti training
    df = pd.DataFrame([mapped], columns=FEATURES)

    raw_pred = model.predict(df)[0]

    return {
        "prediction_raw": int(raw_pred),
        "prediction": map_result(raw_pred)
    }
