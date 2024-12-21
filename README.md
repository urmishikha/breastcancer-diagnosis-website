# Breast Cancer Diagnosis App

This is a full-stack Python app that helps diagnose breast cancer using machine learning. It uses Flask for the web framework, scikit-learn for machine learning, and a simple HTML form for user input.

## Features

User-friendly web interface for entering diagnostic parameters.

Backend powered by Flask for handling requests and predictions.

Machine learning model trained on a breast cancer dataset.

Real-time prediction of whether a tumor is malignant or benign.

Responsive design for desktop and mobile devices.

## Project Structure

- `app/`: Contains the Flask app and related files.
  - `routes.py`: Defines the routes for handling requests.
  - `model.py`: Contains the logic for loading the trained machine learning model and making predictions.
  - `forms.py`: Defines the form for user input.
  - `templates/`: HTML templates for rendering the pages.
  - `static/`: CSS and JavaScript for styling and client-side functionality.
- `data/`: Contains the dataset used for training the machine learning model.
- `model.pkl`: The trained machine learning model.
- `requirements.txt`: List of dependencies for the project.

## How to Run
Install the dependencies:

pip install -r requirements.txt

Run the Flask app:

python app/routes.py

Open the app in your browser:

Navigate to http://127.0.0.1:5000/ in your web browser to use the app.


## Future Improvements

Add user authentication for enhanced security.

Implement more advanced machine learning models to improve prediction accuracy.

Allow users to upload datasets for custom predictions.

Integrate data visualization for better insights into predictions.
