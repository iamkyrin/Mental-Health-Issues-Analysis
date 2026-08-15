from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc
from charts import *

results = pd.DataFrame({
    'Model': ['Logistic Regression', 'Random Forest', 'XGBoost', 'LightGBM'],
    'Accuracy': [0.69, 0.75, 0.77, 0.79],
    'Recall': [0.73, 0.78, 0.80, 0.84],
    'F1': [0.70, 0.75, 0.77, 0.80]
})

def tab3():
    return html.Div([
        dbc.Row([
            dbc.Col([
                html.H2("Model Performance Comparison", className="mt-3 mb-3", style={"color": "#111111", "font-weight": "bold"}),
                dbc.Col([
                    dcc.Graph(figure=model_perf()),
                    html.P("For each model, we evaluate four key performance metrics, which are recall,"
                           " precision, F1 and accuracy. Each one tells us a different piece of insight on"
                           " how well the model is performing."
                           " Precision tells us that the model flagged all those likely to receive treatment and"
                           " how much actually sought treatment."
                           " Recall tells us exactly how many of the actual treatment seekers the model has caught."
                           " F1 is a combination of precision and recall, giving us a single score for both false positives"
                           " and false negatives."
                           " Accuracy gives us the entire picture and the correct predictions across all domains.",
                           style={"color": "#333333", "font-size": "16px", "line-height": "1.6"}),
                    dash_table.DataTable(
                            id='basic-table',
                            columns=[{"name": i, "id": i} for i in results.columns],
                            data=results.to_dict('records'),
                            style_table={'overflowX': 'auto', 'borderRadius': '8px',
                                         'boxShadow': '0 4px 6px rgba(0,0,0,0.1)'},
                            style_cell={
                                'fontFamily': 'Segoe UI, Arial, sans-serif',
                                'fontSize': '14px',
                                'padding': '12px 15px',
                                'textAlign': 'left',
                                'border': '1px solid #EAEAEA'
                            },


                            style_header={
                                'backgroundColor': '#1E293B',
                                'color': '#FFFFFF',
                                'fontWeight': 'bold',
                                'textTransform': 'uppercase',
                                'fontSize': '12px',
                                'letterSpacing': '0.5px'
                            },
                    ),
                    html.P("LightGBM model performs the best with an accuracy of 79%. It also has the best recall"
                           " which fits for predicting those who have sought treatment. Therefore recall is my priority"
                           " metric for comparing the 4 models."),
                ], width=12),
        ])
    ], style={"font-family": "Inter, sans-serif", "overflow-x": "hidden", "max-width": "100%"})
    ])