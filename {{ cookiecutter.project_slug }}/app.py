import pathlib
import streamlit as st
import pandas as pd
from modules import charts, palette

DATA_PATH = pathlib.Path("{{ cookiecutter.data_path }}")

st.set_page_config(page_title="{{ cookiecutter.project_name }}", page_icon="🧃", layout="wide")

@st.cache_data(ttl=0)  # Set TTL to 0 to avoid stale data
def load_data(path: pathlib.Path):
    if path.exists():
        return pd.read_csv(path)
    st.warning("Demo data not found - using empty frame")
    return pd.DataFrame()

df = load_data(DATA_PATH)

st.title("{{ cookiecutter.project_name }} 📊")
st.markdown("{{ cookiecutter.description }}")

if df.empty:
    st.stop()

with st.sidebar:
    metric_choice = st.selectbox("Metric", df.columns[1:])

chart = charts.line_chart(df, metric_choice, color=palette.main())
st.plotly_chart(chart, use_container_width=True)