import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pickle

# Load the breast cancer dataset
def load_data():
    data = load_breast_cancer()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['target'] = data.target
    return df, data.feature_names

# Split the dataset into train and test sets
def split_data(df, feature_names, test_size=0.2, random_state=42):
    X = df[feature_names]
    y = df['target']
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

# Train a Logistic Regression model
def train_model(X_train, y_train, max_iter=5000, random_state=42):
    model = LogisticRegression(max_iter=max_iter, random_state=random_state)
    model.fit(X_train, y_train)
    return model

# Evaluate the model
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy * 100:.2f}%")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

# Save the trained model
def save_model(model, file_name="model.pkl"):
    with open(file_name, "wb") as file:
        pickle.dump(model, file)
    print(f"Model saved as '{file_name}'")

# Main function
def main():
    df, feature_names = load_data()
    X_train, X_test, y_train, y_test = split_data(df, feature_names)
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)
    save_model(model)

if __name__ == "__main__":
    main()
