from textual.widgets import ListView

class TMDB_List(ListView):
    def __init__(self, category: str = "pop"):
        self.category = category