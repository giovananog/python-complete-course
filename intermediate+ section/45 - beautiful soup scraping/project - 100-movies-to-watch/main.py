import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
data = response.text

soup = BeautifulSoup(data, "html.parser")

all_movies = soup.find_all(class_="title")

all_movies = all_movies[10:110]

# movies = []
# for i in all_movies:
#     movies.append(i.get_text())

movies = [i.get_text() for i in all_movies]

movies.reverse()

with open("movie_list.txt", "a") as file:
    for i in movies:
        a = str(i.encode('utf-8')).split('b')[1].replace("'", "")
        file.write(f"{a}\n")

