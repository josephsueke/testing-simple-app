# %%
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import plotly.graph_objs as go

# Create a DataFrame with random data
df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])

# Create a bar chart as a Plotly figure
data = []
for column in df.columns:
    data.append(go.Bar(name=column, x=df.index, y=df[column]))

# Let plotly arrange the data for us
figure = go.Figure(data=data)
figure.update_layout(barmode='stack')

# Create a Dash app
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Random Bar Chart'),
    dcc.Graph(
        id='example-graph',
        figure=figure
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)


