from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, ListView, ListItem, Label, TextArea
from textual.containers import Horizontal

class TMDB_App(App):
    CSS_PATH = "tmdb.tcss"
    BINDINGS = [
        ("d", "toggle_dark", "Toggle Dark Mode"),
        ("q", "quit", "Quit")
        ]

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Footer()
        yield TextArea(placeholder="Search...", compact=True)

if __name__ == "__main__":
    app = TMDB_App()
    app.run()