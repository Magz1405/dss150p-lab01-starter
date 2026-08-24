import psycopg
from config import DB_CONFIG

def main():
    # Read the SQL file
    with open("sql/01_create_schema.sql", "r") as f:
        sql_script = f.read()

    # Execute and verify
    with psycopg.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(sql_script)
            conn.commit()
            print("Schema and table created successfully!\n")
            
            print("--- Verification: lab.customers Columns ---")
            cur.execute("""
                SELECT column_name, data_type, is_nullable
                FROM information_schema.columns
                WHERE table_schema = 'lab' AND table_name = 'customers'
                ORDER BY ordinal_position;
            """)
            for row in cur.fetchall():
                print(row)

if __name__ == "__main__":
    main()