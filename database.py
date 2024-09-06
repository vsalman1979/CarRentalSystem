import sqlite3

class Database:

    def __init__(self, db_name='cr_database.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def execute_query(self, query, params=()):
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
            return self.cursor  # Return the cursor
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return None

    def fetch_all(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def fetch_one(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchone()

    def close(self):
         self.conn.close()


