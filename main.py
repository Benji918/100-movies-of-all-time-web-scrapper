from bs4 import BeautifulSoup
import requests

# Write your code below this line 👇
response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best"
                        "-movies-2/")
soup = BeautifulSoup(response.text, 'html.parser')
# select the tags with the h3 tag in the website
titles = soup.select('h3')

movies = [movie.getText() for movie in titles]
movies_list = movies[::-1]

with open('movies.txt', mode='w', encoding="utf-8") as movies_file:
    for movie in movies_list:
        movies_file.write(movie)
        movies_file.write('\n')





