import sqlite3
import hashlib

conn = sqlite3.connect("users_secure.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
username TEXT,
password TEXT
)
""")

# Hash function
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Create default user only once
cursor.execute("SELECT * FROM users WHERE username=?", ("admin",))
if cursor.fetchone() is None:
    cursor.execute(
        "INSERT INTO users VALUES(?,?)",
        ("admin", hash_password("admin123"))
    )
    conn.commit()


def login():

    print("===== Secure Login =====")

    username = input("Username: ").strip()
    password = input("Password: ").strip()

    encrypted = hash_password(password)

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, encrypted)
    )

    result = cursor.fetchone()

    if result:
        print("\nLogin Successful")
    else:
        print("\nInvalid Username or Password")


login()

conn.close()