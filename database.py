import sqlite3
import threading
from utils import valid_hashed_password


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
        self.db_path = ":memory:" # Use in-memory database for Vercel
        self.init_db()

    def init_db(self):
        with self.get_db_connection() as con:
            cur = con.cursor()
            cur.execute(self.user_table_create_query)
            con.commit()

    def get_db_connection(self):
        return sqlite3.connect(self.db_path)

    def adduser(self, username, password):
        with self.lock:

            with self.get_db_connection() as con:
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

    def verify_user(self, username):
        with self.get_db_connection() as con:
            cur = con.cursor()
            cur.execute(
                "SELECT * FROM users WHERE username = ?",
                (username,),
            )
            user = cur.fetchone()
            return user

    def validate_user(self, user_data):
        with self.get_db_connection() as con:
            cur = con.cursor()
            cur.execute(
                "SELECT * FROM users WHERE username = ? AND id = ?",
                (user_data["user_name"], user_data["user_id"]),
            )
            user = cur.fetchone()
            return user if user else None
