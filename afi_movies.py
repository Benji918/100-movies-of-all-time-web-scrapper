from bs4 import BeautifulSoup
import requests
URL = "https://www.afi.com/afis-100-years-100-movies/"

# Write your code below this line 👇
response = requests.get("https://web.archive.org/web/20200518073855/https://www.afi.com/afis-100-years-100-movies/")
soup = BeautifulSoup(response.text, 'html.parser')
movie_titles = soup.find_all(name='h6', class_="q_title")
movie_list = [movie.getText() for movie in movie_titles][:100]

print(movie_list)

with open('afi_movie.txt', mode='w',  encoding="utf-8") as movie_file:
    for movie in movie_list:
        movie_file.write(movie)
        movie_file.write('\n')