import sqlite3

class DatabaseManager:
    def __init__(self, db_name="password_manager.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """Create a Db table"""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS passwords (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                account TEXT NOT NULL,
                username TEXT,
                password TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def fetch_all_passwords(self):
        """Get all records"""
        self.cursor.execute("SELECT id, account, username, password FROM passwords")
        return self.cursor.fetchall()

    def add_password(self, account, username, password):
        """Add new record"""
        self.cursor.execute("INSERT INTO passwords (account, username, password) VALUES (?, ?, ?)", (account, username, password))
        self.conn.commit()

    def update_password(self, record_id, account, username, password):
        """Update record"""
        self.cursor.execute("UPDATE passwords SET account = ?, username = ?, password = ? WHERE id = ?", (account, username, password, record_id))
        self.conn.commit()

    def close(self):
        """Close the Db"""
        self.conn.close()
