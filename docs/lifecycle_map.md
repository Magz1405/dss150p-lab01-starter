# Data Lifecycle Map - Lab 01

## 1. Data Lifecycle Stages

| Lifecycle Stage | Description & Implementation Details |
| :--- | :--- |
| **Source System** | Raw data originates from CSV files (`customers.csv`, `products_optional_compare.csv`), JSON (`orders.json`), Parquet (`products.parquet`), and a local REST API (`local_api_server.py`). |
| **Ingestion** | Python scripts (`fetch_api.py`, custom loaders) extract data from files and API endpoints into memory. |
| **Storage** | Stored locally within the project directory structure (`data/`) and persisted relationally inside the Dockerized PostgreSQL database container (`dss150p-postgres`). |
| **Processing** | Data cleaning, inspection (`db_inspect.py`, `inspect_sources.py`), and transformation executed via Python pandas and SQL queries. |
| **Quality & Validation** | Schema validation, type-checking, and tracking connection health via diagnostic scripts (`verify_environment.py`). |
| **Delivery** | Tabular and structured datasets made ready for analytical consumption or loading into downstream relational tables. |
| **Consumer** | Data analysts, downstream reporti
ng tools, and script-based data pipelines. |

## 2. Data Flow Architecture

```text
[ Raw Sources: CSV, JSON, Parquet, API ] 
                 │
                 ▼
       [ Python Ingestion Scripts ]
                 │
                 ▼
    [ PostgreSQL Database Container ]
                 │
                 ▼
    [ Processing & Quality Checks ]
                 │
                 ▼
     [ Downstream Analytics / Consumer ]