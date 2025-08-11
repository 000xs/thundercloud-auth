import sqlite3
import threading
import os
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

        # Use writable path on Vercel
        tmp_dir = "/tmp"
        os.makedirs(tmp_dir, exist_ok=True)
        self.db_path = os.path.join(tmp_dir, "database.db")

        self.init_db()

    def init_db(self):
        with self.get_db_connection() as con:
            cur = con.cursor()
            cur.execute(self.user_table_create_query)
            con.commit()

    def get_db_connection(self):
        return sqlite3.connect(self.db_path, check_same_thread=False)

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
            return cur.fetchone()


    def validate_user(self, user_data):
        with self.get_db_connection() as con:
            cur = con.cursor()
            cur.execute(
                "SELECT * FROM users WHERE username = ? AND id = ?",
                (user_data["user_name"], user_data["user_id"]),
            )
            return cur.fetchone()
