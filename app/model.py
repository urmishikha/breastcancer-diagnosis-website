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
    try:
        model = load_model()
        features = np.array(features).reshape(1, -1)  # Ensure 2D input for prediction
        prediction = model.predict(features)[0]  # Get the prediction
        return 'Malignant' if prediction == 1 else 'Benign'
    except Exception as e:
        raise ValueError(f"Error in prediction: {e}")
