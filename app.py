# app.py
import dash
from dash import html
from PlotIterator import PlotIterator  # nur hier importieren, keine Schleife

app = dash.Dash(__name__)
pi = PlotIterator()

app.layout = html.Div([
    html.H1("Minimal Dash App mit PlotIterator"),
    html.Ul([html.Li(str(val)) for val in pi.data])
])
