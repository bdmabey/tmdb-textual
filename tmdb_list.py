from textual.widgets import ListView, ListItem, Label
from textual.containers import VerticalScroll
from textual.app import ComposeResult
from textual.reactive import reactive

from movie import Movie
import utilities

class TMDB_List(ListView):
    movies = reactive([Movie])

    def __init__(self, category: str = "pop"):
        super().__init__()
        self.category = category

    def on_mount(self) -> None:
        self.extend(self._create_movie_list())

    def _create_movie_list(self) -> list[Movie]:
        list = utilities.get_movie_lists(self.category)
        movies = []
        for i in list:
            movies.append(Movie(i["title"], i["vote_average"]))

        return movies