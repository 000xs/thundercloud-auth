import sqlite3
import threading

class Database:
    def __init__(self):
        self.user_table_create_query = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        );
        """
        self.lock = threading.Lock()

        with sqlite3.connect("database.db") as con:
            cur = con.cursor()
            cur.execute(self.user_table_create_query)
            con.commit()

    def adduser(self, username, password):
        with self.lock:
            
            with sqlite3.connect("database.db") as con:
                cur = con.cursor()
                try:
                    cur.execute(
                        "INSERT INTO users (username, password) VALUES (?, ?)",
                        (username, password),
                    )
                    con.commit()
                    return cur.lastrowid
                except sqlite3.IntegrityError:
                    return None  # username exists

    def verify_user(self, username, password):
        with sqlite3.connect("database.db") as con:
            cur = con.cursor()
            cur.execute(
                "SELECT id FROM users WHERE username = ? AND password = ?",
                (username, password),
            )
            user = cur.fetchone()
            return user
        
    def validate_user(self, user_data):
        with sqlite3.connect("database.db") as con:
            cur = con.cursor()
            cur.execute(
                "SELECT * FROM users WHERE username = ? AND id = ?",
                (user_data['user_name'], user_data['user_id']),
            )
            user = cur.fetchone()
            return user if user else None

