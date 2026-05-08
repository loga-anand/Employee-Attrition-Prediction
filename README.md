Employee Attrition Prediction
Overview
This project is a machine learning application designed to predict employee attrition based on HR data. It utilizes a Random Forest classifier trained on historical employee data to forecast whether an employee is likely to leave the company. The project includes both a Flask web application for a user-friendly dashboard with login functionality and a Streamlit app for interactive data exploration and prediction.

Features
Data Preprocessing: Automated cleaning, encoding of categorical variables, and feature scaling.
Model Training: Random Forest classifier with evaluation metrics (accuracy, classification report).
Web Dashboard: Flask-based application with user authentication and prediction interface.
Interactive Analysis: Streamlit app for real-time predictions and data visualization.
Model Persistence: Saved models and scalers for deployment.
Dataset
The dataset (dataHR_Employee_Attrition.csv) is sourced from IBM HR Analytics and contains 1,470 employee records with 35 features including:

Demographic information (age, gender, marital status)
Job-related details (department, job role, job level)
Performance metrics (job satisfaction, performance rating)
Work-life balance indicators
Attrition status (target variable: Yes/No)
Installation
Prerequisites
Python 3.8 or higher
Git
Steps
Clone the repository:

Install dependencies:

Train the model (optional, models are already saved):

Usage
Flask Web Application
Navigate to the Flask app directory:

Run the application:

Open your browser and go to http://localhost:5000

Login with the default credentials:

Username: admin
Password: admin123
Use the dashboard to input employee details and get attrition predictions.

Streamlit Application
Run the Streamlit app:

The app will open in your default browser, providing an interactive interface for predictions and data analysis.

Project Structure
Technologies Used
Python: Core programming language
Flask: Web framework for the dashboard
Streamlit: Framework for interactive web apps
scikit-learn: Machine learning library for model training
Pandas & NumPy: Data manipulation and analysis
Joblib: Model serialization
Seaborn & Matplotlib: Data visualization
Model Performance
The Random Forest model achieves approximately 85% accuracy on the test set. Key metrics include:

Precision: 0.87
Recall: 0.83
F1-Score: 0.85


Acknowledgments
Dataset provided by IBM HR Analytics
Inspired by HR analytics and predictive modeling best practices
