import duckdb as ddb
import pandas as pd
import requests as rq

# Create persistent DuckDB database
conn = ddb.connect("movies_data.db")
# Fetch data from API
# Ingest data directly into a DuckDB SQL Table
# Query data using standard SQL
conn.close()


