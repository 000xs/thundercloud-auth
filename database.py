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
            password TEXT,
            score INTEGER DEFAULT 0
        );
        """
        self.lock = threading.Lock()

        # Use writable path on Vercel
        tmp_dir = "/tmp"
        os.makedirs(tmp_dir, exist_ok=True)
        self.db_path = os.path.join(tmp_dir, "database.db")

        self.init_db()
        self._ensure_progress_column()

    def init_db(self):
        with self.get_db_connection() as con:
            cur = con.cursor()
            cur.execute(self.user_table_create_query)
            con.commit()

    def _ensure_progress_column(self):
        with self.get_db_connection() as con:
            cur = con.cursor()
            # Check if the 'score' column exists
            cur.execute("PRAGMA table_info(users)")
            columns = [column[1] for column in cur.fetchall()]
            if 'score' not in columns:
                # Rename 'progress' to 'score' if 'progress' exists
                if 'progress' in columns:
                    cur.execute("ALTER TABLE users RENAME COLUMN progress TO score")
                else:
                    cur.execute("ALTER TABLE users ADD COLUMN score INTEGER DEFAULT 0")
                con.commit()

    def get_db_connection(self):
        return sqlite3.connect(self.db_path, check_same_thread=False)

    def adduser(self, username, password):
        with self.lock:
            with self.get_db_connection() as con:
                cur = con.cursor()
                try:
                    cur.execute(
                        "INSERT INTO users (username, password, score) VALUES (?, ?, ?)",
                        (username, password, 0),
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

    def get_all_users_progress(self):
        with self.get_db_connection() as con:
            cur = con.cursor()
            cur.execute(
                "SELECT username, score FROM users ORDER BY score DESC"
            )
            return cur.fetchall()

    def update_user_score(self, user_id, score):
        with self.lock:
            with self.get_db_connection() as con:
                cur = con.cursor()
                cur.execute(
                    "UPDATE users SET score = ? WHERE id = ?",
                    (score, user_id),
                )
                con.commit()


    def validate_user(self, user_data):
        with self.get_db_connection() as con:
            cur = con.cursor()
            cur.execute(
                "SELECT * FROM users WHERE username = ? AND id = ?",
                (user_data["user_name"], user_data["user_id"]),
            )
            return cur.fetchone()
