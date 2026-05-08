#  employee_attrition_project

#  Import Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import joblib
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

#  Load Data
data = pd.read_csv("dataHR_Employee_Attrition.csv")

#  Preprocessing
le = LabelEncoder()
for col in data.select_dtypes(include=['object']).columns:
    data[col] = le.fit_transform(data[col])

scaler = StandardScaler()
features = data.drop('Attrition', axis=1)
target = data['Attrition']

features_scaled = scaler.fit_transform(features)

X_train, X_test, y_train, y_test = train_test_split(features_scaled, target, test_size=0.2, random_state=42)

# Train Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

#  Evaluate Model
y_pred = model.predict(X_test)
report = classification_report(y_test, y_pred)
acc = accuracy_score(y_test, y_pred)
print("\nModel Accuracy:", acc)
print("\nClassification Report:\n", report)

#  Save Model and Scaler
joblib.dump(model, 'models/model.pkl')
joblib.dump(scaler, 'models/scaler.pkl')

#  Streamlit App
st.set_page_config(page_title="Employee Attrition Predictor", layout="wide")
st.title("🧠 Employee Attrition Prediction Dashboard")

st.sidebar.header("📋 Input Features")
def user_input():
    age = st.sidebar.slider('Age', 18, 60, 30)
    distance = st.sidebar.slider('Distance From Home', 1, 30, 10)
    job_satisfaction = st.sidebar.selectbox('Job Satisfaction', [1, 2, 3, 4])
    years_at_company = st.sidebar.slider('Years At Company', 0, 40, 5)
    monthly_income = st.sidebar.slider('Monthly Income', 1000, 20000, 5000)
    overtime = st.sidebar.selectbox('OverTime', ['Yes', 'No'])
    overtime = 1 if overtime == 'Yes' else 0
    
    user_df = pd.DataFrame({
        'Age': [age],
        'DistanceFromHome': [distance],
        'JobSatisfaction': [job_satisfaction],
        'YearsAtCompany': [years_at_company],
        'MonthlyIncome': [monthly_income],
        'OverTime': [overtime],
    })
    return user_df

user_df = user_input()

# Align features
user_df_full = pd.DataFrame(np.zeros((1, features.shape[1])), columns=features.columns)
for col in user_df.columns:
    user_df_full[col] = user_df[col]

scaler = joblib.load('models/scaler.pkl')
model = joblib.load('models/model.pkl')

user_scaled = scaler.transform(user_df_full)
prediction = model.predict(user_scaled)
pred_proba = model.predict_proba(user_scaled)

st.subheader("🔍 Prediction Result")
result = "Yes – High Risk of Leaving" if prediction[0] == 1 else "No – Likely to Stay"
color = "red" if prediction[0] == 1 else "green"
st.markdown(f"<h2 style='color:{color};'>{result}</h2>", unsafe_allow_html=True)

st.subheader("📊 Prediction Probability")
st.write(f"Probability of Leaving: {pred_proba[0][1]*100:.2f}%")

st.subheader("📉 Feature Importance")
importances = model.feature_importances_
feature_imp = pd.Series(importances, index=features.columns).sort_values(ascending=False).head(10)
st.bar_chart(feature_imp)

st.markdown("---")
st.caption("Developed using Streamlit + Scikit-learn + VS Code by YOU 🚀")
