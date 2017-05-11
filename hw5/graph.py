#!/usr/bin/env python3

""" Automate the graph layout formatting process for reports. """
import argparse
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np
from scipy import stats

py.sign_in('rodrigovalle', '7Efaat8lp3eEIgkluwLv')

parser = argparse.ArgumentParser(
    description='Automate graph layout formatting process for lab reports',
)
parser.add_argument('NAME', type=str, help='What to name the plot on plot.ly')
parser.add_argument('TITLE', type=str, help='What to title the plot')
parser.add_argument('X_AXIS', type=str, help='What to label the x axis')
parser.add_argument('Y_AXIS', type=str, help='What to label the y axis')
parser.add_argument('CSV_FILE', type=str, help='Two column CSV file with X and Y data')
parser.add_argument('--regression', action='store_true', help='Perform a regression')
args = parser.parse_args()

WIDTH = 1200
HEIGHT = 800

FONT = go.Font(size=17)
TITLEFONT = go.Font(size=33)
AXISFONT = go.Font(size=26)

PADDING = 5
LEFT = 100
RIGHT = 70
TOP = 70
BOTTOM = 80

x_data, y_data = np.loadtxt(args.CSV_FILE, delimiter=',', skiprows=1, unpack=True)

scatter = go.Scatter(
    x=x_data,
    y=y_data,
    mode='markers'
)

layout = go.Layout(
    font=FONT,
    title='${}$'.format(args.TITLE),
    titlefont=TITLEFONT,
    xaxis={'title': '${}$'.format(args.X_AXIS), 'titlefont': AXISFONT},
    yaxis={'title': '${}$'.format(args.Y_AXIS), 'titlefont': AXISFONT},
    margin={'l': LEFT, 'r': RIGHT, 't': TOP, 'b': BOTTOM, 'pad': PADDING},
    width=WIDTH,
    height=HEIGHT,
    showlegend=False
)

if args.regression:
    m, b, r_value, p_value, std_err = stats.linregress(x_data, y_data)
    line = m*x_data + b

    fit = go.Scatter(
        x=x_data,
        y=line,
        mode='lines'
    )

    annotation = go.Annotation(
        text='$R^2 = {}\\\\m={} \pm {}\\\\b = {}$'.format(r_value**2, m, std_err, b),
        showarrow=True
    )

    data = [scatter, fit]
    layout.annotations=[annotation]

else:
    data = [scatter]

fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename=args.NAME)
