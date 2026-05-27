from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import engine, Base, get_db
from app.model import load_model

Base.metadata.create_all(bind=engine)

model = load_model("model.joblib")

app = FastAPI(title="Zara Brand Predictor")

@app.post("/predict", response_model=schemas.PredictionResponse)
def predict(request: schemas.PredictionRequest, db: Session = Depends(get_db)):
    description = request.description
    price = request.price

    try:
        brand = model.predict([description])[0]
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction error: {str(e)}")

    db_request = crud.create_prediction(db, description, price, brand)
    return db_request
