from textual.widgets import ListItem, Label
from textual.app import ComposeResult

import utilities

class Movie(ListItem):
    def __init__(self, title: str = "title", rating: float = 0.0, genre_ids: list[int] | None = None):
        super().__init__()
        self.title = title
        self.rating = rating
        self.genre_ids = genre_ids if genre_ids is not None else []
        self._genre_names: list[str] | None = None

    @property
    def genre_names(self) -> list[str]:
        if self._genre_names is None:
            # This is where we use the utility function to get names
            self._genre_names = utilities.get_genre_names_from_ids(self.genre_ids)
        return self._genre_names

    def compose(self) -> ComposeResult:
        yield Label(self.title, id="title")
        yield Label("Rating: " + str(self.rating))
        yield Label(f"Genre: {', '.join(self.genre_names)}")