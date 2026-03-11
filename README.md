# 📊 Telecom Customer Churn Prediction & Deployment

> **Full-Stack Data Science Project — SQL ETL · Python ML · PySpark · FastAPI · Docker · Power BI**

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://python.org)
[![PySpark](https://img.shields.io/badge/PySpark-Apache%20Spark-E25A1C?logo=apachespark)](https://spark.apache.org)
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
- ⚡ **PySpark (Apache Spark)** — distributed preprocessing and Spark MLlib model training for big data scalability
- 🚀 **FastAPI Deployment** — real-time inference REST API with `/predict` endpoint
- 🐳 **Docker Containerization** — reproducible, portable deployment
- 📊 **Power BI Dashboard** — interactive business intelligence for non-technical stakeholders

The sklearn **Logistic Regression model** achieved **ROC-AUC 0.835**, while the **Spark MLlib Random Forest** pipeline achieved **ROC-AUC 0.849** — demonstrating the value of distributed ML for production scale.

---

## 🎯 Business Problem

Telecom companies lose significant revenue when customers churn. With **7,043 customers** and **$21.37M revenue at stake**, identifying at-risk customers early enables:

- 📞 **Proactive retention campaigns** before customers leave
- 💰 **Revenue protection** by targeting high-value churners
- 🎯 **CRM integration** — flag customers with churn probability > 0.4 for immediate action
- 📊 **Contract strategy** — month-to-month customers churn most; push annual contracts

---

## 📊 Key Results

### Model Comparison — All Models

| Metric | Logistic Regression | Random Forest | XGBoost | PySpark RF (MLlib) |
|---|---|---|---|---|
| **Accuracy** | 79.7% | 78.3% | 78.1% | — |
| **ROC-AUC** | 0.836 | 0.819 | 0.823 | **0.849** ✅ best |
| **Precision (No Churn)** | 0.84 | 0.83 | — | — |
| **Recall (No Churn)** | 0.89 | 0.89 | — | — |
| **F1 (No Churn)** | 0.87 | 0.86 | — | — |
| **Precision (Churn)** | 0.64 | 0.62 | — | — |
| **Recall (Churn)** | 0.53 | 0.48 | — | — |
| **F1 (Churn)** | 0.58 | 0.54 | — | — |
| **Scale** | Single machine | Single machine | Single machine | Distributed cluster |

### After Hyperparameter Tuning — Logistic Regression (Best: C=5, penalty=l2)

| Metric | Before Tuning | After Tuning | After Threshold=0.4 |
|---|---|---|---|
| **Accuracy** | 79.7% | 80% | 80% |
| **ROC-AUC** | 0.836 | 0.836 | — |
| **Precision (Churn)** | 0.64 | 0.65 | 0.65 |
| **Recall (Churn)** | 0.53 | 0.53 | 0.53 |
| **F1 (Churn)** | 0.58 | 0.58 | 0.58 |

> ✅ **Logistic Regression selected** as final model — highest ROC-AUC (sklearn) + interpretability

### SHAP Explainability — Top Churn Drivers (XGBoost)

| Rank | Feature | Importance |
|---|---|---|
| 1 | TotalCharges | 0.1641 |
| 2 | tenure | 0.1538 |
| 3 | MonthlyCharges | 0.1413 |
| 4 | Contract_Two year | 0.0546 |
| 5 | InternetService_Fiber optic | 0.0398 |
| 6 | PaymentMethod_Electronic check | 0.0386 |
| 7 | Contract_One year | 0.0275 |
| 8 | OnlineSecurity_Yes | 0.0263 |

> **Key Insight:** Tenure and charges dominate churn prediction — long-tenure, high-paying customers are most at risk when locked into month-to-month contracts.

### PySpark MLlib — Feature Importance (Distributed RF)

| Rank | Feature | Importance |
|---|---|---|
| 1 | tenure_charge_ratio | 0.1795 |
| 2 | Contract | 0.1253 |
| 3 | contract_length | 0.1166 |
| 4 | tenure | 0.1033 |
| 5 | MonthlyCharges | 0.0531 |
| 6 | premium_internet | 0.0651 |
| 7 | tenure_group | 0.0645 |
| 8 | TotalCharges | 0.0402 |

### PySpark MLlib — Prediction Distribution (Test Set: 1,342 rows)

| Actual | Predicted | Count |
|---|---|---|
| No Churn (0) | No Churn (0) | 907 |
| No Churn (0) | Churn (1) | 81 |
| Churn (1) | No Churn (0) | 185 |
| Churn (1) | Churn (1) | 169 |

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
│  04. Model training (LR + RF + XGB) │
│  05. ROC-AUC evaluation             │
│  06. Hyperparameter tuning          │
│  07. Threshold optimization (0.4)   │
│  08. SHAP explainability            │
│  09. Model saved via Joblib         │
└─────────────────────────────────────┘
     │
     ▼
┌─────────────────────────────────────┐
│     STAGE 3 — PySpark MLlib         │
│  Apache Spark (Google Colab)        │
│  01. Spark Session initialization   │
│  02. Distributed data loading       │
│  03. Feature engineering (withCol)  │
│  04. StringIndexer + OneHotEncoder  │
│  05. VectorAssembler + Scaler       │
│  06. Random Forest (Spark MLlib)    │
│  07. CrossValidator (distributed)   │
│  08. ROC-AUC: 0.849                 │
└─────────────────────────────────────┘
     │
     ▼
┌─────────────────────────────────────┐
│    STAGE 4 — FastAPI + Docker       │
│  app.py (FastAPI inference service) │
│  POST /predict → churn probability  │
│  Dockerfile → containerized image  │
│  docker run -p 8000:8000 churn-api  │
│  ✅ Tested via Swagger UI + cURL    │
└─────────────────────────────────────┘
     │
     ▼
┌─────────────────────────────────────┐
│      STAGE 5 — Power BI             │
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
SELECT COUNT(*) AS staging_rows FROM dbo.customer_churn_ETL;
```

### 03. Transformation
```sql
INSERT INTO dbo.customer_churn_final (...)
SELECT gender, age, city, contract, payment_method,
       tenure_in_months, monthly_charge, total_charges,
       total_revenue, churn_category, churn_reason
FROM dbo.customer_churn_ETL
WHERE customer_status IS NOT NULL;
```

### 04. Analytics View
```sql
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
SELECT COUNT(*) AS staging_rows  FROM dbo.customer_churn_ETL;
SELECT COUNT(*) AS final_rows    FROM dbo.customer_churn_final;
SELECT COUNT(*) AS null_contracts FROM dbo.customer_churn_final WHERE contract IS NULL;
SELECT MIN(total_revenue), MAX(total_revenue) FROM dbo.customer_churn_final;
```

---

## 🐍 Stage 2 — Python ML Pipeline (Google Colab)

### EDA Highlights
- 📋 **Month-to-month** contract customers churn the most
- 💳 **Electronic check** payment method has highest churn rate
- ⏱️ **Low-tenure customers** churn most — highest risk in first 12 months
- 💰 Churned customers pay **~$12/month more** than retained customers

### Feature Engineering (15+ features)
```python
df['tenure_group']         = pd.cut(df['tenure'], bins=[0,12,24,48,60,100], labels=[1,2,3,4,5])
df['avg_spend']            = df['TotalCharges'] / (df['tenure'] + 1)
df['high_value_customer']  = (df['MonthlyCharges'] > df['MonthlyCharges'].median()).astype(int)
df['long_term_customer']   = (df['tenure'] > 24).astype(int)
df['tenure_charge_ratio']  = df['tenure'] / (df['MonthlyCharges'] + 1)
df['contract_length']      = df['Contract'].map({'Month-to-month':1,'One year':2,'Two year':3})
df['premium_internet']     = (df['InternetService'] == 'Fiber optic').astype(int)
df['num_services']         = df[services].apply(lambda x: (x=='Yes').sum(), axis=1)
```

### Model Comparison
| Model | Accuracy | ROC-AUC |
|---|---|---|
| Logistic Regression | 80% | **0.835** ✅ selected |
| Random Forest | ~79% | 0.819 |
| XGBoost | — | — |

### SHAP Explainability
```python
import shap
explainer   = shap.TreeExplainer(xgb_model)
shap_values = explainer.shap_values(X_test)
shap.summary_plot(shap_values, X_test)
```
Top churn drivers identified: **contract type**, **tenure**, **monthly charges**

### Threshold Optimization
```python
# Lower threshold → catch more churners (business priority)
y_pred_threshold = (y_prob_best > 0.4).astype(int)
# Churn Recall improved to 57%
```

---

## ⚡ Stage 3 — PySpark Distributed Pipeline (Apache Spark)

> Same churn prediction logic scaled to Apache Spark — production-ready for millions of records

### Why PySpark?
The Python/sklearn pipeline runs on a single machine. PySpark distributes the same logic across a cluster, making it suitable for real-world telecom data at Swiggy-like scale.

### Spark Session
```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("TelecomChurnAnalysis") \
    .config("spark.driver.memory", "2g") \
    .getOrCreate()
```

### Distributed Feature Engineering
```python
from pyspark.sql.functions import when, col

spark_df = spark_df \
    .withColumn('tenure_group',
        when(col('tenure') <= 12, 1).when(col('tenure') <= 24, 2).otherwise(3)) \
    .withColumn('avg_spend', col('TotalCharges') / (col('tenure') + 1)) \
    .withColumn('contract_length',
        when(col('Contract') == 'Month-to-month', 1)
        .when(col('Contract') == 'One year', 2).otherwise(3)) \
    .withColumn('premium_internet',
        when(col('InternetService') == 'Fiber optic', 1).otherwise(0))
```

### Spark MLlib Pipeline
```python
from pyspark.ml.feature import StringIndexer, OneHotEncoder, VectorAssembler, StandardScaler
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.tuning import CrossValidator, ParamGridBuilder
from pyspark.ml import Pipeline

# Encode → Assemble → Scale → Train
pipeline = Pipeline(stages=indexers + encoders + [assembler, scaler, rf])

# Distributed cross-validation
cv = CrossValidator(estimator=pipeline, estimatorParamMaps=param_grid,
                    evaluator=evaluator, numFolds=3)
cv_model = cv.fit(train_spark)
```

### Results
```
Spark ML ROC-AUC       : 0.8492  ← distributed pipeline
Sklearn LR ROC-AUC     : 0.835   ← single machine baseline
Sklearn RF ROC-AUC     : 0.819   ← single machine baseline
```

| Step | Pandas/Sklearn | PySpark/MLlib |
|---|---|---|
| Data loading | `pd.read_csv()` | `spark.read.csv()` |
| Feature engineering | `df['col'] = ...` | `df.withColumn(...)` |
| Encoding | `pd.get_dummies()` | `StringIndexer + OneHotEncoder` |
| Scaling | `StandardScaler` | `StandardScaler (MLlib)` |
| Model | `RandomForestClassifier` | `RandomForestClassifier (MLlib)` |
| Cross-validation | `GridSearchCV` | `CrossValidator` |
| Runs on | Single machine | **Distributed cluster** |

---

## 🚀 Stage 4 — FastAPI + Docker Deployment

### API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | API status |
| `GET` | `/health` | Health check |
| `POST` | `/predict` | Churn prediction |

### POST /predict
```json
// Request
{ "features": [1.0, 0.45, 2.0, 120, 1.0, 3.0, 80, 1.0, 2.5, 10, 3.4, 1.0, 0.0, 1.2, 3.5, 4.5, 6.7, 8.9] }

// Response
{ "prediction": 0, "churn_probability": 0.0072 }
```

### app.py
```python
from fastapi import FastAPI
from pydantic import BaseModel, conlist
import joblib, numpy as np

model  = joblib.load("LogisticRegression.pkl")
scaler = joblib.load("scaler.pkl")
app    = FastAPI(title="Customer Churn Prediction API", version="1.0.0")

class PredictionRequest(BaseModel):
    features: conlist(float, min_length=30, max_length=30)

@app.post("/predict")
def predict(request: PredictionRequest):
    scaled = scaler.transform(np.array(request.features).reshape(1, -1))
    return {
        "prediction": int(model.predict(scaled)[0]),
        "churn_probability": float(model.predict_proba(scaled)[0][1])
    }
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
docker build -t churn-api .
docker run -p 8000:8000 churn-api
# Swagger UI → http://localhost:8000/docs
```

### ✅ Deployment Proof
- **Swagger UI** tested at `http://localhost:8000/docs`
- **POST /predict** → `prediction: 0`, `churn_probability: 0.0072`, HTTP `200 OK`
- **Docker Desktop** → `churn-api` image running, port `8000:8000`, image size `566 MB`

---

## 📊 Stage 5 — Power BI Dashboard

- 📈 Overall churn rate KPI card
- 🗺️ Geographic churn map across cities
- 📋 Churn by contract type
- 💳 Churn by payment method
- 💰 Revenue at risk segmentation
- 🔍 7 interactive filters

> Dashboard file: `Telecom_customer_churn.pbit`

---

## 💡 Key Business Insights

- 📋 **Month-to-month** customers have the highest churn rate — push annual contracts
- 💳 **Electronic check** payers churn most — incentivize auto-pay migration
- ⏱️ **First 12 months** = highest churn risk window — intervene early
- 💰 Churned customers pay **more per month** — high-value customers are leaving
- 🎯 **Decision threshold 0.4** flags more at-risk customers for proactive retention
- ⚡ **PySpark pipeline** achieves higher ROC-AUC (0.849) and scales to millions of records

---

## 🛠️ Tech Stack

| Layer | Tool | Purpose |
|---|---|---|
| **ETL** | SQL Server (SSMS) | Table creation, loading, transformation, views |
| **ML** | Python · Scikit-learn · Pandas · XGBoost | EDA, feature engineering, modeling |
| **Explainability** | SHAP | Feature importance & churn driver analysis |
| **Big Data** | PySpark · Spark MLlib | Distributed preprocessing & model training |
| **API** | FastAPI · Uvicorn · Pydantic | REST inference service |
| **Deployment** | Docker | Containerization & reproducibility |
| **Model Saving** | Joblib | Model & scaler persistence |
| **Dashboard** | Power BI | Business intelligence |
| **Dev Env** | Google Colab | ML & Spark development |

---

## 🚀 How to Run

**Option 1 — Google Colab (ML + PySpark Notebook)**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1R5-NtS4bo7IaDbCzM8FjcYEjJBhnmoZU?usp=sharing)

**Option 2 — Run API with Docker**
```bash
git clone https://github.com/shreevarsha866/Telecom_customer_churn_prediction
cd Telecom_customer_churn_prediction
docker build -t churn-api .
docker run -p 8000:8000 churn-api
# Open → http://localhost:8000/docs
```

**Option 3 — Run API Locally**
```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

**Option 4 — Run PySpark Pipeline**
```bash
pip install pyspark
python churn_spark.py
```

---

## 📁 Repository Structure

```
📦 Telecom_customer_churn_prediction
 ┣ 📓 Telcom_Customer_churn_updated.ipynb  ← ML + PySpark notebook (Colab)
 ┣ 🐍 app.py                               ← FastAPI inference service
 ┣ ⚡ churn_spark.py                       ← Standalone PySpark pipeline
 ┣ 🐳 Dockerfile                           ← Docker container config
 ┣ 📄 requirements.txt                     ← Python dependencies
 ┣ 🗄️ sql/
 ┃   ┣ 01_create_tables.sql
 ┃   ┣ 02_load_data.sql
 ┃   ┣ 03_transformations.sql
 ┃   ┣ 04_views.sql
 ┃   ┗ 05_data_quality_checks.sql
 ┣ 📊 Telecom_customer_churn.pbit          ← Power BI dashboard
 ┣ 📄 WA_Fn-UseC_-Telco-Customer-Churn.csv
 ┣ 🤖 LogisticRegression.pkl
 ┣ ⚙️ scaler.pkl
 ┗ 📖 README.md
```

---

## 💡 Conclusion

- A **full-stack DS pipeline** from raw SQL ETL to deployed FastAPI microservice
- **PySpark MLlib pipeline** achieves ROC-AUC 0.849 — production-ready for big data scale
- **SHAP explainability** identifies contract type and tenure as top churn drivers
- **Threshold tuning at 0.4** improved churn recall to 57% — aligned with business retention goals
- **Docker deployment** ensures reproducibility across any environment

---

## 🔮 Future Work

- Push Docker image to **Docker Hub** for cloud deployment
- Deploy on **AWS EC2 or Azure App Service** for public access
- Add **real-time streaming** from CRM systems using Kafka
- Build **Streamlit frontend** for non-technical user access
- Extend to **multi-class churn reason prediction**

---

## 👩‍💻 Author

**Shreevarsha S** — Data Scientist | ML · NLP · Big Data

[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-7b6ef6)](https://shreevarsha866.github.io/Shreevarsha_Portfolio)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/s-shreevarsha-503887218/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?logo=github)](https://github.com/shreevarsha866)
[![Email](https://img.shields.io/badge/Email-Contact-red?logo=gmail)](mailto:varshashree866@gmail.com)

---
*⭐ If you found this project helpful, please give it a star!*
