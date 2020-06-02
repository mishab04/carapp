# -*- coding: utf-8 -*-
"""
Created on Sun May 31 20:18:40 2020

@author: User
"""

import dash_core_components as dcc
import dash_html_components as html

def layout():
    yrs = list(range(2,8))
    rating = list(range(1,6))
    condition = list(range(1,11))
    mileage = list(range(8,16))
    layout_page = html.Div([html.H3(id = 'heading',children = 'Car Price Predictor',className="display-4 text-center"),
                       html.Div([
                               html.Div([
                                       html.Header('On road old price'),
                                       dcc.Slider(
                                               id='old_price_range',
                                               min = 500000,
                                               max = 700000,
                                               step = 50000,
                                               value = 550000,
                                               marks = {500000:str(500000),
                                                        700000:str(700000)},
                                               updatemode='drag'
                                               ),
                                        html.Br(),
                                        html.Header('On road new price'),
                                        dcc.Slider(
                                                id ='new_price_range',
                                                min = 700000,
                                                max = 900000,
                                                step = 50000,
                                                value = 750000,
                                                marks = {700000:str(700000),
                                                        900000:str(900000)},
                                                updatemode='drag'
                                                ),
                                        html.Br(),
                                        html.Header('Vehicles age in yrs'),
                                        dcc.Slider(
                                                id = 'years',
                                                min = 2,
                                                max = 7,
                                                marks={i:str(i) for i in yrs},
                                                step = 1,
                                                value = 3,
                                                updatemode='drag'
                                                ),
                                        html.Br(),
                                        html.Header('Total distance covered by vehicle in km'),
                                        dcc.Slider(
                                                id ='distance_covered',
                                                min = 50000,
                                                max = 150000,
                                                step = 10000,
                                                value = 60000,
                                                marks = {50000:str(50000),
                                                         150000:str(150000)},
                                                updatemode='drag'
                                                ),                                        
                                             ],className='col-sm-12 col-md-3 order-1 order-md-1'),
                                html.Div(id = 'priceindicator', className = 'col-sm-12 col-md-6 order-3 order-md-2 font-weight-bold'),
                                html.Div([
                                        html.Header('Overall rating of the new vehicle'),
                                        dcc.Dropdown(
                                                id='rating',
                                                options=[{'label': str(i), 'value': i} for i in rating],
                                                value = 2,
                                                ),
                                        html.Br(),
                                        html.Header('Overall condition of the vehicle'),
                                        dcc.Dropdown(
                                                id='condition',
                                                options=[{'label': str(i), 'value': i} for i in condition],
                                                value = 6,
                                                ),
                                        html.Br(),                                        
                                        html.Header('Current Mileage of the vehicle'),
                                        dcc.Slider(
                                                id ='Mileage',
                                                min = 8,
                                                max = 15,
                                                step = 1,
                                                value = 9,
                                                marks = {i:str(i) for i in mileage},
                                                updatemode='drag'
                                                ),                                          
                                        html.Br(),                                        
                                        html.Header('Top speed of the vehicle'),
                                        dcc.Slider(
                                                id ='Speed',
                                                min = 130,
                                                max = 200,
                                                step = 5,
                                                value = 145,
                                                marks = {130:str(130),
                                                         200:str(200),},
                                                updatemode='drag'
                                                ),                                          
                                        html.Br(),                                        
                                        html.Header('Horse power of the engine '),
                                        dcc.Slider(
                                                id ='Hp',
                                                min = 50,
                                                max = 120,
                                                step = 5,
                                                value = 65,
                                                marks = {50:str(50),
                                                         120:str(120),},
                                                updatemode='drag'
                                                ),                                                                                  
                                        ],className = 'col-sm-12 col-md-3 order-2 order-md-3')],className = 'row')
                       ], className = 'container-lg')
    return layout_page