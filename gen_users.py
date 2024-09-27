import sqlite3
from faker import Faker
import random
import string

DB_FILE = "example.db"

def gen_password():
    length = 12
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for i in range(length))

def bar(cursor):
    fake = Faker()
    username = fake.user_name()
    email = fake.email()
    password = gen_password()
    bio = fake.sentence()
    image = "https://upload.wikimedia.org/wikipedia/commons/7/7c/Profile_avatar_placeholder_large.png"
    query = f"""insert into api_user
            (username, email, password, bio, image)
            values
            ({username!r}, {email!r}, {password!r}, {bio!r}, {image!r})"""
    cursor.execute(query)

def foo():
    conn = sqlite3.connect("example.db")
    cursor =  conn.cursor()
    cursor.execute("BEGIN")
    for _ in range(40):
        bar(cursor)
    cursor.execute("END")
    conn.commit()
    conn.close

def main():
    foo()

if __name__ == "__main__":
    main()
