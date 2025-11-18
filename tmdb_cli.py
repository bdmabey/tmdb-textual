from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, ListView, ListItem, Label, TextArea
from textual.containers import Horizontal
from textual.events import Key

from tmdb_list import TMDB_List
from movie import Movie

class Test_list(ListView):
    def on_mount(self) -> None:
        self.extend([ListItem(Label("class item")), Movie()])

    def on_list_view_selected(self, event: ListView.Selected):
        select = event.index
        self.pop(select)

class TMDB_App(App):
    """TMDB base application. Holds the main screen layout."""

    CSS_PATH = "tmdb.tcss"
    BINDINGS = [
        ("d", "toggle_dark", "Toggle Dark Mode"),
        ("s", "search", "Search for a movie"),
        ("q", "quit", "Quit")
        ]

    def on_key(self, event: Key):
        if event.character == "s":
            search = self.query_one("#search")
            search.focus()

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Footer()
        yield Label("Popular", id="pop")
        yield Label("Now Playing", id="now")
        yield Label("Top Rated", id="top")
        yield Label("Upcoming", id="up")
        yield ListView(
            ListItem(Label("test1")), 
            ListItem(Label("asdf"))
        )
        # yield ListView(ListItem(Label("test2")))
        yield TMDB_List()
        yield Test_list()
        yield ListView(ListItem(Label("test4")))
        yield TextArea(placeholder="Search...", compact=True, id="search")

if __name__ == "__main__":
    app = TMDB_App()
    app.run()