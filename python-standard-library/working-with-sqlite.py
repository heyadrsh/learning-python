import sqlite3
import json
from pathlib import Path

# Sample data
movies = [
    {"id": 1, "title": "Terminator", "year": 1989},
    {"id": 2, "title": "Kindergarten Cop", "year": 1990},
    {"id": 3, "title": "Predator", "year": 1987}
]

# Create and connect to database
with sqlite3.connect("db.sqlite3") as conn:
    # Create table
    command = "CREATE TABLE IF NOT EXISTS Movies (id INTEGER PRIMARY KEY, title TEXT, year INTEGER)"
    conn.execute(command)

    # Insert data
    command = "INSERT INTO Movies (title, year) VALUES(?, ?)"
    for movie in movies:
        conn.execute(command, (movie["title"], movie["year"]))
    conn.commit()

    # Query data
    command = "SELECT * FROM Movies"
    cursor = conn.execute(command)
    for row in cursor:
        print(row)

    # Query with conditions
    command = "SELECT * FROM Movies WHERE year >= 1990"
    cursor = conn.execute(command)
    movies_after_1990 = cursor.fetchall()
    print("\nMovies from 1990 or later:", movies_after_1990)

    # Update data
    command = "UPDATE Movies SET year = ? WHERE title = ?"
    conn.execute(command, (1984, "Terminator"))
    conn.commit()

    # Delete data
    command = "DELETE FROM Movies WHERE year < 1985"
    conn.execute(command)
    conn.commit()

    # Using parameters to prevent SQL injection
    year = 1990
    command = "SELECT * FROM Movies WHERE year = ?"
    cursor = conn.execute(command, (year,))
    print("\nMovies from 1990:", cursor.fetchall())

    # Multiple operations in a transaction
    try:
        conn.execute("BEGIN TRANSACTION")
        conn.execute("INSERT INTO Movies (title, year) VALUES(?, ?)", 
                    ("Total Recall", 1990))
        conn.execute("UPDATE Movies SET year = ? WHERE title = ?",
                    (1991, "Kindergarten Cop"))
        conn.commit()
    except sqlite3.Error:
        conn.rollback()
        print("Transaction failed") 