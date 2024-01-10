import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


data_input = input("Type the data you want to travel to! (Format: YYYY-MM-DD): ")

url = f"https://www.billboard.com/charts/hot-100/{data_input}/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
all_titles = soup.find_all(class_="u-line-height-normal@mobile-max")


titles = [all_titles[i].get_text().split("\t")[9] for i in range(len(all_titles)) if i % 2 == 0]

client_id = "-"
client_secret = "-"
redirect_url = "http://example.com"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_url, scope="playlist-modify-public", show_dialog=True, cache_path="token.txt", username="giovananogueir"))

user_id = sp.current_user()["id"]


av_titles = []

for i in titles:
    try:
        results = sp.search(q=f"track:{i} year:{data_input.split('-')[0]}", type='track')
        uri = results['tracks']['items'][0]['uri']
        av_titles.append(uri)
    except:
        pass


playlist = sp.user_playlist_create(user_id, f"{data_input} Billboard 100", public=True, collaborative=False, description=f'top 100 tracks from {data_input} :D')
playlist_id = playlist['id']

sp.playlist_add_items(playlist_id, av_titles)