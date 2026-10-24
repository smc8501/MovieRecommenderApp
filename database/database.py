import duckdb as ddb
import pandas as pd
import requests as rq
import os
import glob

# Create persistent DuckDB database
# Fetch data from API
# Ingest data directly into a DuckDB SQL Table
# Query data using standard SQL


def main():
    
    with ddb.connect("movies_data.db") as conn:
        conn.execute("CREATE OR REPLACE TABLE movie_data AS SELECT unnest(results) AS movie FROM read_json_auto('data/raw/*.json');")
        count = conn.execute("SELECT COUNT(movie) FROM movie_data;").fetchall()
        print("Count:", count)
   

        conn.execute("COPY movie_data TO 'movies_output.csv' (HEADER, DELIMITER ',');")

        print("CSV export complete")
if __name__ == "__main__":
    main()