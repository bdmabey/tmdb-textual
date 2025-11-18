from textual.widgets import ListItem, Label
from textual.app import ComposeResult

class Movie(ListItem):
    def __init__(self, title: str = "title", rating: float = 0.0, genre: str = "unk"):
        super().__init__()
        self.title = title
        self.rating = rating
        self.genre = genre

    def compose(self) -> ComposeResult:
        yield Label(self.title, id="title")
        yield Label("Rating: " + str(self.rating))
        yield Label("Genre: " + self.genre)