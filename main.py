from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()

classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

@app.get("/")
def home():
    return {"message": "Sentiment API Running"}

@app.get("/predict")
def predict(text: str):
    result = classifier(text)
    return {"input": text, "result": result}
