import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
data = soup.find_all(name="h3", class_="title")

movies = []
for item in data:
    movie = item.getText()
    movies.append(movie)

movies = movies[::-1]

with open("Movies.txt", "w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
