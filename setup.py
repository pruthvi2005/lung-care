from setuptools import setup, find_packages

setup(
    name="lung_cancer_prediction",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'Flask==2.3.3',
        'Flask-SQLAlchemy==3.1.1',
        'Werkzeug==2.3.7',
        'pandas==1.5.3',
        'numpy==1.24.4',
        'scikit-learn==1.2.2',
        'xgboost==1.7.6',
        'joblib==1.2.0',
        'python-dotenv==1.0.0',
        'gunicorn==21.2.0'
    ],
    python_requires='>=3.9.0, <3.10.0',
    classifiers=[
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
