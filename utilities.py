import httpx
import requests

async def get_movie_lists(category: str) -> list:
    url = ""
    api_key = ""
    if category == "pop":
        url = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"
    elif category == "now":
        url = "https://api.themoviedb.org/3/movie/now_playing?language=en-US&page=1"
    elif category == "top":
        url = "https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1"
    elif category == "up":
        url = "https://api.themoviedb.org/3/movie/upcoming?language=en-US&page=1"

    with open("api.cfg") as f:
        api_key = f.read()

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer " + api_key
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url=url, headers=headers)

    json = response.json()

    movie_list = json["results"]

    return movie_list

def get_genres():
    url = "https://api.themoviedb.org/3/genre/movie/list?language=en"
    api_key = ""

    with open("api.cfg") as f:
        api_key = f.read().strip()

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer " + api_key
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    genres_data = response.json()["genres"]

    # Convert list of dicts [{id: 28, name: "Action"}, ...]
    # into a dictionary for easy lookup {28: "Action", ...}
    genre_map = {genre["id"]: genre["name"] for genre in genres_data}
    return genre_map

# Global variable to store genres, loaded once
# This is a simple approach, for larger apps consider a singleton pattern or dependency injection
_genre_cache = {}

def get_genre_name(genre_id: int) -> str:
    """Looks up a genre name by its ID."""
    if not _genre_cache:
        # Load genres if cache is empty (first time this function is called)
        try:
            _genre_cache.update(get_genres())
        except Exception as e:
            print(f"Error loading genres: {e}")
            return "Unknown Genre"
    return _genre_cache.get(genre_id, "Unknown Genre")

def get_genre_names_from_ids(genre_ids: list[int]) -> list[str]:
    """Converts a list of genre IDs to a list of genre names."""
    return [get_genre_name(gid) for gid in genre_ids]