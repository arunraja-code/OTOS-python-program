import sqlite3
database = sqlite3.connect("users.db")
cursor = database.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT NOT NULL UNIQUE,
email TEXT NOT NULL,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
""")
database.commit()
