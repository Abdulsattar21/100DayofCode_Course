from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="b7a18842499241cdb1fe7583ec35c834",
        client_secret="935428ef3e0a448cbc3eb6d0e299bcbd",
        show_dialog=True,
        cache_path="token.txt",
        username="31r5ew7rpecvt3wa6rlrnqhwjyuu", ))
user_id = sp.current_user()["id"]
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
song_names = ["The list of song", "titles from your", "web scrape"]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

