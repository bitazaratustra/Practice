# pylint: disable=missing-docstring, C0103
import sqlite3

conn = sqlite3.connect('data/movies.sqlite')
#db = conn.cursor()
#rows = db.fetchall()



def directors_count(db):
    # return the number of directors contained in the database
    db = conn.cursor()
    query = 'SELECT COUNT(id) FROM directors'
    db.execute(query)
    results = db.fetchall()
    print(int(results[0][0]))

directors_count(conn)

def directors_list(db):
    # return the list of all the directors sorted in alphabetical order
    pass  # YOUR CODE HERE


def love_movies(db):
    # return the list of all movies which contain the exact word "love"
    # in their title, sorted in alphabetical order
    pass  # YOUR CODE HERE


def directors_named_like_count(db, name):
    # return the number of directors which contain a given word in their name
    pass  # YOUR CODE HERE


def movies_longer_than(db, min_length):
    # return this list of all movies which are longer than a given duration,
    # sorted in the alphabetical order
    pass  # YOUR CODE HERE
