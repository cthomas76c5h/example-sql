import sqlite3
import psycopg2

DB_FILE = "example.db"

def get_users():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cmd = cursor.execute("SELECT * from api_user")
    result = cmd.fetchall()
    data = []
    for row in result:
        keys = ["id", "username", "email", "password", "bio", "image"]
        obj = dict(zip(keys, row))
        data.append(obj)
    conn.commit()
    conn.close
    return data

def copy_data(data):
    conn = psycopg2.connect(database="example",
                            host="localhost",
                            user="postgres",
                            password="secret1234",
                            port="5433")
    cursor = conn.cursor()
    cursor.execute("BEGIN")
    for d in data:
        query = """insert into api_user
            (username, email, password, bio, image)
            values
            ({username!r}, {email!r}, {password!r}, {bio!r}, {image!r})""".format(**d)
        cursor.execute(query)
    cursor.execute("END")
    conn.commit()
    conn.close

def main():
    data = get_users()
    copy_data(data)

if __name__ == "__main__":
    main()
