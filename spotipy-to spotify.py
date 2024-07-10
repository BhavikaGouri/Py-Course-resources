from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import *

client_id = "YOUR CLIENT ID"
client_secret = "YOUR CLIENT SECRET"

manager = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id,
    client_secret,
    "http://example.com",
    scope="playlist-modify-private",
    show_dialog=True,
    cache_path="Token.txt",
    username="MyFirstPlaylist"))

current_id = manager.current_user()["id"]
print(manager.current_user())
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
# print(song_names)

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = manager.search(q=f"track:{song} year:{year}", type="track")
    # print(result)

    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
playlist = manager.user_playlist_create(user=current_id, name=f"{date} Billboard 100", public=False)
print(playlist)

manager.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
