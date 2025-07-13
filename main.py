import requests
from bs4 import BeautifulSoup

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

print(songs_titles)

