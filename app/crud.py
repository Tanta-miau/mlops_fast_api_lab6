from sqlalchemy.orm import Session
from app.database import Prediction

def create_prediction(db: Session, description: str, price: float, brand: str):
    db_pred = Prediction(description=description, price=price, predicted_brand=brand)
    db.add(db_pred)
    db.commit()
    db.refresh(db_pred)
    return db_pred
