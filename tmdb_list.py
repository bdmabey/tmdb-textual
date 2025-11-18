from textual.widgets import ListView, ListItem, Label
from textual.containers import VerticalScroll
from textual.app import ComposeResult

from movie import Movie

class TMDB_List(ListView):
    def __init__(self, category: str = "pop"):
        super().__init__()
        self.category = category

    def on_mount(self) -> None:
        self._create_movie_list()
        self.extend([
            Movie(),
            Movie(),
            Movie(),
            Movie(),
            Movie(),
            Movie(),
            Movie()
            ])

    def _create_movie_list():
        return [Movie]