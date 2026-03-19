# app.py
import dash
from dash import html
from PlotIterator import PlotIterator

# Dash App erstellen
app = dash.Dash(__name__)
pi = PlotIterator()

# Minimal Layout
app.layout = html.Div([
    html.H1("Minimal Dash App mit PlotIterator"),
    html.Ul([html.Li(str(val)) for val in pi.data])
])