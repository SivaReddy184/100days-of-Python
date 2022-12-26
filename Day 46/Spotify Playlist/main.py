import requests
from bs4 import BeautifulSoup
import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


# ------------------------------Scraping Billboard Top 100--------------------------------------------------------
songs_endpoint = "https://www.billboard.com/charts/hot-100/"
date = input("Which year do you want to travel to? Type the name in this format YYYY-MM-DD: ")
response = requests.get(f"{songs_endpoint}{date}/")

soup = BeautifulSoup(response.text, "html.parser")
titles = soup.find_all(class_="a-no-trucate", name="h3")
songs_titles = [title.getText(strip=True) for title in titles]
# print(songs_titles)


# ----------------------------------SPOTIFY AUTHENTICATION--------------------------------------------------------
SPOTIFY_CLIENT_ID = os.environ["SPOTIFY_CLIENT_ID"]
SPOTIFY_CLIENT_SECRET = os.environ["SPOTIFY_CLIENT_SECRET"]
REDIRECT_URL = "http://localhost:8888/callback"  # IMPORTANT!!! set this redirect URL inside your Spotify account

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="user-library-read playlist-modify-private",
        redirect_uri=REDIRECT_URL,
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=False,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)


# -----------------------------Searching Spotify for songs by title and getting song URIs---------------------------
song_uris = []
year = date.split("-")[0]
for song in songs_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# -----------------------------Creating a new private playlist in Spotify---------------------------------------------
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)


# ------------------------------Adding songs found into the new playlist---------------------------------------------
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
