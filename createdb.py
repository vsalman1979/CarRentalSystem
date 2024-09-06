# create database and tables
import sqlite3


def create_tables():
    conn = sqlite3.connect('cr_database.db')
    cursor = conn.cursor()

    # Create customers table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customer (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cusname TEXT UNIQUE NOT NULL,
        address TEXT NOT NULL,
        email TEXT,
        mobile TEXT NOT NULL,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
        )
              
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS feedbacks (
        cusname	TEXT,
        feedback	TEXT
        )
    ''')

    # users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
          )
              
    ''')
    
    # Insert admin record fro user table
    username = 'admin'
    password = 'adminpass'

    cursor.execute("DELETE FROM users WHERE username='admin' and password='adminpass'")
    cursor.execute("INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)", (username, password))
 
    # cars table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cars (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        make TEXT NOT NULL,
        model TEXT NOT NULL,
        year INTEGER NOT NULL,
        mileage INTEGER NOT NULL,
        available_now TEXT CHECK(available_now IN ('Y', 'N')) NOT NULL,
        min_rent_period INTEGER NOT NULL,
        max_rent_period INTEGER NOT NULL,
        daily_charge INTEGER NOT NULL
    )
    ''')

    # rentals table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS rentals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        car_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        start_date TEXT NOT NULL,
        end_date TEXT NOT NULL,
        approved TEXT CHECK(approved IN ('Y', 'N', 'P')) NOT NULL,
        cus_username TEXT NULL,                   
        FOREIGN KEY(car_id) REFERENCES cars(id),
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    ''')
 
    conn.commit()
    conn.close()

if __name__ == "__main__":
     create_tables()
     print("Database created.")



