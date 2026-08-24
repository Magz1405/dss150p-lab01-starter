# DSS150P Lab 01: Data Sources and Profiling
**Name:** Feny Lane L. Tolentino 
**Student Number:** 2024110095
## Purpose of the Laboratory
To identify, profile, and document various data sources (CSV, JSON, Parquet, REST API, PostgreSQL) and establish a basic data contract and SQL schema for future ingestion.

## Software Requirements
- Python 3.x
- Docker Desktop (for PostgreSQL)
- Git

## Exact Steps to Reproduce the Environment
1. Clone the repository.
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment.
4. Install dependencies: `pip install -r requirements.txt`
5. Copy `.env.example` to `.env`.

## Start and Stop PostgreSQL
- **Start:** `docker compose up -d`
- **Stop:** `docker compose down`

## How to Run Each Python Script
- Profile sources: `python src/profile_sources.py`
- Fetch API data: `python src/inspect_api.py`
- Seed Database: `python src/seed_db.py`
- Inspect Database: `python src/db_inspect.py`
- Apply Schema: `python src/apply_schema.py`

## Description of Each Source
- `customers.csv`: Customer demographic data (contains nulls and duplicates).
- `orders.json`: Transactional order records (contains nested shipping data).
- `products.parquet`: Product catalog with strict data types.
- `api_snapshot.json`: Support tickets fetched via REST API.
- `support_tickets` (PostgreSQL): Relational data containing ticket statuses.

## Known Limitations or Unresolved Questions
- The `customers.csv` file requires a deduplication step and handling for missing `email` and `city` fields before final ingestion.