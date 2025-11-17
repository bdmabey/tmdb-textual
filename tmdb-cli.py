from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, ListView, ListItem, Label, TextArea
from textual.containers import Horizontal

class TMDB_App(App):
    CSS_PATH = "tmdb.tcss"
    BINDINGS = [
        ("d", "toggle_dark", "Toggle Dark Mode"),
        ("s", "search", "Search for a movie"),
        ("q", "quit", "Quit")
        ]

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Footer()
        yield Label("Popular", id="pop")
        yield Label("Now Playing", id="now")
        yield Label("Top Rated", id="top")
        yield Label("Upcoming", id="up")
        yield ListView(ListItem(Label("test1")))
        yield ListView(ListItem(Label("test2")))
        yield ListView(ListItem(Label("test3")))
        yield ListView(ListItem(Label("test4")))
        yield TextArea(placeholder="Search...", compact=True)

if __name__ == "__main__":
    app = TMDB_App()
    app.run()