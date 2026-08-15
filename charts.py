from data import df
from data import df2
import plotly.express as px
import pandas as pd
import plotly.figure_factory as ff

def treatmentChart():
    treat = df2['treatment'].value_counts()
    fig = px.bar(x=treat.index,
                 y=treat.values,
                 title='How many receive treatment',
                 text_auto=True,
                 color=treat.index,
                 color_discrete_sequence=px.colors.qualitative.Prism
                 )
    fig.update_layout(
        title_font_size=24,
        title_x=0.5,
        plot_bgcolor="rgba(240, 240, 240, 1)",
        paper_bgcolor="white",
        bargap=0.5
    )
    fig.update_yaxes(
        title_text="Count of treatment",
        title_font_size=16,
        tickfont_size=12,
        showgrid=False
    )
    fig.update_xaxes(
        title_text="Received Treatment",
        title_font_size=16,
        tickfont_size=12,
        showgrid=False
    )

    return fig
def genderChart():
    gender = df2['Gender'].value_counts()
    fig = px.bar(x=gender.index,
                 y=gender.values,
                 title='Gender Distribution',
                 text_auto=True, color=gender.index,
                 color_discrete_sequence=px.colors.qualitative.Prism
                 )
    fig.update_layout(
        title_font_size=24,
        title_x=0.5,
        plot_bgcolor="rgba(240, 240, 240, 1)",
        paper_bgcolor="white",
        bargap=0.5
    )
    fig.update_yaxes(
        title_text="Count of Gender",
        title_font_size=16,
        tickfont_size=12,
        showgrid=False
    )
    fig.update_xaxes(
        title_text="Gender",
        title_font_size=16,
        tickfont_size=12,
        showgrid=False
    )

    return fig
def countryChart():
    country = df2['Country'].value_counts()
    country_top5 = country.head(5)
    fig = px.bar(x=country_top5.index,
                 y=country_top5.values,
                 title='Top 5 Country Distribution',
                 text_auto=True, color=country_top5.index,
                 color_discrete_sequence=px.colors.qualitative.Prism
                 )
    fig.update_layout(
        title_font_size=24,
        title_x=0.5,
        plot_bgcolor="rgba(240, 240, 240, 1)",
        paper_bgcolor="white",
        bargap=0.5
    )
    fig.update_yaxes(
        title_text="Count of Countries",
        title_font_size=16,
        tickfont_size=12,
        showgrid=False
    )
    fig.update_xaxes(
        title_text="Countries",
        title_font_size=16,
        tickfont_size=12,
        showgrid=False
    )

    return fig
def ageChart():
    country = df2['Age'].value_counts()
    fig = px.histogram(
        df2,
        x="Age",
        nbins=15,
        barmode="overlay",
        opacity=0.75,
        text_auto=True,
        title="Age distribution"
    )
    fig.update_layout(
        title_font_size=24,
        title_x=0.5,
        plot_bgcolor="rgba(240, 240, 240, 1)",
        paper_bgcolor="white",
        bargap=0.5
    )
    fig.update_yaxes(
        title_text="Count of Ages",
        title_font_size=16,
        tickfont_size=12,
        showgrid=False
    )
    fig.update_xaxes(
        title_text="Ages",
        title_font_size=16,
        tickfont_size=12,
        showgrid=False
    )

    return fig
def treatmentvsgenderChart():
    fig = px.histogram(
        df2,
        x="treatment",
        color='Gender',
        nbins=15,
        barmode="group",
        opacity=0.75,
        text_auto=True,
        title="Treatment Vs Gender"
    )
    fig.update_layout(
        title_font_size=24,
        title_x=0.5,
        plot_bgcolor="rgba(240, 240, 240, 1)",
        paper_bgcolor="white",
        bargap=0.5
    )
    fig.update_yaxes(
        title_text="Count",
        title_font_size=16,
        tickfont_size=12,
        showgrid=False
    )
    fig.update_xaxes(
        title_text="Treatment",
        title_font_size=16,
        tickfont_size=12,
        showgrid=False
    )

    return fig
def treatmentvsfamilyhistory():
    fig = px.histogram(
        df2,
        x="treatment",
        color='family_history',
        nbins=15,
        barmode="group",
        opacity=0.75,
        text_auto=True,
        title="Treatment Vs Family history"
    )
    fig.update_layout(
        title_font_size=24,
        title_x=0.5,
        plot_bgcolor="rgba(240, 240, 240, 1)",
        paper_bgcolor="white",
        bargap=0.5
    )
    fig.update_yaxes(
        title_text="Count",
        title_font_size=16,
        tickfont_size=12,
        showgrid=False
    )
    fig.update_xaxes(
        title_text="Treatment",
        title_font_size=16,
        tickfont_size=12,
        showgrid=False
    )

    return fig
def treatmentvsworkinterfere():
    fig = px.histogram(
        df2,
        x="treatment",
        color='work_interfere',
        nbins=15,
        barmode="group",
        opacity=0.75,
        text_auto=True,
        title="Treatment Vs Work interference"
    )
    fig.update_layout(
        title_font_size=24,
        title_x=0.5,
        plot_bgcolor="rgba(240, 240, 240, 1)",
        paper_bgcolor="white",
        bargap=0.5
    )
    fig.update_yaxes(
        title_text="Count",
        title_font_size=16,
        tickfont_size=12,
        showgrid=False
    )
    fig.update_xaxes(
        title_text="Treatment",
        title_font_size=16,
        tickfont_size=12,
        showgrid=False
    )

    return fig
def treatmentvseekhelp():
    fig = px.histogram(
        df2,
        x="treatment",
        color='seek_help',
        nbins=15,
        barmode="group",
        opacity=0.75,
        text_auto=True,
        title="Treatment Vs Seek Help"
    )
    fig.update_layout(
        title_font_size=24,
        title_x=0.5,
        plot_bgcolor="rgba(240, 240, 240, 1)",
        paper_bgcolor="white",
        bargap=0.5
    )
    fig.update_yaxes(
        title_text="Count",
        title_font_size=16,
        tickfont_size=12,
        showgrid=False
    )
    fig.update_xaxes(
        title_text="Treatment",
        title_font_size=16,
        tickfont_size=12,
        showgrid=False
    )

    return fig
def treatmentvsremotework():
    fig = px.histogram(
        df2,
        x="treatment",
        color='remote_work',
        nbins=15,
        barmode="group",
        opacity=0.75,
        text_auto=True,
        title="Treatment Vs Remote_Work"
    )
    fig.update_layout(
        title_font_size=24,
        title_x=0.5,
        plot_bgcolor="rgba(240, 240, 240, 1)",
        paper_bgcolor="white",
        bargap=0.5
    )
    fig.update_yaxes(
        title_text="Count",
        title_font_size=16,
        tickfont_size=12,
        showgrid=False
    )
    fig.update_xaxes(
        title_text="Treatment",
        title_font_size=16,
        tickfont_size=12,
        showgrid=False
    )

    return fig
def treatmentvswellnessprogram():
    fig = px.histogram(
        df2,
        x="treatment",
        color='wellness_program',
        nbins=15,
        barmode="group",
        opacity=0.75,
        text_auto=True,
        title="Treatment Vs Wellness Program"
    )
    fig.update_layout(
        title_font_size=24,
        title_x=0.5,
        plot_bgcolor="rgba(240, 240, 240, 1)",
        paper_bgcolor="white",
        bargap=0.5
    )
    fig.update_yaxes(
        title_text="Count",
        title_font_size=16,
        tickfont_size=12,
        showgrid=False
    )
    fig.update_xaxes(
        title_text="Treatment",
        title_font_size=16,
        tickfont_size=12,
        showgrid=False
    )

    return fig
def treatmentvsnumberemployees():
    fig = px.histogram(
        df2,
        x="treatment",
        color='no_employees',
        nbins=15,
        barmode="group",
        opacity=0.75,
        text_auto=True,
        title="Treatment Vs Number Of employees"
    )
    fig.update_layout(
        title_font_size=24,
        title_x=0.5,
        plot_bgcolor="rgba(240, 240, 240, 1)",
        paper_bgcolor="white",
        bargap=0.5
    )
    fig.update_yaxes(
        title_text="Count",
        title_font_size=16,
        tickfont_size=12,
        showgrid=False
    )
    fig.update_xaxes(
        title_text="Treatment",
        title_font_size=16,
        tickfont_size=12,
        showgrid=False
    )

    return fig
def treatmentvsage():
    fig = px.box(
        df2,
        x="treatment",
        y='Age',
        title="Treatment Vs Age"
    )
    fig.update_layout(
        title_font_size=24,
        title_x=0.5,
        plot_bgcolor="rgba(240, 240, 240, 1)",
        paper_bgcolor="white",
        bargap=0.5
    )
    fig.update_yaxes(
        title_text="Age",
        title_font_size=16,
        tickfont_size=12,
        showgrid=False
    )
    fig.update_xaxes(
        title_text="Treatment",
        title_font_size=16,
        tickfont_size=12,
        showgrid=False
    )

    return fig
def treatmentcorr():
    df_encoded = df2.copy()
    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()
    cat_cols = df_encoded.select_dtypes(include='str').columns
    for col in cat_cols:
        df_encoded[col] = le.fit_transform(df_encoded[col].astype(str))

    corr = df_encoded.corr().round(2)

    fig = ff.create_annotated_heatmap(
        z=corr.values,
        x=list(corr.columns),
        y=list(corr.index),
        colorscale='RdBu',
        showscale=True,
        reversescale=True
    )
    fig.update_layout(
        title="Correlation Matrix",
        title_x=0.5,
        title_font_size=24,
        height=700,
        paper_bgcolor="white"
    )
    return fig


def model_perf():
    results = pd.DataFrame({
        'Model': ['Logistic Regression', 'Random Forest', 'XGBoost', 'LightGBM'],
        'Accuracy': [0.69, 0.75, 0.77, 0.79],
        'Recall': [0.73, 0.78, 0.80, 0.84],
        'F1': [0.70, 0.75, 0.77, 0.80]
    })
    fig = px.bar(results, x="Model", y="Recall", color="Accuracy", barmode="group") 
    return fig