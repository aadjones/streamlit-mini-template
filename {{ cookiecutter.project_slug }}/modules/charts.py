# modules/charts.py
from .constants import LABELS, COLORS   # COLORS is now used 100 % of the time

def _label(col: str) -> str:
    return LABELS.get(col.lower(), col.capitalize())

{% if cookiecutter.chart_lib == 'plotly' %}
import plotly.express as px

def line_chart(df, column: str, color: str | None = None):
    color = COLORS.get(column.lower(), color or "#4682B4")  # auto-lookup
    fig = px.line(
        df,
        x=df.columns[0],
        y=column,
        markers=True,
        color_discrete_sequence=[color],
    )
    fig.update_layout(yaxis_title=_label(column))
    return fig

{% elif cookiecutter.chart_lib == 'altair' %}
import altair as alt

def line_chart(df, column: str, color: str | None = None):
    color = COLORS.get(column.lower(), color or "#4682B4")
    return (
        alt.Chart(df)
        .mark_line(color=color)
        .encode(
            x=df.columns[0] + ":T",
            y=alt.Y(f"{column}:Q", title=_label(column)),
        )
    )
{% endif %}
