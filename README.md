# 📊 Telecom Customer Churn Prediction

Predict which telecom customers are about to leave — an end-to-end analytics pipeline from **SQL data structuring → Python Machine Learning → FastAPI Inference API → Docker → Power BI dashboard** that transforms churn risk into actionable retention strategy.

---

# 🚀 Business Problem

In telecom, acquiring a new customer costs **5–10× more** than retaining one.

* **Dataset:** 7,043 customers
* **Churn rate:** 26.54%
* **Objective:** Identify high-risk customers early and support data-driven retention campaigns

This project delivers a complete predictive system — from structured data preparation to deployable ML inference and executive dashboards.

---

# 📄 API Deployment Proof

The ML inference service was successfully:

* Containerized using Docker
* Executed locally with port mapping
* Validated via Swagger UI
* Tested using cURL
* Returned HTTP 200 responses
* Produced churn probability output

👉[Download Deployment Proof](https://github.com/shreevarsha866/Telecom_customer_churn_prediction/blob/main/Customer%20Churn%20Prediction%20-%20API%20%20Deployment%20Proof.pdf)

---

# 🏗️ End-to-End Architecture

```
Raw CSV Data
   ↓
SQL Server (Table Creation, Loading, Transformation, Views, Data Quality Checks)
   ↓
Python (Google Colab: Inspection, Cleaning, EDA, Feature Engineering)
   ↓
ML Model Training & Tuning
   ↓
Model Persistence (Joblib)
   ↓
FastAPI Inference Service
   ↓
Docker Containerization
   ↓
Power BI Business Dashboard
```

---

# 🗂️ Project Structure

```
telecom-customer-churn-prediction/
│
├── Dataset/
├── ETL_pipeline/
├── models/
│   ├── LogisticRegression.pkl
│   ├── RandomForestClassifier.pkl
│   └── scaler.pkl
│
├── notebook/
├── powerBI/
├── customer-churn-api/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── Customer_Churn_API_Deployment_Proof.pdf
└── README.md
```

---

# 🧱 Stage 1 — SQL Server Data Preparation

SQL Server was used for structured data preparation before modeling.

### Implemented in SQL (SSMS)

* Created staging and final schema tables
* Loaded raw CSV via flat file import
* Applied transformation logic
* Performed data quality checks

  * NULL validation
  * Data type corrections
* Built analytical views

  * Churn by contract type
  * Revenue aggregation
  * Tenure analysis

**Output:** Structured, analysis-ready dataset passed to Python for modeling.

---

# 🔎 Stage 2 — Python (Google Colab)

After SQL preparation, modeling work was completed in Python.

### Performed in Python:

* Data inspection and validation
* Additional cleaning
* Exploratory Data Analysis (EDA)
* Feature engineering
* Encoding & scaling
* Stratified 80/20 train-test split
---

# 🤖 Stage 3 — Machine Learning Pipeline

## Preprocessing

| Step             | Method                                |
| ---------------- | ------------------------------------- |
| Target Encoding  | Yes = 1, No = 0                       |
| Dropped          | customerID                            |
| TotalCharges Fix | Converted to numeric, 11 NaNs removed |
| Encoding         | pd.get_dummies(drop_first=True)       |
| Scaling          | StandardScaler                        |
| Split            | 80/20 stratified                      |

---

## Models Trained

### Logistic Regression (Baseline)

```python
LogisticRegression(max_iter=1000)
```

### Random Forest

```python
RandomForestClassifier(
    n_estimators=300,
    random_state=42,
    class_weight='balanced'
)
```

### Hyperparameter Tuning

```python
param_grid = {
    'C': [0.01, 0.1, 0.5, 1, 5, 10],
    'penalty': ['l2']
}
```

* 5-fold cross-validation
* Scoring metric: ROC-AUC

---

# 📈 Model Comparison

| Model                     | ROC-AUC   | Notes             |
| ------------------------- | --------- | ----------------- |
| Logistic Regression       | 0.835     | Strong baseline   |
| Random Forest             | 0.819     | Higher complexity |
| Tuned Logistic Regression | **0.835** | Final model       |

### 🎯 Final Model: Tuned Logistic Regression

Decision threshold adjusted to **0.4** to improve churn recall to **57%**.

---

# 💾 Model Persistence (Joblib)

Saved artifacts:

* LogisticRegression.pkl
* RandomForestClassifier.pkl
* scaler.pkl

### Load & Predict

```python
import joblib

model = joblib.load("LogisticRegression.pkl")
scaler = joblib.load("scaler.pkl")

X_scaled = scaler.transform(X_new)
churn_prob = model.predict_proba(X_scaled)[:, 1]
churn_flag = (churn_prob > 0.4).astype(int)
```

---

# 🚀 Stage 4 — FastAPI Inference Service

A production-ready API was built to serve real-time churn predictions.

### Run locally

```
uvicorn app:app --reload
```

Swagger UI:

```
http://localhost:8000/docs
```

---

# 🐳 Docker Containerization

### Build Image

```
docker build -t churn-api ./customer-churn-api
```

### Run Container

```
docker run -p 8000:8000 churn-api
```

Container execution and API validation documented in the Deployment Proof PDF.

---

# 📊 Stage 5 — Power BI Dashboard

File: `Report_BI.pbix`

### KPI Summary

| Metric          | Value       |
| --------------- | ----------- |
| Total Customers | 7,043       |
| Total Revenue   | $21.37M     |
| Churn Rate      | 26.54%      |
| Total Tenure    | 228K months |
| Avg Charges     | $2.28K      |

👉 **[Download powerbi Proof (PDF)](Report_BI.pdf)**
---

# 🛠️ Tech Stack

| Layer             | Tools            |
| ----------------- | ---------------- |
| Data Preparation  | SQL Server, SSMS |
| Data Processing   | Pandas, NumPy    |
| ML                | Scikit-learn     |
| API               | FastAPI          |
| Containerization  | Docker           |
| Model Persistence | Joblib           |
| BI                | Power BI         |

---

# 📊 Final Results

| Metric                 | Value  |
| ---------------------- | ------ |
| ROC-AUC                | 0.835  |
| Accuracy               | 80%    |
| Recall (0.4 threshold) | 57%    |
| Dataset Size           | 7,043  |
| Churn Rate             | 26.54% |

---

# 💡 Business Recommendations

* Launch competitor-targeted retention campaigns
* Incentivize Month-to-Month upgrades
* Monitor high monthly charge new customers
* Prioritize high-revenue senior segment
* Deploy scoring with threshold = 0.4

---

# 📦 Getting Started

```
git clone https://github.com/shreevarsha866/telecom-customer-churn-prediction.git
cd telecom-customer-churn-prediction
pip install -r requirements.txt
```

---

# 📄 License

MIT License

---
