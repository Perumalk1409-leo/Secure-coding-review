# vulnerable_login.py

import sqlite3

# Database connection
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    username TEXT,
    password TEXT
)
""")

# Default user
cursor.execute("INSERT INTO users VALUES('admin','admin123')")
conn.commit()


def login():
    print("===== LOGIN =====")

    username = input("Username: ")
    password = input("Password: ")

    # Vulnerability: SQL Injection
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"

    print("\nExecuting Query:")
    print(query)

    cursor.execute(query)

    result = cursor.fetchone()

    if result:
        print("\nLogin Successful")
    else:
        print("\nInvalid Username or Password")


login()

conn.close()