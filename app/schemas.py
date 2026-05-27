from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PredictionRequest(BaseModel):
    description: str
    price: Optional[float] = None

class PredictionResponse(BaseModel):
    id: int
    description: str
    price: Optional[float]
    predicted_brand: str
    timestamp: datetime

    class Config:
        from_attributes = True
