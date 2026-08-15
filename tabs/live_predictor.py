from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import pandas as pd
import joblib
import os


model_path = os.path.join(os.path.dirname(__file__), "my_model.joblib")
model = joblib.load(model_path)


def tab5():
    return html.Div([
        dbc.Row([
            dbc.Col([
                html.H2("Live predictor", className="mt-3 mb-3",
                        style={"color": "#111111", "font-weight": "bold"}),
                html.P("Test the model out for yourself! "
                       "This is a live predictor, once you input details, "
                       "the model will try to predict whether you are more likely to seek treatment or not.",
                       style={"color": "#333333", "font-size": "16px", "line-height": "1.6"}),
                html.H5("Age"),
                html.P("Valid ranges only from 18 - 65"),
                dcc.Input(id="age-input", placeholder="Input details", type="number"),

                html.H5("Work Interference"),
                html.P("How often does your mental health interfere with your work?"),
                dcc.Dropdown(
                    options=[
                        {"label": "Often", "value": "Often"},
                        {"label": "Sometimes", "value": "Sometimes"},
                        {"label": "Rarely", "value": "Rarely"},
                        {"label": "Never", "value": "Never"},
                    ],
                    id="work_interference",
                    multi=False,
                ),

                html.H5("Family History"),
                html.P("Has your family ever had issues with mental health?"),
                dcc.Dropdown(
                    options=[
                        {"label": "Yes", "value": "Yes"},
                        {"label": "No", "value": "No"},
                    ],
                    id="family_history",
                    multi=False,
                ),

                html.H5("Care Options"),
                html.P(
                    "Does the company you are employed at have any care option packages that helps individuals with mental health?"),
                dcc.Dropdown(
                    options=[
                        {"label": "Yes", "value": "Yes"},
                        {"label": "No", "value": "No"},
                        {"label": "Not Sure", "value": "Not Sure"},
                    ],
                    id="care_options",
                    multi=False,
                ),

                html.H5("Benefits"),
                html.P("Does the company you are employed at provide any benefits?"),
                dcc.Dropdown(
                    options=[
                        {"label": "Yes", "value": "Yes"},
                        {"label": "No", "value": "No"},
                        {"label": "Don't know", "value": "Dont know"},
                    ],
                    id="benefits",
                    multi=False,
                ),

                html.H5("Gender"),
                dcc.Dropdown(
                    options=[
                        {"label": "Male", "value": "Male"},
                        {"label": "Female", "value": "Female"},
                        {"label": "Other", "value": "Other"},
                    ],
                    id="gender",
                    multi=False,
                ),

                html.Button(
                    'Submit',
                    id='custom-btn',
                    n_clicks=0,
                    style={
                        'backgroundColor': '#1E88E5',
                        'color': 'white',
                        'border': 'none',
                        'borderRadius': '8px',
                        'padding': '10px 20px',
                        'fontSize': '16px',
                        'cursor': 'pointer',
                        'fontWeight': 'bold',
                        'boxShadow': '0px 4px 6px rgba(0,0,0,0.1)',
                        'transition': '0.3s'
                    }
                ),

                html.Div("Prediction output: ", id="prediction_output")

            ], width=8)
        ])
    ], style={"font-family": "Inter, sans-serif", "overflow-x": "hidden", "max-width": "100%"})


def register_callbacks(app):
    @app.callback(
        Output("prediction_output", "children"),
        Input("custom-btn", "n_clicks"),
        State("age-input", "value"),
        State("work_interference", "value"),
        State("family_history", "value"),
        State("care_options", "value"),
        State("benefits", "value"),
        State("gender", "value"),
        prevent_initial_call=True
    )
    def predict(n_clicks, age, work_interference, family_history, care_options, benefits, gender):
        print(f"Button clicked: {n_clicks}")
        print(
            f"Values: age={age}, work={work_interference}, family={family_history}, care={care_options}, benefits={benefits}, gender={gender}")

        if None in [age, work_interference, family_history, care_options, benefits, gender]:
            return html.P("Please fill in all fields before submitting.",
                          style={"color": "orange", "font-weight": "bold"})

        try:
            work_int_map = {"Never": 0, "Rarely": 1, "Sometimes": 2, "Often": 3}

            input_data = {
                "Age": [age],
                "work_interfere": [work_int_map[work_interference]],
                "family_history_No": [family_history == "No"],
                "family_history_Yes": [family_history == "Yes"],
                "care_options_No": [care_options == "No"],
                "care_options_Not_sure": [care_options == "Not Sure"],
                "care_options_Yes": [care_options == "Yes"],
                "benefits_Don_t_know": [benefits == "Dont know"],
                "benefits_No": [benefits == "No"],
                "benefits_Yes": [benefits == "Yes"],
                "Gender_Other": [gender == "Other"],
                "Gender_female": [gender == "Female"],
                "Gender_male": [gender == "Male"],
            }

            df_input = pd.DataFrame(input_data)
            print(f"Input DataFrame: {df_input}")

            prediction = model.predict(df_input)[0]
            print(f"Prediction: {prediction}")

            if prediction == 1:
                return html.P("This person is likely to seek treatment.",
                              style={"color": "green", "font-size": "18px", "font-weight": "bold"})
            else:
                return html.P("This person is unlikely to seek treatment.",
                              style={"color": "red", "font-size": "18px", "font-weight": "bold"})
        except Exception as e:
            print(f"Error: {e}")
            return html.P(f"Error making prediction: {str(e)}",
                          style={"color": "red"})