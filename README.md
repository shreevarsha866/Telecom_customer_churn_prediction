# 📊 Telecom Customer Churn Prediction & Deployment

> **Full-Stack Data Science Project — SQL ETL · Python ML · FastAPI · Docker · Power BI**

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-Deployed-009688?logo=fastapi)](https://fastapi.tiangolo.com)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)](https://docker.com)
[![SQL Server](https://img.shields.io/badge/SQL%20Server-ETL-CC2927?logo=microsoftsqlserver)](https://www.microsoft.com/sql-server)
[![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?logo=powerbi)](https://powerbi.microsoft.com)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange?logo=scikit-learn)](https://scikit-learn.org)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1R5-NtS4bo7IaDbCzM8FjcYEjJBhnmoZU?usp=sharing)

---

## 📌 Project Overview

This is a **full-stack data science project** that predicts telecom customer churn using a complete production-grade pipeline:

- 🗄️ **SQL Server ETL** — raw CSV → staging → transformation → final table → analytics views
- 🐍 **Python ML** — data cleaning, EDA, feature engineering, model training & evaluation
- 🚀 **FastAPI Deployment** — real-time inference REST API with `/predict` endpoint
- 🐳 **Docker Containerization** — reproducible, portable deployment
- 📊 **Power BI Dashboard** — interactive business intelligence for non-technical stakeholders

The final **Logistic Regression model** achieved **ROC-AUC 0.835** with **57% churn recall** — optimized for real business retention objectives, not just accuracy.

---

## 🎯 Business Problem

Telecom companies lose significant revenue when customers churn. With **7,043 customers** and **$21.37M revenue at stake**, identifying at-risk customers early enables:

- 📞 **Proactive retention campaigns** before customers leave
- 💰 **Revenue protection** by targeting high-value churners
- 🎯 **CRM integration** — flag customers with churn probability > 0.4 for immediate action
- 📊 **Contract strategy** — month-to-month customers churn most; push annual contracts

---

## 📊 Key Results

| Metric | Value |
|---|---|
| **Dataset** | 7,043 telecom customers |
| **Churn Rate** | 26.6% |
| **Final Model** | Logistic Regression (tuned) |
| **Accuracy** | 80% |
| **ROC-AUC** | **0.835** |
| **Churn Recall** | **57%** (after threshold tuning at 0.4) |
| **Decision Threshold** | 0.4 (business-optimized) |
| **API Status** | ✅ Deployed & tested |

---

## 🏗️ Full Project Architecture

```
Raw CSV (WA_Fn-UseC_-Telco-Customer-Churn.csv)
     │
     ▼
┌─────────────────────────────────────┐
│         STAGE 1 — SQL ETL           │
│  SQL Server (SSMS)                  │
│  01. Create staging & final tables  │
│  02. Load CSV via Flat File Import  │
│  03. Transform & cleanse data       │
│  04. Create analytics views         │
│  05. Data quality checks            │
└─────────────────────────────────────┘
     │
     ▼
┌─────────────────────────────────────┐
│       STAGE 2 — Python ML           │
│  Google Colab                       │
│  01. Data inspection & cleaning     │
│  02. EDA & visualizations           │
│  03. Feature engineering            │
│  04. Model training (LR + RF)       │
│  05. ROC-AUC evaluation             │
│  06. Hyperparameter tuning          │
│  07. Threshold optimization (0.4)   │
│  08. Model saved via Joblib         │
└─────────────────────────────────────┘
     │
     ▼
┌─────────────────────────────────────┐
│    STAGE 3 — FastAPI + Docker       │
│  app.py (FastAPI inference service) │
│  POST /predict → churn probability  │
│  Dockerfile → containerized image  │
│  docker run -p 8000:8000 churn-api  │
│  ✅ Tested via Swagger UI + cURL    │
└─────────────────────────────────────┘
     │
     ▼
┌─────────────────────────────────────┐
│      STAGE 4 — Power BI             │
│  Interactive churn dashboard        │
│  KPI cards, geographic map,         │
│  contract & payment breakdowns      │
└─────────────────────────────────────┘
```

---

## 🗄️ Stage 1 — SQL ETL Pipeline (SQL Server / SSMS)

> SQL handles all data infrastructure — table creation, loading, transformation, and quality validation

### 01. Create Tables
```sql
-- Staging table (raw import)
CREATE TABLE dbo.customer_churn_ETL (
    gender NVARCHAR(50), age INT, city NVARCHAR(50),
    contract NVARCHAR(50), payment_method NVARCHAR(50),
    tenure_in_months INT, monthly_charge DECIMAL(18,10),
    total_charges DECIMAL(18,10), total_revenue DECIMAL(18,10),
    churn_category NVARCHAR(50), churn_reason NVARCHAR(50),
    customer_status NVARCHAR(50)
    -- + 20 more feature columns
);

-- Final curated table (with primary key)
CREATE TABLE dbo.customer_churn_final (
    customer_id INT IDENTITY(1,1) PRIMARY KEY,
    gender NVARCHAR(50), age INT, city NVARCHAR(50),
    contract NVARCHAR(50), payment_method NVARCHAR(50),
    tenure_in_months INT, monthly_charge DECIMAL(18,10),
    total_revenue DECIMAL(18,10),
    churn_category NVARCHAR(50), churn_reason NVARCHAR(50)
);
```

### 02. Load Data
```sql
-- Data loaded via SSMS Import Flat File Wizard
-- Source: customer_churn_ETL.csv → Target: dbo.customer_churn_ETL
SELECT COUNT(*) AS staging_rows FROM dbo.customer_churn_ETL;
```

### 03. Transformation
```sql
-- Filter & load valid records to final table
INSERT INTO dbo.customer_churn_final (...)
SELECT gender, age, city, contract, payment_method,
       tenure_in_months, monthly_charge, total_charges,
       total_revenue, churn_category, churn_reason
FROM dbo.customer_churn_ETL
WHERE customer_status IS NOT NULL;
```

### 04. Analytics View
```sql
-- Churn rate by contract type
CREATE VIEW vw_churn_metrics AS
SELECT
    contract,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN churn_category IS NOT NULL THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(100.0 * SUM(CASE WHEN churn_category IS NOT NULL THEN 1 ELSE 0 END) / COUNT(*), 2)
        AS churn_rate_percent
FROM dbo.customer_churn_final
GROUP BY contract;
```

### 05. Data Quality Checks
```sql
SELECT COUNT(*) AS staging_rows FROM dbo.customer_churn_ETL;
SELECT COUNT(*) AS final_rows   FROM dbo.customer_churn_final;
SELECT COUNT(*) AS null_contracts FROM dbo.customer_churn_final WHERE contract IS NULL;
SELECT MIN(total_revenue) AS min_revenue, MAX(total_revenue) AS max_revenue
FROM dbo.customer_churn_final;
```

---

## 🐍 Stage 2 — Python ML Pipeline (Google Colab)

### Dataset
- **Source:** `WA_Fn-UseC_-Telco-Customer-Churn.csv`
- **Records:** 7,043 customers
- **Target:** `Churn` (Yes/No → 1/0)
- **Class imbalance:** ~73.5% No / 26.5% Yes

### Data Cleaning
```python
# Fix TotalCharges (stored as string)
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df = df.dropna()  # remove 11 rows with null TotalCharges
```

### EDA Highlights
- 📋 **Month-to-month** contract customers churn the most
- 💳 **Electronic check** payment method has highest churn rate
- ⏱️ **Low-tenure customers** churn most — highest risk in first 12 months
- 💰 Churned customers pay **~$12/month more** than retained customers on average

### Feature Engineering
```python
# Drop customerID, encode categoricals
X = df.drop(['Churn', 'customerID'], axis=1)
y = df['Churn'].map({'Yes': 1, 'No': 0})

X = pd.get_dummies(X, categorical_cols, drop_first=True)

# Scale + stratified split
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)
```

### Model Training & Selection
```python
# Logistic Regression
log_model = LogisticRegression(max_iter=1000)

# Random Forest
rf_model = RandomForestClassifier(n_estimators=300, class_weight='balanced', random_state=42)
```

| Model | Accuracy | ROC-AUC |
|---|---|---|
| Logistic Regression | 80% | **0.835** ✅ |
| Random Forest | ~79% | 0.819 |

> ✅ **Logistic Regression selected** — higher AUC + interpretability for business use

### Hyperparameter Tuning + Threshold Optimization
```python
# GridSearchCV on C parameter
param_grid = {'C': [0.01, 0.1, 0.5, 1, 5, 10], 'penalty': ['l2']}
grid = GridSearchCV(LogisticRegression(max_iter=1000), param_grid, cv=5, scoring='roc_auc')

# Custom threshold = 0.4 (prioritize churn recall over precision)
y_pred_threshold = (y_prob_best > 0.4).astype(int)
# Churn Recall improved to 57%
```

### Model Saving
```python
import joblib
joblib.dump(log_model, "LogisticRegression.pkl")
joblib.dump(scaler, "scaler.pkl")
```

---

## 🚀 Stage 3 — FastAPI + Docker Deployment

### API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | API status |
| `GET` | `/health` | Health check |
| `POST` | `/predict` | Churn prediction |

### POST /predict
```json
// Request
{
  "features": [1.0, 0.45, 2.0, 120, 1.0, 3.0, 80, 1.0, 2.5, 10, 3.4, 1.0, 0.0, 1.2, 3.5, 4.5, 6.7, 8.9]
}

// Response
{
  "prediction": 0,
  "churn_probability": 0.0072
}
```

### app.py (FastAPI Inference Service)
```python
from fastapi import FastAPI
from pydantic import BaseModel, conlist
import joblib, numpy as np

model  = joblib.load("LogisticRegression.pkl")
scaler = joblib.load("scaler.pkl")

app = FastAPI(title="Customer Churn Prediction API", version="1.0.0")

class PredictionRequest(BaseModel):
    features: conlist(float, min_length=30, max_length=30)

@app.post("/predict")
def predict(request: PredictionRequest):
    input_data  = np.array(request.features).reshape(1, -1)
    scaled_data = scaler.transform(input_data)
    prediction  = model.predict(scaled_data)[0]
    probability = model.predict_proba(scaled_data)[0][1]
    return {"prediction": int(prediction), "churn_probability": float(probability)}
```

### Dockerfile
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Build & Run
```bash
# Build Docker image
docker build -t churn-api .

# Run container
docker run -p 8000:8000 churn-api

# Test via cURL
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"features": [1.0, 0.45, 2.0, 120, ...]}'
```

### ✅ Deployment Proof
- **Swagger UI** tested at `http://localhost:8000/docs`
- **POST /predict** → `prediction: 0`, `churn_probability: 0.0072`, HTTP `200 OK`
- **cURL verification** → confirmed working outside Swagger
- **Docker Desktop** → `churn-api` image running, port `8000:8000`, image size `566 MB`

---

## 📊 Stage 4 — Power BI Dashboard

Interactive dashboard built to visualize:
- 📈 Overall churn rate KPI card
- 🗺️ Geographic churn map across cities
- 📋 Churn by contract type (month-to-month vs annual)
- 💳 Churn by payment method
- 💰 Revenue at risk segmentation
- 🔍 7 interactive filters for self-serve analysis

> Dashboard file: `Telecom_customer_churn.pbit`

---

## 💡 Key Business Insights

- 📋 **Month-to-month** customers have the **highest churn rate** — push annual contracts
- 💳 **Electronic check** payers churn most — incentivize auto-pay migration
- ⏱️ **First 12 months** = highest churn risk window — intervene early
- 💰 Churned customers pay **more per month** — high-value customers are leaving
- 🎯 **Decision threshold 0.4** → flags more at-risk customers for proactive retention
- 🔌 API ready for **CRM system integration** — real-time churn scoring at scale

---

## 🛠️ Tech Stack

| Layer | Tool | Purpose |
|---|---|---|
| **ETL** | SQL Server (SSMS) | Table creation, data loading, transformation, views |
| **ML** | Python · Scikit-learn · Pandas | Data cleaning, EDA, modeling |
| **API** | FastAPI · Uvicorn · Pydantic | REST inference service |
| **Deployment** | Docker | Containerization & reproducibility |
| **Model Saving** | Joblib | Model & scaler persistence |
| **Dashboard** | Power BI | Business intelligence |
| **Dev Env** | Google Colab | ML development |

---

## 🚀 How to Run

**Option 1 — Google Colab (ML Notebook)**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1R5-NtS4bo7IaDbCzM8FjcYEjJBhnmoZU?usp=sharing)

**Option 2 — Run API with Docker**
```bash
git clone https://github.com/shreevarsha866/Telecom_customer_churn_prediction
cd Telecom_customer_churn_prediction

docker build -t churn-api .
docker run -p 8000:8000 churn-api

# Open Swagger UI
# http://localhost:8000/docs
```

**Option 3 — Run API Locally**
```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

---

## 📁 Repository Structure

```
📦 Telecom_customer_churn_prediction
 ┣ 📓 Telcom_Customer_churn.ipynb          ← ML notebook (Colab)
 ┣ 🐍 app.py                               ← FastAPI inference service
 ┣ 🐳 Dockerfile                           ← Docker container config
 ┣ 📄 requirements.txt                     ← Python dependencies
 ┣ 🗄️ sql/
 ┃   ┣ 01_create_tables.sql                ← Staging & final table DDL
 ┃   ┣ 02_load_data.sql                    ← CSV load instructions
 ┃   ┣ 03_transformations.sql              ← Data cleanse & insert
 ┃   ┣ 04_views.sql                        ← vw_churn_metrics view
 ┃   ┗ 05_data_quality_checks.sql          ← Row counts, null checks
 ┣ 📊 Telecom_customer_churn.pbit          ← Power BI dashboard
 ┣ 📄 WA_Fn-UseC_-Telco-Customer-Churn.csv ← Dataset
 ┣ 🤖 LogisticRegression.pkl              ← Saved model
 ┣ ⚙️ scaler.pkl                           ← Saved StandardScaler
 ┣ 📄 churn_prediction_data.csv            ← Cleaned export
 ┗ 📖 README.md
```

---

## 💡 Conclusion

- A **full-stack DS pipeline** from raw SQL ETL to deployed FastAPI microservice
- **Logistic Regression outperformed Random Forest** on ROC-AUC (0.835 vs 0.819) — showing model selection over complexity
- **Threshold tuning at 0.4** improved churn recall to 57% — aligned with business goal of catching at-risk customers
- **Docker deployment** ensures reproducibility across any environment
- **Power BI dashboard** bridges the gap between ML model and business stakeholders

---

## 🔮 Future Work

- Push Docker image to **Docker Hub** for cloud deployment
- Deploy on **AWS EC2 or Azure App Service** for public access
- Add **real-time streaming** from CRM systems using Kafka
- Build **Streamlit frontend** for non-technical user access
- Extend to **multi-class churn reason prediction** (price, competitor, service)

---

## 👩‍💻 Author

**Shreevarsha S**
Data Science Professional | ML & NLP Enthusiast

[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-7b6ef6?logo=globe)](https://shreevarsha866.github.io/Shreevarsha_Portfolio)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/s-shreevarsha-503887218/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?logo=github)](https://github.com/shreevarsha866)
[![Email](https://img.shields.io/badge/Email-Contact-red?logo=gmail)](mailto:varshashree866@gmail.com)

---

*⭐ If you found this project helpful, please give it a star!*
