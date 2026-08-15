from dash import dcc, html
import dash_bootstrap_components as dbc


def tab4():
    return html.Div([
        dbc.Row([
            dbc.Col([
                html.H2("SHAP Explainability", className="mt-3 mb-3", style={"color": "#111111", "font-weight": "bold"}),
                dbc.Col([
                    html.P("SHAP is a tool that helps us understand why our model makes"
                           " specific predictions. Instead of treating the model as a black box, SHAP"
                           " breaks down each prediction to show us which features had the biggest"
                           " influence on its outcome. It also explains which feature pushed the prediction"
                           " up or down. In short, SHAP explains the models reasoning.",
                           style={"color": "#333333", "font-size": "16px", "line-height": "1.6"}),
                ], width=10),

                html.H2("Global Feature Importance", className="mt-3 mb-3",
                        style={"color": "#111111", "font-weight": "bold"}),
                dbc.Col([
                    html.Img(src='assets/shap_summary.png', style={'width': '100%'}),
                    html.P("Work interfere matters the most when the model is making"
                           " predictions, this contradicts the finding in the correlation"
                           " matrix heatmap. In my EDA finding, this confirms that work"
                           " interfere is the most important column when the model is making"
                           " predictions.",
                           style={"color": "#333333", "font-size": "16px", "line-height": "1.6", "margin-top": "10px"}),
                    html.P(""),
                ], width=10),

                html.H2("Individual Prediction Explanation", className="mt-3 mb-3",
                        style={"color": "#111111", "font-weight": "bold"}),
                dbc.Col([
                    html.Img(src='assets/shap_waterfall.png', style={'width': '100%'}),
                    html.P("This confirms that work interfere is one of the best"
                           " features that the models uses to predict, tested on a person in the dataset."
                           " It considers all features, bringing the confidence level up or down. For this specific person,"
                           " the model only decreased it's confidence based on the companies care options."
                           " The model can, however, decrease its confidence levels based on any feature it was trained on."
                           " As for this person, the model correctly predicted that this person has sought treatment.",
                           style={"color": "#333333", "font-size": "16px", "line-height": "1.6", "margin-top": "10px"}),
                ], width=10),


                html.H2("Key Takeaways", className="mt-3 mb-3",
                        style={"color": "#111111", "font-weight": "bold"}),
                dbc.Col([
                    html.P("The reasoning of the model makes complete sense. It aligns with"
                           " EDA findings and it connects to real world issues. Features such as work interference and"
                           " family history correlate well with psychology research on mental health. Companies that offer"
                           " mental health support options (care option) for employees that struggle with their mental health"
                           " make the person more likely to seek treatment and realize when they are struggling.",
                           style={"color": "#333333", "font-size": "16px", "line-height": "1.6", "margin-top": "10px"}),
                ], width=10)
                    ])

    ], style={"font-family": "Inter, sans-serif", "overflow-x": "hidden", "max-width": "100%"})
        ])