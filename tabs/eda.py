from dash import dcc, html
import dash_bootstrap_components as dbc
from charts import *

def tab2():
    return html.Div([
        dbc.Row([
            dbc.Col([
                html.H2("Target Variable Analysis", className="mt-3 mb-3", style={"color": "#111111", "font-weight": "bold"}),
                dbc.Col([
                    dcc.Graph(figure=treatmentvsgenderChart()),
                    html.P("Males take up the most in the dataset, with females being the least and other taking up the second highest."
                           " With that knowledge, females seem to seek treatment much more than males."
                           " The findings are interesting, it is counterintuitive that the smallest group has the highest treatment rates. I expected"
                           " males to take up a much larger portion, since they take up the most in the dataset.",
                           style={"color": "#333333", "font-size": "16px", "line-height": "1.6"}),
                    dcc.Graph(figure=treatmentvsfamilyhistory()),
                    html.P(
                        "People that have a family history of mental health struggles are much more willing to go for treatment"
                        " than those that don't have a family history of mental health struggles."
                        " With family history of mental health issues, 74% have seeked treatment, while those without"
                        " family history sought treatment 35% of the time."
                        , style={"color": "#333333", "font-size": "16px", "line-height": "1.6"}),
                    dcc.Graph(figure=treatmentvsworkinterfere()),
                    html.P(
                        "Those that agree work interference is 'often' affecting their"
                        " mental health, have seeked out treatment. Those that are unsure or have not clearly stated"
                        " if work interference was a indicator for their mental health, have not."
                        " A strong 85% seeked treatment when answered 'often' that work was affecting their mental health."
                        " Those unsure or have not clearly stated have seeked treatment 2% of the time."
                        , style={"color": "#333333", "font-size": "16px", "line-height": "1.6"}),
                    dcc.Graph(figure=treatmentvseekhelp()),
                    html.P(
                        "Those that seek help with their mental health issues go for treatment 59% of the time."
                        " While those that don't seek help have sought treatment 50% of the time."
                        " Those unsure whether they should seek help only have sought treatment 46% of the time."
                        " Those more inclined to seek help have sought out treatment much more than those unsure."
                        , style={"color": "#333333", "font-size": "16px", "line-height": "1.6"}),

                    dcc.Graph(figure=treatmentvsremotework()),
                    html.P(
                        "People that do remote work are much more likely to seek out treatment."
                        " As shown, people that do remote work have sought treatment 53% of the time."
                        " Those that don't have remote work only seek treatment 50% of the time."
                        , style={"color": "#333333", "font-size": "16px", "line-height": "1.6"}),
                    dcc.Graph(figure=treatmentvswellnessprogram()),
                    html.P(
                        "Companies that have wellness programs actually help those seek treatment much more."
                        " The 'no' column showcase companies that don't have wellness programs. 'Yes' column shows"
                        " the companies that do have wellness programs and the 'Don't Know' column shows that the"
                        " survey takers wasn't sure if their company had wellness programs."
                        " The companies that didn't have wellness programs, had survey takers 49% of the time more likely to seek treatment,"
                        " while those unsure if the company had wellness programs sought treatment 43% of the time."
                        " Companies that did have wellness programs however, had survey takers seeking treatment 59% of the time."
                        " Showcasing that companies who have wellness programs, helped employees seeked treatment much more than those who"
                        " didn't have wellness programs."
                        , style={"color": "#333333", "font-size": "16px", "line-height": "1.6"}),

                    dcc.Graph(figure=treatmentvsnumberemployees()),
                    html.P(
                        "A bar chart of those that seeked treatment based on the company size."
                        " There is no trend, meaning that company size does not directly affect whether or not"
                        " those would seek treatment."
                        , style={"color": "#333333", "font-size": "16px", "line-height": "1.6"}),

                    dcc.Graph(figure=treatmentvsage()),
                    html.P(
                        "A boxplot that showcases the difference in age that have seeked treatment."
                        " The median age of those who sought treatment are 32 and those who did not are 31,almost identical,"
                        " which suggests that age has very little influence on whether"
                        " a worker seeks treatment or not."
                        , style={"color": "#333333", "font-size": "16px", "line-height": "1.6"}),

                ], width=12),

                html.H2("Correlation Analysis", className="mt-3 mb-3", style={"color": "#111111", "font-weight": "bold"}),
                dcc.Graph(figure=treatmentcorr()),
                html.P(
                    "Originally, this correlation matrix showed that work interference is not a good"
                    " predictor for the model in helping predict whether or not someone sought treatment."
                    " However, when mapping the work interference column into ordinal numbers,"
                    " I have found out that work interference was"
                    " the column that the model would use the most when trying to predict if a person has"
                    " sought treatment."
                    " Other columns the matrix showed as strong indicators that turned out to be strong predictors were,"
                    " family history,care options and benefits."
                    , style={"color": "#333333", "font-size": "16px", "line-height": "1.6"}),
            ]),

        ])
    ], style={"font-family": "Inter, sans-serif", "overflow-x": "hidden", "max-width": "100%"})