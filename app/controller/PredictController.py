import pickle
from app import response, app
from flask import request

def prediction():
    try:
        Location = int(request.form['Location'])
        MaxTemp = float(request.form['MaxTemp'])
        Rainfall = float(request.form['Rainfall'])
        Evaporation = float(request.form['Evaporation'])
        Sunshine = float(request.form['Sunshine'])
        WindGustDir = int(request.form['WindGustDir'])
        WindGustSpeed = float(request.form['WindGustSpeed'])
        WindDir9am = int(request.form['WindDir9am'])
        WindDir3pm = int(request.form['WindDir3pm'])
        WindSpeed9am = float(request.form['WindSpeed9am'])
        WindSpeed3pm = float(request.form['WindSpeed3pm'])
        Humidity3pm = float(request.form['Humidity3pm'])
        Pressure9am = float(request.form['Pressure9am'])
        Cloud9am = float(request.form['Cloud9am'])
        Cloud3pm = float(request.form['Cloud3pm'] )
        RainToday = int(request.form['RainToday'])
        Year = int(request.form['Year'])
        Month = int(request.form['Month'])
        Day = int(request.form['Day'])

        data = [Location, MaxTemp, Rainfall, Evaporation, Sunshine, WindGustDir, WindGustSpeed, WindDir9am, WindDir3pm, WindSpeed9am, WindSpeed3pm, Humidity3pm, Pressure9am, Cloud9am, Cloud3pm, RainToday, Year, Month, Day]
        lr_filename = './app/models/Rain_in_Australia_LR1.pkl'
        lr_clf = pickle.load(open(lr_filename, 'rb'))
        pred = lr_clf.predict([data])
        if pred == 0:
            return response.succes('Hujan', 'Succes')
        else:
            return response.succes('Tidak Hujan', 'Succes')
        
    except Exception:
        return response.badRequest()