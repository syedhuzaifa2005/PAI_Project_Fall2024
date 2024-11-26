import pandas as pd
from joblib import load

# Load pre-trained model and preprocessors
def load_model():
    model = load('ml_model/logistic_regression_model.joblib')
    imputer = load('ml_model/imputer.joblib')
    scaler = load('ml_model/scaler.joblib')
    return model, imputer, scaler

# Define the top 10 features
top_10_features = [
    'area_mean', 'concave points_mean', 'concave points_worst', 
    'concavity_worst', 'perimeter_mean', 'perimeter_worst', 
    'radius_mean', 'radius_worst', 'texture_mean', 'texture_worst'
]

# Preprocess and predict
def predict_cancer(data):
    model, imputer, scaler = load_model()

    # Create a DataFrame from input data
    top_10_input_data = {key: data[key] for key in top_10_features}
    input_data = pd.DataFrame([top_10_input_data])

    # Apply imputation and scaling
    input_data = imputer.transform(input_data)
    input_data = scaler.transform(input_data)

    # Predict the class and probability
    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)

    return prediction[0], probability[0][1]