# app/model.py
import pickle
import numpy as np

# Load the model (assuming it's trained and saved)
def load_model():
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

# Prediction function
def predict_cancer(features):
    model = load_model()
    features = np.array(features).reshape(1, -1)  # Convert to 2D array for prediction
    prediction = model.predict(features)[0]  # Predict cancer type (0 = benign, 1 = malignant)
    return 'Malignant' if prediction == 1 else 'Benign'
