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
        'numpy==1.21.6',
        'scikit-learn==1.0.2',
        'xgboost==1.6.2',
        'joblib==1.1.1',
        'python-dotenv==0.21.0',
        'gunicorn==20.1.0'
    ],
    python_requires='>=3.8.0, <3.9.0',
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
