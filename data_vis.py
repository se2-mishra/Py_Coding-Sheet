# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 15:08:48 2020

@author: User
"""
import datetime 
import pandas_datareader.data as web 
import dash 
import dash_core_components as dcc     
import dash_html_components as html 
from dash.dependencies import Input, Output  
app = dash.Dash() 
app.title = "Stock Visualisation"
app.layout = html.Div(children =[ 
    html.H1("Stock Visualisation Dashboard"), 
      
    html.H4("Please enter the stock name"), 
  
    dcc.Input(id ='input', value ='', type ='text'), 
  
    html.Div(id ='output-graph') 
]) 
def update_value(input_data): 
    # Reads stock prices from 1st January 2010 
    start = datetime.datetime(2010, 1, 1)  
    end = datetime.datetime.now() 
  
    # Read stock data from yahoo's finance API from start to end  
    df = web.DataReader(input_data, 'yahoo', start, end) 
        
    return dcc.Graph(id ="example", 
        figure ={ 
            'data':[{'x':df.index, 'y':df.Close, 'type':'line', 'name':input_data}, 
            ], 
            'layout':{ 
                'title':input_data 
            } 
        } 
    ) 
    
####################################################################
if __name__ == '__main__': 
    app.run_server() 