

# 📈 Stock Explain — AI-Powered Stock Movement Explainer

Stock Explain is a full-stack web application that explains **why a stock’s price moved** in simple, human-readable language.
The focus is on **explainability**, not prediction or investment advice.

Instead of showing raw numbers alone, the app converts live market data into **short AI-generated explanations** that are easy for beginners to understand.

---

## 🚀 Key Features

* 📊 Fetches live stock data (NSE stocks)
* 🔍 Compares **today’s price with yesterday’s opening price**
* 🧠 Uses a **locally hosted LLaMA 3 (8B)** model for explanations
* ✍️ Generates **exactly 3 concise sentences**
* ⏳ Loader for smooth user experience during AI processing
* ⚠️ Ethical design — no predictions, no financial advice
* 🛡️ Defensive handling for missing or delayed data

---

## 🧠 How It Works (High-Level)

1. User enters a stock symbol (e.g., `INFY.NS`)
2. Backend fetches market data
3. Price fluctuation is calculated using:

   * Yesterday’s opening price
   * Latest available price
4. The processed data is sent to a local AI model
5. AI generates a short, uncertainty-aware explanation
6. Result is displayed on the frontend

---

## 🛠️ Tech Stack

### Backend

* **Python**
* **FastAPI**
* Yahoo Finance (market data)
* Ollama (local AI runtime)
* LLaMA 3 (8B) model

### Frontend

* HTML
* CSS
* JavaScript

### AI

* Local LLM inference (no cloud dependency)
* Prompt-controlled output (concise & ethical)

---

## 🖥️ Project Structure

```
stock-explain/
├── backend/
│   ├── main.py
│   ├── services/
│   │   └── stock_service.py
│   ├── utils/
│   │   └── ai_explanation_engine.py
│   ├── .gitignore
│   └── venv/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
```

---

## ▶️ How to Run the Project

### 1️⃣ Start the Backend

```bash
cd backend
venv\Scripts\activate
uvicorn main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

---

### 2️⃣ Start Ollama (AI Engine)

```bash
ollama serve
```

Ensure the model is available:

```bash
ollama pull llama3:8b
```

---

### 3️⃣ Open the Frontend

* Open `frontend/index.html` in a browser
* Enter a stock symbol like:

  ```
  INFY.NS
  TCS.NS
  TATAMOTORS.NS
  ```

---

## 📌 Example Output

> “The stock is trading slightly higher compared to where it opened yesterday. Trading activity suggests steady market participation during the session. Other broader market or external factors may also be influencing this movement.”

---

## ⚠️ Disclaimer

* This project is for **educational purposes only**
* It does **not provide investment advice**
* Market data may be delayed or incomplete
* AI explanations are **observational**, not definitive

---

## 🔮 Future Scope & Enhancements

This project is designed to be **easily extendable**. Possible future improvements include:

### 📊 Data Enhancements

* Multiple comparison baselines (previous close, weekly average)
* Market index comparison (NIFTY vs stock)
* Sector-wise insights

### 🧠 AI Enhancements

* Sentiment labels (Bullish / Neutral / Bearish)
* Confidence score for explanations
* Multi-language explanations
* User-controlled explanation length

### 🌐 Product / SaaS

* Authentication & user accounts
* Saved watchlists
* Hosted AI inference
* Subscription-based SaaS model
* Mobile-friendly UI

---

## 🏁 Conclusion

Stock Explain demonstrates how **AI + clean data logic + good UX** can turn raw financial data into meaningful insights.
The project emphasizes **clarity, responsibility, and real-world engineering practices**, making it suitable for academic evaluation, portfolio use, and MVP-level product demos.


