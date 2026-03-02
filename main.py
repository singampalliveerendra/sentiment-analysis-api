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
    cleaned_text = text.strip()  # remove extra spaces
    print("Processing text:", cleaned_text)  # debug log
    
    result = classifier(cleaned_text)
    
    return {
        "input": cleaned_text,
        "sentiment": result[0]["label"],
        "confidence": result[0]["score"]
    }
