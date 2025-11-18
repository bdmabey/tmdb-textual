from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, ListView, ListItem, Label, TextArea, LoadingIndicator
from textual.containers import Horizontal
from textual.events import Key
from textual.message import Message

from tmdb_list import TMDB_List
import utilities
import asyncio

class TMDB_App(App):
    """TMDB base application. Holds the main screen layout."""

    CSS_PATH = "tmdb.tcss"
    BINDINGS = [
        ("d", "toggle_dark", "Toggle Dark Mode"),
        ("s", "search", "Search for a movie"),
        ("q", "quit", "Quit")
        ]

    class MovieListsLoaded(Message):
        def __init__(self, category: str, movies: list[dict]) -> None:
            super().__init__()
            self.category = category
            self.movies = movies

    def on_mount(self) -> None:
        self.run_worker(self._load_all_movie_lists(), exclusive=True)

    async def _load_all_movie_lists(self) -> None:
        categories = ["pop", "now", "top", "up"]

        tasks = []
        for category in categories:
            tasks.append(self._load_and_post_movies(category))
        
        await asyncio.gather(*tasks)

    async def _load_and_post_movies(self, category: str) -> None:
        """Loads movies for a specific category and posts an event."""
        try:
            # Assuming utilities.get_movie_lists is async
            movie_list_data = await utilities.get_movie_lists(category)
            self.post_message(self.MovieListsLoaded(category, movie_list_data))
        except Exception as e:
            self.log(f"Error loading {category} movies: {e}")

    def on_tmdb_app_movie_lists_loaded(self, message: MovieListsLoaded) -> None:
        """Handle the custom event when a movie list is loaded."""
        list_view = self.query_one(f"#{message.category}-list", TMDB_List)
        list_view.populate(message.movies)

    def on_key(self, event: Key):
        """Selects the search bar."""
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
        yield TMDB_List("pop", id="pop-list")
        yield TMDB_List("now", id="now-list")
        yield TMDB_List("top", id="top-list")
        yield TMDB_List("up", id="up-list")
        yield TextArea(placeholder="Search...", compact=True, id="search")

if __name__ == "__main__":
    app = TMDB_App()
    app.run()