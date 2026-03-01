# 📊 Telecom Customer Churn Prediction

Predict which telecom customers are about to leave — an end-to-end analytics pipeline from **SQL ETL → Python Machine Learning → FastAPI Inference API → Docker → Power BI dashboard** that transforms churn risk into actionable retention strategy.

---

## 🚀 Business Problem

In telecom, acquiring a new customer costs **5–10x more** than retaining one.

* Dataset: **7,043 customers**
* Churn rate: **26.54%**
* Objective: Identify high-risk customers early and support data-driven retention campaigns.

This project delivers a complete predictive system — from raw CSV ingestion to deployable ML inference and stakeholder-ready dashboards.

---

# 🏗️ End-to-End Architecture

```
CSV Data
   ↓
SQL Server ETL (Staging → Transform → Final Table → Views)
   ↓
Python EDA + Feature Engineering
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
└── README.md
```

---

# 🧱 Stage 1 — SQL Server ETL Pipeline

**Pipeline Flow:**

```
Raw CSV → Staging Table → Transformations → Final Table → Analytics Views
```

### Implemented in SQL Server (SSMS):

* Created staging & final schema tables
* Imported CSV via flat file import
* Applied:

  * Data type corrections
  * NULL handling
  * Data validation checks
* Built analytical views:

  * Churn by contract type
  * Revenue aggregation
  * Tenure analysis

**Output:** Clean, structured dataset passed into Python for modeling.

---

# 🔎 Stage 2 — Exploratory Data Analysis

### Dataset Summary

| Metric              | Value    |
| ------------------- | -------- |
| Customers           | 7,043    |
| Churn Rate          | 26.54%   |
| Class Imbalance     | Moderate |
| Optimization Metric | ROC-AUC  |

### Key Insights

* 📌 Month-to-Month contracts churn significantly more
* 📌 Churned customers have lower average tenure
* 📌 Electronic check users churn at highest rate
* 📌 Churned avg monthly charge: **$75**
* 📌 Retained avg monthly charge: **$63**
* 📌 Senior citizens (~16%) show distinct churn behavior

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
| Split            | 80/20 stratified split                |

---

## Models Trained

### 1️⃣ Logistic Regression (Baseline)

```python
LogisticRegression(max_iter=1000)
```

### 2️⃣ Random Forest

```python
RandomForestClassifier(
    n_estimators=300,
    random_state=42,
    class_weight='balanced'
)
```

### 3️⃣ Hyperparameter Tuning

```python
param_grid = {
    'C': [0.01, 0.1, 0.5, 1, 5, 10],
    'penalty': ['l2']
}
```

* 5-fold cross-validation
* Scoring metric: ROC-AUC

---

## 📈 Model Comparison

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

* `LogisticRegression.pkl`
* `RandomForestClassifier.pkl`
* `scaler.pkl`

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

```bash
uvicorn app:app --reload
```

Swagger UI:

```
http://localhost:8000/docs
```

---

# 🐳 Docker Containerization

The inference service is containerized for reproducible deployment.

### Build image

```bash
docker build -t churn-api ./customer-churn-api
```

### Run container

```bash
docker run -p 8000:8000 churn-api
```

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

### Dashboard Features

* Revenue by contract type
* Churn reason breakdown
* Gender distribution
* Revenue by age segment
* Geographic churn heatmap
* Interactive service filters

---

# 🛠️ Tech Stack

| Layer             | Tools               |
| ----------------- | ------------------- |
| ETL               | SQL Server, SSMS    |
| Data Wrangling    | Pandas, NumPy       |
| Visualization     | Matplotlib, Seaborn |
| ML                | Scikit-learn        |
| Model Persistence | Joblib              |
| API               | FastAPI             |
| Containerization  | Docker              |
| BI                | Power BI            |

---

# 📊 Final Results

| Metric                       | Value               |
| ---------------------------- | ------------------- |
| Final Model                  | Logistic Regression |
| ROC-AUC                      | 0.835               |
| Accuracy                     | 80%                 |
| Churn Recall (0.4 threshold) | 57%                 |
| Dataset Size                 | 7,043               |
| Churn Rate                   | 26.54%              |

---

# 💡 Business Recommendations

* Launch competitor-targeted retention campaigns (841 churn cases)
* Incentivize Month-to-Month customers to upgrade early
* Monitor high monthly charge new customers closely
* Offer premium support for 60+ age segment
* Use **0.4 threshold** for operational churn scoring

---

# 📦 Getting Started

```bash
git clone https://github.com/shreevarsha866/telecom-customer-churn-prediction.git
cd telecom-customer-churn-prediction
pip install -r requirements.txt
```

---

# 📄 License

MIT License

---

---

