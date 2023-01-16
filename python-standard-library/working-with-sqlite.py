import sqlite3
import json
from pathlib import Path

movies = json.loads(Path("movies.json").read_text())

with sqlite3.connect("db.sqlite3") as conn:
    command = "CREATE TABLE IF NOT EXISTS Movies (id INTEGER PRIMARY KEY, title TEXT, year INTEGER)"
    conn.execute(command)

    command = "INSERT INTO Movies (title, year) VALUES(?, ?)"
    for movie in movies:
        conn.execute(command, (movie["title"], movie["year"]))
    conn.commit()

    command = "SELECT * FROM Movies"
    cursor = conn.execute(command)
    print("\nAll movies from database:")
    for row in cursor:
        print(row)
    
    command = "SELECT * FROM Movies WHERE year > 1985"
    cursor = conn.execute(command)
    print("\nMovies after 1985:")
    movies_list = cursor.fetchall()
    print(movies_list)

    command = "UPDATE Movies SET year = ? WHERE title = ?"
    conn.execute(command, (1991, "Terminator"))
    
    command = "DELETE FROM Movies WHERE year < 1990"
    conn.execute(command)
    conn.commit() 