import sqlite3
import os
import psycopg2

DB_FILE = "example.db"

def get_sql_file(fname):
    with open(fname, "r") as fp:
        text = fp.read()
    return text

def create_sqlite_tables():
    conn = sqlite3.connect(DB_FILE)
    cursor =  conn.cursor()
    for fname in os.listdir("models"):
        table_cmd = get_sql_file("models/" + fname)
        cursor.execute(table_cmd)
    conn.commit()
    conn.close

def create_postgres_tables():
    conn = psycopg2.connect(database="example",
                            host="localhost",
                            user="postgres",
                            password="secret1234",
                            port="5433")
    cursor = conn.cursor()
    for fname in os.listdir("models.postgres"):
        table_cmd = get_sql_file("models.postgres/" + fname)
        cursor.execute(table_cmd)
    conn.commit()
    conn.close

def main():
    create_sqlite_tables()
    create_postgres_tables()

if __name__ == "__main__":
    main()
