import os
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(
    __name__,
    requests_pathname_prefix="/app1/",
    external_stylesheets=external_stylesheets,
)


server = app.server

app.layout = html.Div(children=[
        html.H2("Dash app 1"),
        html.Div(children="""
            Dash: a web application framework for Python
        """),
        dcc.Dropdown(
            id="dropdown",
            options=[{"label": i, "value": i} for i in ["LA", "NYC", "MTL"]],
            value="LA",
        ),
        html.Div(id="display-value"),
        dcc.Graph(
            id='example-graph',
            figure={
                "data": [
                    {"x": [1, 2, 3], "y": [4, 1, 2], "type": "bar", "name": "SF"},
                    {"x": [1, 2, 3], "y": [2, 4, 5], "type": "bar", "name": u'Montréal'}
                ],
                "layout": {
                    "title": "Dash Data Visualization"
                }
            }
        )
    ]
)


@app.callback(
    dash.dependencies.Output("display-value", "children"),
    [dash.dependencies.Input("dropdown", "value")],
) # call back uses the function view function name and binds it to a function that can be accessed in the dashboard html
def display_value(value):
    return 'You have selected "{}"'.format(value)


if __name__ == "__main__":
    app.run_server(debug=True)
