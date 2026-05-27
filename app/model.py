import joblib

def load_model(path: str):
    return joblib.load(path)
