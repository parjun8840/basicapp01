import datetime
import sqlite3
CREATE_MOVIE_TABLES= """ create table if not exists movies (
    title TEXT,
    release_timestamp REAL,
    watched INTEGER
);"""

INSERT_MOVIES="Insert into movies (title,release_timestamp,watched) Values(?,?,0)"
SELECT_ALL_MOVIES="Select * From movies"
SELECT_UPCOMING_MOVIES="Select * From movies WHERE release_timestamp > ?;"
SELECT_WATCHED_MOVIES="Select * From movies WHERE watched=1;"
SET_MOVIE_WATCHED="Update movies set watched=1 WHERE title=?;"

connection = sqlite3.connect("data.db")

def create_table():
    with connection:
        connection.execute(CREATE_MOVIE_TABLES)

def add_movie(title, release_timestamp):
    with connection:
        connection.execute(INSERT_MOVIES,(title,release_timestamp))

def get_movies(upcoming=False):
    with connection:
        cursor = connection.cursor()
        if upcoming:
            today_timestamp = datetime.datetime.today().timestamp()
            cursor.execute(SELECT_UPCOMING_MOVIES,(today_timestamp,))
        else:
            cursor.execute(SELECT_ALL_MOVIES) 
        return cursor.fetchall()

def get_watched_movies():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_WATCHED_MOVIES)
        return cursor.fetchall()

def watch_movie(title):
    with connection:
        connection.execute(SET_MOVIE_WATCHED,(title,))