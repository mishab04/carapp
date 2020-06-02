# -*- coding: utf-8 -*-
"""
Created on Sun May 31 12:08:20 2020

@author: User
"""

import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from loaded_model import loadmodel
from layout import layout
import pandas as pd
import numpy as np


app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
app.layout = layout()

@app.callback(Output('priceindicator', 'children'),
              [Input('old_price_range', 'value'),
               Input('new_price_range', 'value'),
               Input('years', 'value'),
               Input('distance_covered', 'value'),
               Input('rating', 'value'),
               Input('condition', 'value'),
               Input('Mileage', 'value'),
               Input('Speed', 'value'),
               Input('Hp', 'value')])
def predict_price(value1,value2,value3,value4,value5,value6,value7,value8,value9):
    try:
        model = loadmodel('models/joblib_model.pkl')
    except:
        return 'unable to load file'
    X_single_point = pd.DataFrame(data = np.array([[value1,value2,value3,value4,int(value5),int(value6),value7,value8,value9]]),
                              columns = ['on road old', 'on road now', 'years', 'km ', 'rating', 'condition', 'economy', 'top speed', 'hp']               
                              )
    predicted_price = model.predict(X_single_point)
    return  'Price : {}'.format(int(round(predicted_price[0])))

if __name__ == "__main__":
    app.run_server()