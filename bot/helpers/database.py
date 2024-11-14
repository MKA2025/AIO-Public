import sqlite3
from contextlib import closing

DATABASE_NAME = 'your_database.db'

def get_database_connection():
    """Create a new database connection."""
    return sqlite3.connect(DATABASE_NAME)

def fetch_data(query: str, params: tuple = ()):
    """Fetch data from the database."""
    with closing(get_database_connection()) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()

def insert_data(query: str, data: tuple):
    """Insert data into the database."""
    with closing(get_database_connection()) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute(query, data)
            conn.commit()

def update_data(query: str, data: tuple):
    """Update data in the database."""
    with closing(get_database_connection()) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute(query, data)
            conn.commit()

def delete_data(query: str, params: tuple):
    """Delete data from the database."""
    with closing(get_database_connection()) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute(query, params)
            conn.commit()
