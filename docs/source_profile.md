# Source Data Profiles & Observations

## 1. customers.csv
* **Nullability Risk:** The `email` and `city` columns contain missing values (3 and 2 missing, respectively). A future pipeline must handle or filter these nulls to avoid breaking downstream processes.
* **Duplicate Records:** There are 2 fully duplicated rows in the dataset, requiring a deduplication step before loading this data into a database.
* **Type Ambiguity:** The `signup_date` is currently inferred as a plain string (`object`). It will need to be explicitly parsed into a proper `date` or `datetime` type.

## 2. orders.json
* **Nested JSON Structure:** The `shipping` column contains nested dictionaries (e.g., `{'region': 'Region VII', 'method': 'Standard'}`). This column must be flattened into separate fields (like `shipping_region` and `shipping_method`) before it can be saved in a standard relational database.
* **Clean Initial State:** There are no missing values and zero fully duplicated rows, indicating that the system generating these orders has good internal data validation.

## 3. products.parquet
* **Strict Typing:** The Parquet format successfully preserved strict numeric types (e.g., `int32` for `stock_quantity` and `float64` for `weight_kg`). This means the pipeline won't have to guess or manually cast these types.
* **High Data Quality:** There are zero missing values and zero duplicated rows, making this the cleanest and most reliable source of the three.
## 4. PostgreSQL (support_tickets)
* **Table Name**: `support_tickets`
* **Row Count**: 250
* **Columns, Types, and Nullability**:
  * `ticket_id`: integer (NOT NULL) — *Implied Primary Key*
  * `customer_id`: character varying (NOT NULL)
  * `category`: character varying (NOT NULL)
  * `priority`: character varying (NOT NULL)
  * `assigned_agent`: character varying (NULLABLE)
  * `opened_at`: timestamp without time zone (NOT NULL)
  * `resolved_at`: timestamp without time zone (NULLABLE)
  * `status`: character varying (NOT NULL)
* **Observations**: The `assigned_agent` and `resolved_at` fields are nullable. This aligns with standard business logic, as tickets currently "In Progress" (like ticket #4) do not yet have a resolution time.

**Sample Records:**
1. `(1, 'C0246', 'Technical', 'High', 'J. Reyes', 2026-06-19 04:00, 2026-06-21 13:00, 'Resolved')`
2. `(2, 'C0130', 'Product', 'Medium', 'J. Reyes', 2026-05-26 07:00, 2026-05-26 23:00, 'Closed')`
3. `(3, 'C0094', 'Delivery', 'Medium', 'J. Reyes', 2026-03-28 09:00, 2026-03-31 17:00, 'Closed')`
4. `(4, 'C0057', 'Technical', 'High', 'L. Tan', 2026-04-25 19:00, None, 'In Progress')`
5. `(5, 'C0120', 'Delivery', 'High', 'R. Cruz', 2026-01-20 02:00, 2026-01-22 21:00, 'Resolved')`