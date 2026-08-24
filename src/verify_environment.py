import psycopg2

try:
    conn = psycopg2.connect(
        host="127.0.0.1",
        port="5432",
        dbname="dss150p",
        user="dss150p",
        password="dss150p"
    )
    
    cur = conn.cursor()
    
    cur.execute("SELECT version();")
    print("Database Version:", cur.fetchone()[0])
    
    cur.execute("SELECT current_database();")
    print("Connected to Database:", cur.fetchone()[0])
    
    cur.close()
    conn.close()
    print("\nSuccess! Python is connected to PostgreSQL.")

except Exception as e:
    print(f"Connection failed: {e}")