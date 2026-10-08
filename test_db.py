import pytest
import duckdb as ddb
import os

DB_FILE = "movies_data.db"

@pytest.fixture
def test_database_file_exists():
    """Confirms that the persistant database file actually exists on the local file system."""
    assert os.path.exists(DB_FILE), f"Database file '{DB_FILE}' could not be located"
