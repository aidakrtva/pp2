import psycopg2

conn = psycopg2.connect(
    host="localhost",
    dbname="phonebook",
    user="postgres",
    password="808",
    port=5432
)

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(255) NOT NULL,
        second_name VARCHAR(255) NOT NULL,
        phone VARCHAR(20) NOT NULL
    )
""")
conn.commit()

cur.close()
conn.close()