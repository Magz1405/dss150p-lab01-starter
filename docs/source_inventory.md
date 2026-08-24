# Data Source Inventory

## 1. Customers Data
* **Source name**: `customers.csv`
* **Source-system type**: Local File System
* **Data format**: CSV
* **Structured / semi-structured / unstructured**: Structured
* **Expected update pattern**: Periodic batch updates
* **Likely acquisition method**: File read (Python pandas/csv module)
* **Schema location or schema owner**: Inferred from header row
* **Possible primary/business key**: `customer_id`
* **Potential schema-evolution risk**: High (columns can be easily added, removed, or renamed without strict enforcement)
* **Potential data-quality risk**: Missing values, incorrect delimiters, inconsistent data types

## 2. Orders Data
* **Source name**: `orders.json`
* **Source-system type**: Local File System
* **Data format**: JSON
* **Structured / semi-structured / unstructured**: Semi-structured
* **Expected update pattern**: Near real-time or frequent batch
* **Likely acquisition method**: File read / JSON parsing
* **Schema location or schema owner**: Embedded within the JSON key-value pairs
* **Possible primary/business key**: `order_id`
* **Potential schema-evolution risk**: Moderate (nested structures or new keys might be introduced without warning)
* **Potential data-quality risk**: Missing keys, mixed data types within the same field

## 3. Products Data
* **Source name**: `products.parquet`
* **Source-system type**: Local File System
* **Data format**: Parquet
* **Structured / semi-structured / unstructured**: Structured
* **Expected update pattern**: Scheduled batch processing
* **Likely acquisition method**: Parquet reader (pandas/pyarrow)
* **Schema location or schema owner**: Embedded tightly in the Parquet file metadata
* **Possible primary/business key**: `product_id`
* **Potential schema-evolution risk**: Low (Parquet enforces strict schema on write)
* **Potential data-quality risk**: Data type mismatch errors during extraction

## 4. Support Tickets Data
* **Source name**: Local REST API
* **Source-system type**: Web Service / API
* **Data format**: JSON (API Payload)
* **Structured / semi-structured / unstructured**: Semi-structured
* **Expected update pattern**: On-demand / Real-time
* **Likely acquisition method**: HTTP GET requests via Python `requests` library
* **Schema location or schema owner**: API Documentation / Developer team
* **Possible primary/business key**: `ticket_id`
* **Potential schema-evolution risk**: High (API version upgrades or endpoint payload changes)
* **Potential data-quality risk**: Network connection timeouts, rate limiting, partial payloads
* **Retrieval timestamp in UTC**: *2026-08-24T16:53:45.427917+00:00*

## 5. Inventory Data
* **Source name**: PostgreSQL Database
* **Source-system type**: Relational Database Management System (RDBMS)
* **Data format**: Relational Tables
* **Structured / semi-structured / unstructured**: Structured
* **Expected update pattern**: Continuous transactional updates
* **Likely acquisition method**: SQL Query via SQLAlchemy/psycopg2
* **Schema location or schema owner**: Database `information_schema` / DBA
* **Possible primary/business key**: `inventory_id` or `product_id`
* **Potential schema-evolution risk**: Low (requires explicit `ALTER TABLE` DDL commands)
* **Potential data-quality risk**: Null values in columns missing `NOT NULL` constraints
