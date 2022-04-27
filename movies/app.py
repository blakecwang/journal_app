#!/usr/bin/env python


import psycopg2
from pprint import pprint


url = "postgres://aaliwkpw:8o3PcnfTOM5Ojf1-uMhwK2ckyu1_8sgS@heffalump.db.elephantsql.com/aaliwkpw"
connection = psycopg2.connect(url)
cursor = connection.cursor()


DROP_USERS_TABLE = "DROP TABLE IF EXISTS users;"
CREATE_USERS_TABLE = """CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY
);"""

DROP_MOVIES_TABLE = "DROP TABLE IF EXISTS movies;"
CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS movies (
    id SERIAL PRIMARY KEY,
    title TEXT,
    released_at REAL
);"""

DROP_WATCHES_TABLE = "DROP TABLE IF EXISTS watches;"
CREATE_WATCHES_TABLE = """CREATE TABLE IF NOT EXISTS watches (
    user_username TEXT,
    movie_id INTEGER,
    FOREIGN KEY(user_username) REFERENCES users(username),
    FOREIGN KEY(movie_id) REFERENCES movies(id)
);"""

INSERT_INTO_USERS = "INSERT INTO users (username) VALUES (%s);"
INSERT_INTO_MOVIES = "INSERT INTO movies (title, released_at) VALUES (%s, %s);"
INSERT_INTO_WATCHES = "INSERT INTO watches (user_username, movie_id)"

SELECT_FROM_USERS = "SELECT * FROM users;"




print("Welcome!")

with connection.cursor() as cursor:
    cursor.execute(DROP_USERS_TABLE)
    cursor.execute(DROP_MOVIES_TABLE)
    cursor.execute(DROP_WATCHES_TABLE)
    cursor.execute(CREATE_USERS_TABLE)
    cursor.execute(CREATE_MOVIES_TABLE)
    cursor.execute(CREATE_WATCHES_TABLE)

menu = {
    "a": "insert_user",
    "b": "select_all_users",
    "exit": "exit",
}

def insert_user():
    username = input("username: ")
    with connection.cursor() as cursor:
        cursor.execute(INSERT_INTO_USERS, (username,))

def select_all_users():
    with connection.cursor() as cursor:
        cursor.execute(SELECT_FROM_USERS)
        print(cursor.fetchall())

while (user_input := input(str(menu))) != "exit":
    try:
        fn = menu[user_input]
        eval(fn + "()")
    except KeyError:
        print("invalid input, please try again")

connection.close()
print("Goodbye! :)")
