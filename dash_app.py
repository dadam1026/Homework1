import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output, State
import pandas as pd
from os import listdir, remove
import pickle
from time import sleep
import candlestick_app
import file_input_n_output


from helper_functions import * # this statement imports all functions from your helper_functions file!

# Run your helper function to clear out any io files left over from old runs
# 1:
check_for_and_del_io_files()


# Make a Dash app!
app = dash.Dash(__name__)

# Define the layout.
app.layout = html.Div([

    # Section title
    html.H1("Section 1: Fetch & Display exchange rate historical data"),

    # Currency pair text input, within its own div.
    html.Div(
        [
            "Input Currency: CHFUSD",
            # Your text input object goes here:

        ],
        # Style it so that the submit button appears beside the input.
        style={'display': 'inline-block'}
    ),
    # Submit button:
    <input type="submit">
    ,
    # Line break
    html.Br(),
    # Div to hold the initial instructions and the updated info once submit is pressed
    app.layout = html.Div([
    html.Div(dcc.Input(id='currency-pair', type='text')),
    html.Button('Submit', id='submit-button', n_clicks=0),
    html.Div(id='output-div', children='Enter a currency code and press 'submit'')
    ])
    ,
    html.Div([
        # Candlestick graph goes here:
        dcc.Graph(id='candlestick-graph')
    ]),
    # Another line break
    html.Br(),
    # Section title
    html.H1("Section 2: Make a Trade"),
    # Div to confirm what trade was made
    html.Div([
        file_input_n_output.my_func()
    ]),
    # Radio items to select buy or sell
    dcc.RadioItems(
        options=[
            {'label': 'Buy', 'value': 'Buy'},
            {'label': 'Sell', 'value': 'Sell'},
        ],
        value='Buy'
    )
    ,
    # Text input for the currency pair to be traded
    <input type="CHFUSD">
    ,
    # Numeric input for the trade amount
    <input type="2000">
    ,
    # Submit button for the trade
    <input type="Trade">


])

# Callback for what to do when submit-button is pressed
@app.callback(
    [ # there's more than one output here, so you have to use square brackets to pass it in as an array.
    ,

    ],
    ,

)
def update_candlestick_graph(n_clicks, value): # n_clicks doesn't get used, we only include it for the dependency.

    # Now we're going to save the value of currency-input as a text file.

    # Wait until ibkr_app runs the query and saves the historical prices csv

    # Read in the historical prices


    # Remove the file 'currency_pair_history.csv'

    # Make the candlestick figure

    # Give the candlestick figure a title


    # Return your updated text to currency-output, and the figure to candlestick-graph outputs
    return ('Submitted query for ' + value), fig

# Callback for what to do when trade-button is pressed
@app.callback(
    ,
    ,
    ,
    # We DON'T want to start executing trades just because n_clicks was initialized to 0!!!
    prevent_initial_call=True
)
def trade(n_clicks, action, trade_currency, trade_amt): # Still don't use n_clicks, but we need the dependency

    # Make the message that we want to send back to trade-output


    # Make our trade_order object -- a DICTIONARY.

    # Dump trade_order as a pickle object to a file connection opened with write-in-binary ("wb") permission:


    # Return the message, which goes to the trade-output div's "children" attribute.
    return msg

# Run it!
if __name__ == '__main__':
    app.run_server(debug=True)
