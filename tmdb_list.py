from textual.widgets import ListView, ListItem, Label

class TMDB_List(ListView):
    def __init__(self, category: str = "pop"):
        super().__init__()
        self.category = category

    def on_mount(self) -> None:
        self.extend([ListItem(Label("ext class item."))])