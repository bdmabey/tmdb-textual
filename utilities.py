import requests

def get_movie_lists(category: str):
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

    response = requests.get(url, headers=headers)

    json = response.json()

    movie_list = json["results"]

    return movie_list