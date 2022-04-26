import sqlite3


connection = sqlite3.connect("data.db")
connection.row_factory = sqlite3.Row


def create_table():
    with connection:
        connection.execute("DROP TABLE IF EXISTS entries;")
        connection.execute(
            "CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT);",
        )


def close_connection():
    connection.close()


def add_entry(entry_content, entry_date):
    with connection:
        connection.execute(
            "INSERT INTO entries (content, date) VALUES (?, ?);",
            (entry_content, entry_date),
        )


def get_entries():
    cursor = connection.execute(
        "SELECT content, date FROM entries;",
    )
    return cursor
