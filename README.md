# Sentiment Analysis API (FastAPI + DistilBERT)

## 📌 Project Goal
Build a REST API that analyzes input text and classifies it as Positive or Negative using a pre-trained transformer model.

---

# 🧠 How This Project Works

1. User sends text to API
2. FastAPI receives request
3. Text is tokenized
4. Transformer model processes input
5. Model returns sentiment + confidence score
6. API responds with JSON

---

# ⚙️ Step-by-Step Setup Guide (Ubuntu)

## 1️⃣ Clone the Repository

git clone https://github.com/singampalliveerendra/sentiment-analysis-api.git
cd sentiment-analysis-api

---

## 2️⃣ Create Virtual Environment

python3 -m venv venv
source venv/bin/activate

You should see (venv) in terminal.

---

## 3️⃣ Install Dependencies

pip install -r requirements.txt

This installs:
- FastAPI
- Uvicorn
- Transformers
- Torch (CPU)

---

## 4️⃣ Run the Server

uvicorn main:app

After startup, you should see:

Uvicorn running on http://127.0.0.1:8000

---

## 5️⃣ Test the API

Open in browser:

http://127.0.0.1:8000/docs

Click `/predict`
Click "Try it out"

Example:

I am very happy today

---

# 📂 Project Structure

sentiment-analysis-api/
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md

---

# 🔥 API Endpoints

GET /
Health check endpoint.

GET /predict?text=your_text
Returns sentiment classification.

---

# 🚀 Future Improvements

- Convert GET to POST
- Add database logging
- Dockerize application
- Deploy on cloud
