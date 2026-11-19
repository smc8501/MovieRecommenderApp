
import duckdb as ddb
import os
import pytest
from database import build_database

DB_FILE = "e:/MovieRecommenderApp/database/moviesDB.duckdb"

@pytest.fixture
def db_conn():
    with ddb.connect(DB_FILE, read_only=True) as conn:
        yield conn

def test_database_file_exists():
    """Confirms that the persistant database file actually exists on the local file system."""
    assert os.path.exists(DB_FILE), f"Database file '{DB_FILE}' could not be located"

def test_no_missing_values(db_conn):
    """Fail if any in the movies table contains NULL values."""
    null_columns = db_conn.sql(
        """
        SELECT column_name, null_percentage
        FROM (SUMMARIZE movies)
        WHERE null_percentage > 0;
        """
        ).fetchall()
    assert len(null_columns) == 0, f"Found columns with NULL VALUES: {null_columns}"

def test_no_duplicate_ids(db_conn):
    """Fail if the primary key column 'id' has duplicate values."""
    duplicates = db_conn.sql(
        """
        SELECT id, COUNT(*) AS count
        FROM movies
        GROUP BY id
        HAVING COUNT(*) > 1;
        """
    ).fetchall()

    assert len(duplicates) == 0, f"Found duplicate IDs: {duplicates}"

    def test_no_exact_duplicate_rows(db_conn):
        """Fail if any two rows are 100% identical across all columns"""
        duplicate_rows = db_conn.sql(
            """
            SELECT *, COUNT(*) AS count
            FROM movies
            GROUP BY ALL
            HAVING COUNT(*) > 1;
            """
        ).fetchall()

        assert len(duplicate_rows) == 0, f"Found {len(duplicate_rows)} exact duplicate rows"

    def test_is_alread_built(db_conn):
        table_exists = db_conn.sql(
            """
            SELECT COUNT(*)
            FROM duckdb_tables()
            WHERE table_name = 'movies';

            """
        ).fetchone()

        if table_exists == False or table_exists[0] == 0:
            return False

        row_count = db_conn.sql(
            """
            SELECT COUNT(*) FROM movies;
            """
        ).fetchone()
        return bool(row_count and row_count[0] > 0)

