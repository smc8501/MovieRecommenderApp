"""Database operations and local file management using DuckDB.

These modules resolves filesystem paths and executes analytical SQL queries
against local DuckDB databases.
"""
import pathlib
import duckdb as ddb


# Create persistent DuckDB database
# Fetch data from API
# Ingest data directly into a DuckDB SQL Table
# Query data using standard SQL

def load_raw_movies(conn, raw_data_path):
    """Pulls raw movie data from the /popular endpoint of TMDB API"""
    safe_path = raw_data_path.as_posix().replace("'", "''")
    conn.execute(
        f"""
        CREATE OR REPLACE TABLE movies_raw AS
        SELECT unnest(results, max_depth := 2) AS movie
        FROM read_json_auto('{safe_path}');
        """
    )

def remove_duplicates(conn):
    """Remove duplicate movie records and rows without an ID."""
    conn.execute(
        """
        CREATE OR REPLACE TABLE movies_deduped AS
        SELECT *
        FROM movies_raw
        WHERE id IS NOT NULL
        QUALIFY ROW_NUMBER() OVER (PARTITION BY id ORDER BY id) = 1;
        """
    )
def replace_nulls_with_strings(conn):
    """This is a function to replace nulls with strings"""
    conn.execute(
            """
            CREATE OR REPLACE TABLE movies AS
            SELECT
                CASE 
                    WHEN typeof(COLUMNS(*)) = 'VARCHAR' THEN COALESCE(COLUMNS(*), '')
                    ELSE COLUMNS(*)
                END
            FROM movies_deduped;
            """
        )
def finalise_schema(conn):
    """Drop staging tables, add the primary key, and return the final row count."""
    conn.execute("DROP TABLE IF EXISTS movies_raw;")
    conn.execute("DROP TABLE IF EXISTS movies_deduped;")
    conn.execute("ALTER TABLE movies ADD CONSTRAINT movie_id_pk PRIMARY KEY (id)")

    result = conn.sql("SELECT COUNT(*) FROM movies;").fetchone()

    return result[0] if result else 0



def build_database(raw_data_path, db_path, force):
    """This is a function that create a database and transforms tables for: movies."""

    if db_path.exists() and force is False:
        print(f"Database already exists at {db_path}. Skipping build.")

        with ddb.connect(str(db_path)) as conn:
            result = conn.sql(
            """
            SELECT COUNT(*) FROM movies;
            """
            ).fetchone()
            return result[0] if result else 0
    else:
        db_path.parent.mkdir(parents=True, exist_ok=True)

        with ddb.connect(str(db_path)) as conn:
            load_raw_movies(conn, raw_data_path)
            remove_duplicates(conn)
            replace_nulls_with_strings(conn)
            clean_row_count = finalise_schema(conn)

        print(f"Database built successfully at {db_path} ({clean_row_count} clean rows).")
        return clean_row_count

def main():
    """This is the main function that runs all the functions."""
    # db_path = pathlib.Path("e:/MovieRecommenderApp/database/moviesDB.duckdb")
    base_dir = pathlib.Path("e:/MovieRecommenderApp")
    raw_file = base_dir / "data" / "raw" / "*.json"
    db_file = base_dir / "database" / "moviesDB.duckdb"

    total_rows = build_database(raw_file, db_file, False)

    print(total_rows)
        # # Create Genre table
        # conn.execute("CREATE OR REPLACE TABLE genre AS SELECT unnest(genres, recursive := true) AS genre FROM read_json_auto('data/raw/genre_list.json');")
        # # Update Genre table
        # # Create Movie_Genre Table (Junction Table) to resolve the Many-to-Many
        # conn.execute("CREATE OR REPLACE TABLE movie_genre AS SELECT m.title, g.name AS genre_name FROM movie m INNER JOIN genre g ON m.genre_id = g.id ORDER BY;")
        # conn.sql("SELECT DISTINCT COUNT(movie_id) FROM movie_genre;").show()
        # conn.execute("COPY movie TO 'movies_output-1.csv' (HEADER, DELIMITER ',');")
        # conn.execute("COPY movie_data TO 'movies_output.csv' (HEADER, DELIMITER ',');")


        # print("CSV export complete")

if __name__ == "__main__":
    main()
