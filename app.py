from flask import Flask,request,render_template
import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustomException
import sys
import pickle

app = Flask(__name__)

# Load the ML model
model = pickle.load(open("model_copy_2.pkl","rb"))

@app.route('/')
def home():
    return render_template('home.html', prediction_text='')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input values from the form
    

    country_dict_reversed = {'Congo, DRC': 0, "Côte d'Ivoire": 1, 'Haiti': 2, 'Mozambique': 3, 'Nigeria': 4, 'Rwanda': 5, 'South Africa': 6, 'Tanzania': 7, 'Uganda': 8, 'Vietnam': 9, 'Zambia': 10, 'Zimbabwe': 11}
    country_name = country_dict_reversed[request.form['country_name']]
    
    vendor_dict_reversed = {'CIP': 0, 'DAP': 1, 'DDP': 2, 'EXW': 3, 'FCA': 4, 'RDC': 5}
    vendor_name = vendor_dict_reversed[request.form['vendor_name']]

    shipment_mode_dict_reversed = {'Air': 0, 'Air Charter': 1, 'Ocean': 2, 'Truck': 3}
    shipment_mode = shipment_mode_dict_reversed[request.form['shipment_mode']]


    unit_of_measure = int(request.form['unit_of_measure'])
    line_item_quantity = int(request.form['line_item_quantity'])
    line_item_value = int(request.form['line_item_value'])
    pack_price = int(request.form['pack_price'])
    unit_price = float(request.form['unit_price'])
    weight = int(request.form['weight'])

    manufacturing_site_dict_reversed = {'China': 0, 'Cyprus': 1, 'Nashik': 2, 'Port Elizabeth': 3, 'Thailand': 4, 'Switzerland': 5, 'Haarlem': 6, 'France': 7, 'Germany': 8, 'India': 9, 'Latina': 10, 'Poland': 11, 'Canada': 12, 'South Africa': 13, 'Puerto Rico': 14}
    manufacturing_site =  manufacturing_site_dict_reversed[request.form['manufacturing_site']]

    distance = int(request.form['distance'])

    # Perform prediction using the ML model
    input_data = [[country_name,vendor_name,shipment_mode,unit_of_measure,line_item_quantity,line_item_value,pack_price,unit_price,weight,manufacturing_site,distance]]
    prediction = model.predict(input_data)[0]

    # Format the prediction result as a string
    result = f"The predicted consignment price is: {prediction}"
    result = ('%.2f' % prediction)
    return render_template('home.html', prediction_text=result)

if __name__=="__main__":
    app.run(debug = True)