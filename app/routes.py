from app import app
from app.controller import PredictController
from flask import request

@app.route('/')
def index():
    return 'URL Api Classification: http://127.0.0.1:5000/api/v1/predict : USE POST Method'

@app.route('/api/v1/predict', methods=['GET', 'POST'])
def prediction():
    if request.method == 'GET':
        return 'URL Api Classification: http://127.0.0.1:5000/api/v1/predict : POST Method'
    else:
        return PredictController.prediction()