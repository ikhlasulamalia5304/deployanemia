from pydantic import BaseModel, Field

class BloodInput(BaseModel):
    gender: float
    hemoglobin: float
    mch: float
    mchc: float
    mcv: float
    hb_mcv_ratio: float