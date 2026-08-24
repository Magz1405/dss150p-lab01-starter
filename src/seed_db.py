import psycopg
from config import DB_CONFIG

def main():
    # Read the SQL file
    with open("sql/seed_support_tickets.sql", "r", encoding="utf-8") as file:
        sql_commands = file.read()

    # Connect to the database and run the commands
    with psycopg.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(sql_commands)
            conn.commit()
            
    print("Database seeded successfully!")

if __name__ == "__main__":
    main()