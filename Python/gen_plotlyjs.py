# Filename: gen_plotlyjs.py
#
# Generate the Temperature and Humidity Graphs
#
# Create a new html file containing the graph created with
# PlotlyJS offline. Two graph are created (Temp and Hum) for
# each cluster

from plotly.offline import plot
from plotly.graph_objs import Scatter, Layout, Bar
from datetime import datetime


def to_unix_time(dt):
    epoch = datetime.utcfromtimestamp(0)
    return (dt - epoch).total_seconds() * 1000


def update_graph_data(data):
    temp_data = [Scatter(
        x=data.loc[sensor].date,
        y=data.loc[sensor].Temp,
        name="Data Node " + str(sensor),
        mode='markers+lines',
    ) for sensor in data.index.unique()]
    hum_data = [Scatter(
        x=data.loc[sensor].date,
        y=data.loc[sensor].Humidity,
        name="Data Node " + str(sensor),
        mode='markers+lines',
    ) for sensor in data.index.unique()]
    return temp_data, hum_data


def update_graph(data, destination, from_date, until_date):
    temp_data, hum_data = update_graph_data(data);
    range_ = [to_unix_time(from_date), to_unix_time(until_date)]
    temp_fig = dict(
        data=temp_data,
        layout=Layout(
            title='Temperature',
            yaxis=dict(
                title='Temperature [ C ]'
            ),
            xaxis=dict(
                title='Date',
                range=range_,
            ),
        )
    )
    hum_fig = dict(
        data=hum_data,
        layout=Layout(
            title='Humidity',
            yaxis=dict(
                title='Humidity [ % ]'
            ),
            xaxis=dict(
                title='Date',
                range=range_,
            ),
        )
    )
    temp_filename = destination + '/Temp_AllNodes.html'
    hum_filename = destination + '/Hum_AllNodes.html'
    temp_url = plot(temp_fig, filename=temp_filename)
    hum_url = plot(hum_fig, filename=hum_filename)
    return temp_url, hum_url
