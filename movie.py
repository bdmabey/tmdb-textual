from textual.containers import VerticalGroup
from textual.widgets import ListItem, Label
from textual.app import ComposeResult

class Movie(ListItem):
    def __init__(self, title: str = "title", rating: str = "0", genre: str = "unk"):
        super().__init__()
        self.title = title
        self.rating = rating
        self.genre = genre

    def compose(self) -> ComposeResult:
        yield Label(self.title, id="title")
        yield Label("Rating: " + self.rating)
        yield Label("Genre: " + self.genre)