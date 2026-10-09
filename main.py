import duckdb as ddb
import pandas as pd
import requests as rq
import streamlit as st

st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)
st.title('Movie Recommender App')
st.write('Choose your favorite movie')


# Create persistent DuckDB database
conn = ddb.connect("movies_data.db")
# Fetch data from API
# Ingest data directly into a DuckDB SQL Table
# Query data using standard SQL
conn.close()


