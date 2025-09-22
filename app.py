from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os
import pandas as pd
import joblib
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this to a secure secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Create database tables
with app.app_context():
    db.create_all()

# Load the machine learning model (placeholder - replace with actual model loading)
# model = joblib.load('path_to_your_model.pkl')

def predict_risk_level(features):
    """
    Predict the risk level based on input features
    In a real application, this would use the trained model
    """
    # This is a placeholder - replace with actual model prediction
    risk_score = sum(features.values()) / len(features)
    
    if risk_score <= 3:
        return 'Low', risk_score
    elif risk_score <= 6:
        return 'Medium', risk_score
    else:
        return 'High', risk_score

# Routes
@app.route('/')
def index():
    return redirect(url_for('welcome'))

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['username'] = user.username
            flash('Logged in successfully!', 'success')
            return redirect(url_for('predict'))
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        if password != confirm_password:
            flash('Passwords do not match', 'error')
            return redirect(url_for('register'))
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'error')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered', 'error')
            return redirect(url_for('register'))
        
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, email=email, password=hashed_password)
        
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('welcome'))

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if 'user_id' not in session:
        flash('Please log in to access the risk assessment', 'warning')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        # Get form data
        features = {
            'air_pollution': float(request.form.get('air_pollution', 5)),
            'alcohol_use': float(request.form.get('alcohol_use', 5)),
            'dust_allergy': float(request.form.get('dust_allergy', 5)),
            'occupational_hazards': float(request.form.get('occupational_hazards', 5)),
            'genetic_risk': float(request.form.get('genetic_risk', 5)),
            'chronic_lung_disease': float(request.form.get('chronic_lung_disease', 5)),
            'smoking': float(request.form.get('smoking', 5)),
            'passive_smoker': float(request.form.get('passive_smoker', 5)),
            'fatigue': float(request.form.get('fatigue', 5)),
            'dry_cough': float(request.form.get('dry_cough', 5))
        }
        
        # Get prediction (in a real app, this would use the ML model)
        risk_level, risk_score = predict_risk_level(features)
        
        # In a real app, you would save this prediction to the database
        # prediction = Prediction(user_id=session['user_id'], risk_level=risk_level, risk_score=risk_score, **features)
        # db.session.add(prediction)
        # db.session.commit()
        
        # For now, we'll just pass the result to the template
        return render_template('predict.html', 
                             prediction_made=True,
                             risk_level=risk_level,
                             risk_score=risk_score,
                             **features)
    
    return render_template('predict.html', prediction_made=False)

if __name__ == '__main__':
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()
    
    # Run the app
    app.run(debug=True)
