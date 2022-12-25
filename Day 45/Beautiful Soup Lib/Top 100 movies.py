from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")
titles = soup.find_all(class_="title", name="h3")
# print(titles)

movie_titles = [movie.getText() for movie in titles]
movies = movie_titles[::-1]

with open("movies.txt", mode="w", encoding="utf8") as file:
    for movie in movies:
        file.write(f"{movie}\n")

