import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from tabs.overview import tab1
from tabs.eda import tab2
from tabs.model_performance import tab3
from tabs.shap import tab4
from tabs.live_predictor import tab5, register_callbacks

app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.COSMO,
                                      "https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap"
                                      ])

register_callbacks(app)
app.layout = html.Div([
    dbc.Row([
        dbc.Col([
            html.Div([html.H1("Mental Health Analysis",
                className="text-primary mt-3",
                style={"font-weight": "bold", "text-align": "center"}),
            html.P("An analysis of mental health issues in the workplace.",
                                    className="mb-2"),
            html.P("Done by Joshua Walters, Also known as iamkyrin",
                                                className="mb-2"),
            html.Hr()],
                style={"text-align": "center"}),

                        ],
                className="text-center"),
            ]),
    dbc.Row([
                dbc.Tabs(id='tabs', children=[
                    dbc.Tab(label="Overview", tab_id='tab-1'),
                    dbc.Tab(label="EDA analysis", tab_id='tab-2'),
                    dbc.Tab(label="Model Performance", tab_id ='tab-3'),
                    dbc.Tab(label="SHAP Explainability", tab_id ='tab-4'),
                    dbc.Tab(label="Live Predictor", tab_id ='tab-5')
                                            ]),
                html.Div(id="tab-content", style={'padding': '20px'})
            ])
], style={"font-family": "Inter, sans-serif", "overflow-x": "hidden", "max-width": "100%"})

@app.callback(
    Output("tab-content", "children"),
    Input("tabs", "active_tab")
)
def render_content(active_tab):
    if active_tab == "tab-1":
        return tab1()
    elif active_tab == "tab-2":
        return tab2()
    elif active_tab == "tab-3":
        return tab3()
    elif active_tab == "tab-4":
        return tab4()
    elif active_tab == "tab-5":
        return tab5()
    return None


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8050, debug=False)