from modules import charts
import pandas as pd

df = pd.DataFrame(
    {"date": ["2024-01-01", "2024-01-02"], "anxiety": [4, 5]}
)

def test_line_chart():
    fig = charts.line_chart(df, "anxiety", "#000")
{% if cookiecutter.chart_lib == 'plotly' %}
    # Plotly figure: extract y data
    assert fig.data[0].y.tolist() == [4, 5]
{% elif cookiecutter.chart_lib == 'altair' %}
    # Altair chart: check encoded y channel shorthand
    assert fig.encoding.y.shorthand == "anxiety:Q"
{% endif %}
