import sqlite3

DATABASE_URL = "countries.db"

def get_connection():
    connection = sqlite3.connect(DATABASE_URL)
    connection.row_factory = sqlite3.Row
    return connection