import sqlite3

def connect_db():
    conn = sqlite3.connect("student_tracker.db")
    return conn

def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students(
        roll_number TEXT PRIMARY KEY,
        name TEXT,
        math INTEGER,
        science INTEGER,
        english INTEGER
    )
    ''')

    conn.commit()
    conn.close()
