from textual.widgets import ListView, ListItem, Label
from textual.containers import VerticalScroll
from textual.app import ComposeResult
from textual.reactive import reactive

from movie import Movie
import utilities

class TMDB_List(ListView):
    def __init__(self, category: str = "pop", id: str | None = None):
        super().__init__(id=id)
        self.category = category

    def populate(self, movie_data: list[dict]) -> None:
        self.clear()
        movies = []
        for i in movie_data:
            movies.append(Movie(i["title"], i["vote_average"]))
        self.extend(movies)