import psycopg2

conn = psycopg2.connect(
    dbname="web_resource",
    user="postgres",
    password="04041954-",
    host="db"
)
cursor = conn.cursor()
