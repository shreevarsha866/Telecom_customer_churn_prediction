Predict which telecom customers are about to leave — a full end-to-end pipeline from SQL ETL to Python ML to Power BI dashboard that turns churn risk into actionable retention strategy.

Problem Statement In telecom, acquiring a new customer costs 5 to 10 times more than retaining one. With a 26.54% churn rate across 7,043 customers, identifying at-risk customers before they leave is a critical business need. This project delivers a complete predictive solution from raw data ingestion to stakeholder-ready dashboards.

What This Project Does

SQL Server ETL pipeline — stages, transforms, and curates raw CSV data for analysis
Exploratory Data Analysis — uncovers churn drivers across contract type, tenure, and payment method
ML models trained and compared — Logistic Regression vs Random Forest with hyperparameter tuning
Interactive Power BI dashboard — KPI cards, geographic churn map, and revenue analysis 5.Saved model artifacts — .pkl files ready for deployment or inference on new customers
Project Structure

image
Stage 1 — SQL Server ETL Pipeline

Raw data was processed through a structured ETL pipeline before any ML work.

CSV File → Staging Table → Transformation → Final Table → Analytics Views

Steps performed in SQL Server (SSMS):

Created staging and final schema tables
Loaded raw CSV via flat file import
Applied data transformations and quality checks
Built analytical views for churn rate by contract type
Output: clean, analysis-ready dataset passed into Python
Stage 2 — Exploratory Data Analysis:

Dataset: 7,043 customers.
Churn rate: 26.54%.
Moderate class imbalance — ROC-AUC prioritized over accuracy.
Key Finding Insight:

Contract type Month-to-Month customers churn far more than 1-year or 2-year holders
TenureChurned customers have significantly lower average tenurePayment method Electronic check users churn at the highest rate
Monthly charges Churned avg $75/month vs Stayed avg $63/month
Senior citizensAround 16% of base — distinct behavioral segment
Stage 3 — Machine Learning Pipeline: - Preprocessing Steps

Step Method Target encoding Churn: Yes = 1, No = 0
Dropped columncustomerID (not predictive)
TotalCharges fixConverted to numeric, 11 NaN rows dropped
Categorical encodingpd.get_dummies() with drop_first=True
Feature scaling StandardScaler — fit on train, transform on testTrain/test split80/20, random_state=42, stratify=y
Models Trained:

1. Logistic Regression
LogisticRegression(max_iter=1000)

2. Random Forest
RandomForestClassifier(n_estimators=300, random_state=42, class_weight='balanced')

3. Hyperparameter Tuning
GridSearchCV on Logistic Regression — 5-fold CV, scoring = roc_auc: pythonparam_grid = { 'C': [0.01, 0.1, 0.5, 1, 5, 10], 'penalty': ['l2'] }

Model Comparison

ModelROC-AUC Notes Logistic Regression (baseline)0.835 Strong interpretable baselineRandom Forest0.819Higher complexity, lower AUCLogistic Regression (tuned)0.835 Final model selected
Final model: Tuned Logistic Regression. Decision threshold adjusted to 0.4 to improve churn recall to 57%.
Saved Model Artifacts Three files saved with joblib:

LogisticRegression.pkl — FINAL prediction model
RandomForestClassifier.pkl — feature importance reference
scaler.pkl — StandardScaler (required for Logistic Regression)
**Load and predict on new data: **

pythonimport joblib model = joblib.load("LogisticRegression.pkl") scaler = joblib.load("scaler.pkl")

X_scaled = scaler.transform(X_new) churn_prob = model.predict_proba(X_scaled)[:, 1] churn_flag = (churn_prob > 0.4).astype(int)

Stage 4 — Power BI Dashboard File: Report_BI.pbix — Open with Power BI Desktop (free)

KPI Cards
MetricValueTotal Customers 7,043
Total Revenue$21.37M
Total Refund$13.82K
Average Charges$2.28K
Total Tenure (months)228K
Churn Rate26.54%
Dashboard Visuals
In Visual What It Shows:

Revenue by Contract (Donut)Month-to-Month $6.16M, One Year $6.17M, Two Year $9.04M
Churn Category (Bar)Competitor 841, Dissatisfaction 321, Attitude 314, Price 211, Other 182
Customers by Gender (Pie)Male 50.48%, Female 49.52%
Customers and Revenue by Age Above-60 is the largest customer and revenue segment
Avg Monthly Charges by Status Churned $75, Stayed $63, Joined $44
Geographic MapRevenue and churn rate across California cities
Interactive Filters: Streaming TV, Streaming Music, Streaming Movie, Unlimited Data, Internet Service, Internet Type (Cable / DSL / Fiber Optic), Premium Support
Tech Stack -LayerToolsETLSQL Server, SSMS

CSV Flat File Import Language Python — Google Colab / Jupyter
Data Wrangling
Pandas, NumPy
Visualization
Matplotlib, Seaborn
Machine Learning
Scikit-learn — LogisticRegression, RandomForestClassifier, GridSearchCV
Model Persistence Joblib
BI DashboardPower BI Desktop
Getting Started

Clone the repository bashgit clone https://github.com/shreevarsha866/Telecom-customer-churn-prediction.git cd Telecom-customer-churn-prediction
Install dependencies bashpip install pandas numpy matplotlib seaborn scikit-learn joblib
Run the notebook Open Telcom_Customer_churn.ipynb in Jupyter or Google Colab. Place WA_Fn-UseC_-Telco-Customer-Churn.csv at /content/ for Colab or update the path in Cell 1.
Predict on new customers
pythonimport joblib model = joblib.load("LogisticRegression.pkl") scaler = joblib.load("scaler.pkl") X_scaled = scaler.transform(X_new) churn_prob = model.predict_proba(X_scaled)[:, 1] at_risk = (churn_prob > 0.4).astype(int)

5. Open the Power BI dashboard

Open Report_BI.pbix in Power BI Desktop and explore with the interactive filters.
Final Results

Metric Value Final Model Logistic Regression (GridSearchCV tuned)
Accuracy 80% ROC-AUC Score 0.835 Churn Recall (threshold = 0.4)57%
Dataset Size 7,043 customersChurn Rate26.54%
Business Recommendations

Competitor churn is the top reason (841 cases) — launch targeted competitive pricing campaigns immediately
Month-to-month customers are highest risk — incentivize upgrades to annual contracts early in tenure
High-charge new customers are most vulnerable — churned customers pay $12/month more on average
Above-60 age group generates the most revenue — prioritize premium support offerings for this segment
Use a threshold of 0.4 instead of 0.5 when scoring customers — improves recall by flagging more true churners
License This project is licensed under the MIT License.
