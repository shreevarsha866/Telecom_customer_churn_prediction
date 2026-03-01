from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, conlist
import joblib
import numpy as np

# --------------------------------------------------
# Load trained model and scaler at startup
# --------------------------------------------------

model = joblib.load("LogisticRegression.pkl")
scaler = joblib.load("scaler.pkl")

# --------------------------------------------------
# Create FastAPI app
# --------------------------------------------------

app = FastAPI(
    title="Customer Churn Prediction API",
    description="FastAPI-based ML inference service with Docker deployment",
    version="1.0.0"
)

# --------------------------------------------------
# Request Schema
# --------------------------------------------------

class PredictionRequest(BaseModel):
    # Exactly 30 numerical features required
    features: conlist(float, min_length=30, max_length=30)


# --------------------------------------------------
# Response Schema
# --------------------------------------------------

class PredictionResponse(BaseModel):
    prediction: int
    churn_probability: float


# --------------------------------------------------
# Health Check Endpoint
# --------------------------------------------------

@app.get("/health")
def health():
    return {"status": "API is running"}


# --------------------------------------------------
# Root Endpoint
# --------------------------------------------------

@app.get("/")
def home():
    return {"message": "Customer Churn Prediction API is live"}


# --------------------------------------------------
# Prediction Endpoint
# --------------------------------------------------

@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):

    try:
        # Convert input list to numpy array
        input_data = np.array(request.features).reshape(1, -1)

        # Scale input
        scaled_data = scaler.transform(input_data)

        # Make prediction
        prediction = model.predict(scaled_data)[0]
        probability = model.predict_proba(scaled_data)[0][1]

        return PredictionResponse(
            prediction=int(prediction),
            churn_probability=float(probability)
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))