# MovieRecommenderApp

A Python-based project focused on collecting, validating, and storing movie data from The Movie Database (TMDB) API. The repository demonstrates how to fetch popular movies, validate the JSON payloads, and prepare the dataset for storage in a local DuckDB database.

## Project Overview

This project is a simple data pipeline for a movie recommendation dataset. It pulls movie information from TMDB, saves raw JSON files locally, validates them to ensure consistent structure, and provides a foundation for SQL-based querying and future recommendation logic.

The repository is designed to help learn the full lifecycle of working with data:

- pulling data from an external API
- storing raw records safely
- validating schema and content
- organizing data for database ingestion
- creating a reusable data layer for analysis

## Repository Structure

```text
MovieRecommenderApp/
├── data/
│   └── raw/
│       ├── popular_movies-1.json
│       ├── popular_movies-2.json
│       ├── popular_movies-3.json
│       ├── popular_movies-4.json
│       └── popular_movies-5.json
├── ingestion/
│   └── ingest_movies.py
├── .gitignore
├── database.py
├── movies_data.db
├── package.json
├── test_db.py
└── README.md
```

## What the Project Does

### 1. Fetches movie data from TMDB
The ingestion script calls TMDB's popular movies endpoint and downloads several pages of movie results.

### 2. Saves raw JSON files
Each response is stored in the `data/raw` folder, making it easy to inspect, debug, and re-use the fetched data.

### 3. Validates the JSON schema
The project uses `jsonschema` to confirm that the API response matches a defined structure, including required fields and expected value types.

### 4. Stores data in a database
The project includes a DuckDB database setup (`movies_data.db`) to prepare for structured analytics and SQL-based queries.

### 5. Tests database existence
A lightweight pytest test checks that the database file is present and accessible, reinforcing good validation practices.

## Core Files

### `ingestion/ingest_movies.py`
This is the main data collection script. It:

- loads environment variables from `.env`
- builds the TMDB API request
- fetches popular movies by page
- writes data to JSON files
- validates each result with a JSON schema
- catches API and validation errors gracefully

### `database.py`
This file is intended to connect to the local DuckDB database and manage the data layer. It shows the foundations of data persistence and SQL database interaction using Python.

### `test_db.py`
This file contains a simple pytest test confirming the database exists. It introduces testing as part of a data engineering workflow.

### `data/raw/*.json`
These files are the raw movie datasets downloaded from TMDB. They act as a local staged dataset for analysis, experimentation, and later ingestion into a database.

## Technologies Used

- Python
- requests
- python-dotenv
- jsonschema
- DuckDB
- pandas
- pytest
- JSON data handling
- SQL fundamentals

## Skills Learnt

This project is a strong example of practical learning in data-focused software development. Some of the key skills gained include:

### API Integration
Working with external APIs teaches how to:

- send HTTP requests
- handle authentication tokens
- pass query parameters
- work with JSON responses
- manage errors and rate limits

### Environmental Configuration
The use of `.env` files and environment variables introduces secure configuration management. This helps avoid hardcoding sensitive keys such as TMDB tokens in source code.

### Data Validation
Using `jsonschema` helps understand how to enforce data quality rules, verify required fields, and detect malformed or inconsistent records before they are processed further.

### File Handling and Data Storage
The project teaches how to:

- read and write JSON files
- organize records by page or dataset
- create a reliable data collection workflow
- preserve raw data before transformations

### Database Fundamentals
DuckDB helps introduce database concepts such as:

- connecting to a database from Python
- creating persistent storage for structured data
- using SQL for querying and summarizing records
- thinking in terms of tables, rows, and columns

### Python Programming for Data Workflows
The code demonstrates reusable functions, modular script design, and practical application of Python for automation and data processing.

### Testing and Quality Assurance
The pytest setup encourages habit-forming testing skills, including verifying that required files exist and validating assumptions in the data pipeline.

### Problem Solving and Data Engineering Thinking
This project helps build a mindset for building robust systems:

- validate before using data
- separate raw data from processed data
- automate repetitive tasks
- handle errors gracefully
- create a repeatable workflow

## Future Improvements

This repository can be expanded to include:

- cleaning and transforming raw movie data
- inserting records into SQL tables
- building a movie recommendation engine
- ranking movies by popularity, genre, or user preferences
- generating insights from the stored dataset
- developing a simple frontend or API for recommendations

## Summary

MovieRecommenderApp is a beginner-to-intermediate data project that demonstrates how to fetch, validate, and store movie information from an API. It combines Python, data validation, JSON processing, database storage, and testing into a practical project that showcases real-world data engineering skills.

This repository is especially useful for learning how data flows from external sources into a structured, queryable system.

## License

This project currently does not include a formal license file. If needed, a license can be added later depending on how the project is intended to be used.
