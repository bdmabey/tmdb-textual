from textual.widgets import ListView

from movie import Movie

class TMDB_List(ListView):
    def __init__(self, category: str = "pop", id: str | None = None):
        super().__init__(id=id)
        self.category = category

    def populate(self, movie_data: list[dict]) -> None:
        self.clear()
        movies = []
        for i in movie_data:
            movies.append(Movie(i["title"], i["vote_average"], i["genre_ids"]))
        self.extend(movies)