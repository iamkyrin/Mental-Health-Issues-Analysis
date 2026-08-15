from dash import dcc, html
import dash_bootstrap_components as dbc
from charts import *

def tab1():
    return html.Div([
        dbc.Row([
            dbc.Col([
                html.H2("Project Overview", className="mt-3 mb-3", style={"color": "#111111", "font-weight": "bold"}),
                html.P("A mental health analysis in a survey with a dataset that has 1259 rows and 25 columns."
                       " The survey covers personal questions that help to determine whether or not a worker"
                       " has sought treatment based on their mental health struggles. Covering things such as "
                       "family history of mental health struggles, mental health affecting their work"
                       " and much more columns.",
                       style={"color": "#333333", "font-size": "16px", "line-height": "1.6"}),
                html.P(
                    "I have built a LightGBM classification model that can predict whether a worker has sought treatment with an accuracy of 79%+."
                    " I have found that the most determining factors was work interference and the family history column, which made up a large part"
                    " of the prediction model's training set. An interesting finding was that previously, in a correlation matrix, work interference"
                    " was set out not to be one of the models most predictive factor. During analysis, I mapped work interference"
                    " into numbers so that the model can work well with the column. After that, work interference became one of the best predictors"
                    " for the model."
                    , style={"color": "#333333", "font-size": "16px", "line-height": "1.6"}),
                html.H2("Charts", className="mt-3 mb-3", style={"color": "#111111", "font-weight": "bold"}),
                html.P("Treatment Distribution of bar chart (Yes or No)",
                       style={"color": "#333333", "font-size": "16px", "line-height": "1.6"}),
                html.P("Top 5 countries bar chart",
                       style={"color": "#333333", "font-size": "16px", "line-height": "1.6"}),
                html.P("Gender Distribution of the survey bar chart",
                       style={"color": "#333333", "font-size": "16px", "line-height": "1.6"}),
                html.P("More charts well be shown in the EDA analysis and SHAP explainability. These charts"
                       " are an overview that showcase the demographic of the entire dataset.",
                       style={"color": "#333333", "font-size": "16px", "line-height": "1.6"}),

            ], width=8),
            dbc.Col([
                dbc.Card(dbc.CardBody([html.H2("1,259"), html.P("Survey Respondents")])),
                dbc.Card(dbc.CardBody([html.H2("25"), html.P("Columns")]), className="mt-2"),
                dbc.Card(dbc.CardBody([html.H2("79%"), html.P("Model Accuracy")]), className="mt-2"),
                dbc.Card(dbc.CardBody([html.H2("4"), html.P("Models Compared")]), className="mt-2"),
            ], width=4),
            dbc.Col([
                dcc.Graph(figure=treatmentChart()),
                dcc.Graph(figure=genderChart()),
                dcc.Graph(figure=countryChart()),
                dcc.Graph(figure=ageChart())
            ], width=12)
        ])
    ], style={"font-family": "Inter, sans-serif", "overflow-x": "hidden", "max-width": "100%"})