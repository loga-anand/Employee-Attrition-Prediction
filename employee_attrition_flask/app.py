from flask import Flask, render_template, request, redirect, url_for, session, flash
import os
import pandas as pd
import numpy as np
import joblib
import json
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this!

# Dummy model & scaler load placeholders (replace with your own)
# model = joblib.load('models/model.pkl')
# scaler = joblib.load('models/scaler.pkl')

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Dummy user check; replace with real user validation
        if username == 'admin' and password == 'admin123':
            session['username'] = username
            session['role'] = 'admin'
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials', 'danger')
    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))

    prediction = None
    probability = None

    if request.method == 'POST':
        # Process form input and do prediction here
        prediction = "No – Likely to Stay"
        probability = "85%"

    return render_template('dashboard.html', username=session['username'], role=session['role'], prediction=prediction, probability=probability)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
