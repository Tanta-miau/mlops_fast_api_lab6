import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib
import os

# загрузка
data_path = "zara_us_sample_data.json"
if not os.path.exists(data_path):
    raise FileNotFoundError(f"Файл {data_path} не найден. Поместите его в папку проекта.")

with open(data_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame(data)

#  бренды
df = df[df['brand'].isin(['ZARA', 'ZARAHOME'])]

# признаки и целевая переменная
X = df['description']
y = df['brand']

# train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Пайплайн: TF-IDF + логистическая регрессия
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english', max_features=5000)),
    ('clf', LogisticRegression(max_iter=1000, random_state=42))
])

# обучение
pipeline.fit(X_train, y_train)

# качество
y_pred = pipeline.predict(X_test)
print(classification_report(y_test, y_pred))

# сохранение
joblib.dump(pipeline, 'model.joblib')
print("Модель сохранена в model.joblib")