import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("Which year do you want to travel to? Type date in this format  YYYY-MM-DD:")
headers ={"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0"}
URL = f"https://www.billboard.com/charts/hot-100/{date.strip()}"

response = requests.get(url="https://www.billboard.com/charts/hot-100/2024-04-25/",headers=headers)
website = response.text
songs_titles = []

soup = BeautifulSoup(website, "html.parser")

songs_tags = soup.select(selector="ul li ul li h3.c-title")

for song_tag in songs_tags:
    songs_titles.append(song_tag.getText(strip=True))

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://127.0.0.1:9090",
        client_id="YOUR CLIENT ID",
        client_secret="YOUR CLIENT SECRET",
        show_dialog=True,
        cache_path="token.txt",
        username="YOUR SPOTIFY USERNAME", 
    )
)
user_id = sp.current_user()["id"]
print(user_id)

song_uris = []
year = date.split("-")[0]
for song in songs_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
