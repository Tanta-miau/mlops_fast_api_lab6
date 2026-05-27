import pytest
import joblib
import os

MODEL_PATH = "model.joblib"

@pytest.fixture(scope="module")
def model():
    assert os.path.exists(MODEL_PATH), "Модель не найдена, сначала запустите train.py"
    return joblib.load(MODEL_PATH)

test_data = [
    ("Bodysuit with sweetheart neckline and adjustable spaghetti straps.", "ZARA"),
    ("Forged stainless steel kitchen scissors.", "ZARAHOME"),
    ("Swimsuit made of lightweight technical fabric.", "ZARA"),
]

@pytest.mark.parametrize("description,expected_brand", test_data)
def test_model_predictions(model, description, expected_brand):
    pred = model.predict([description])[0]
    assert pred == expected_brand, f"Expected {expected_brand}, got {pred} for '{description}'"
