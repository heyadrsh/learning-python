import json
from pathlib import Path

# Writing JSON to a string
movies = [
    {"id": 1, "title": "Terminator", "year": 1989},
    {"id": 2, "title": "Kindergarten Cop", "year": 1990}
]

# Converting to JSON string
movies_json = json.dumps(movies)
print(movies_json)

# Converting to JSON string with formatting
movies_json = json.dumps(movies, indent=2)
print(movies_json)

# Writing JSON to a file
Path("movies.json").write_text(movies_json)

# Reading JSON from a file
movies = json.loads(Path("movies.json").read_text())
print(movies)

# Working with custom objects
class Movie:
    def __init__(self, id, title, year):
        self.id = id
        self.title = title
        self.year = year

# Custom JSON encoder
class MovieEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Movie):
            return {'id': obj.id, 'title': obj.title, 'year': obj.year}
        return super().default(obj)

movie = Movie(1, "Terminator", 1989)
movie_json = json.dumps(movie, cls=MovieEncoder)
print(movie_json)

# Custom JSON decoder
def movie_decoder(dict):
    if 'id' in dict and 'title' in dict and 'year' in dict:
        return Movie(dict['id'], dict['title'], dict['year'])
    return dict

movie_obj = json.loads(movie_json, object_hook=movie_decoder)
print(f"Movie: {movie_obj.title} ({movie_obj.year})") 