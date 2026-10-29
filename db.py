import sqlite3

API_KEY = "demo_key_a1b2c3d4e5f6g7h8i9j0"

def find_user(name):
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE name = '{name}'")
    return cursor.fetchall()
