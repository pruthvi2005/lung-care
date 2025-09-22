# Lung Cancer Risk Prediction Tool

A web application that helps users assess their risk of lung cancer based on various health and lifestyle factors using machine learning.

## Features

- User authentication (register/login)
- Interactive risk assessment form
- Real-time risk prediction
- Secure data storage
- Responsive design

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/lung-cancer-prediction.git
   cd lung-cancer-prediction
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your browser and go to `http://127.0.0.1:5000`

## Deployment

This application can be deployed to various platforms. Here are some options:

### Option 1: Render.com
1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Set the build command: `pip install -r requirements.txt`
4. Set the start command: `gunicorn app:app`
5. Deploy!

### Option 2: Heroku
1. Install Heroku CLI and login
2. Create a `Procfile` with: `web: gunicorn app:app`
3. Run:
   ```bash
   heroku create
   git push heroku main
   ```

## Technologies Used

- Backend: Python, Flask
- Frontend: HTML, Tailwind CSS, JavaScript
- Database: SQLite (development), PostgreSQL (production)
- Machine Learning: Scikit-learn, XGBoost

## License

This project is licensed under the MIT License.
