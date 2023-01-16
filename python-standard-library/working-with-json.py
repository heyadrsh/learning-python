import json
from pathlib import Path

movies = [
    {"id": 1, "title": "Terminator", "year": 1984},
    {"id": 2, "title": "Kindergarten Cop", "year": 1990}
]

data = json.dumps(movies)
Path("movies.json").write_text(data)

data = Path("movies.json").read_text()
movies = json.loads(data)
print("\nAll movies:")
print(movies)

movie = {
    "title": "Die Hard",
    "year": 1988,
    "price": 9.99,
    "is_awesome": True,
    "actors": ["Bruce Willis", "Alan Rickman"]
}

with open("movie.json", "w") as file:
    json.dump(movie, file, indent=4)

with open("movie.json") as file:
    movie = json.load(file)
    print("\nMovie details:")
    print(movie) 