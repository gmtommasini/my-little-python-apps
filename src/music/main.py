from bs4 import BeautifulSoup
import requests
from track import Track
from sptfy import search_song, create_playlist
import traceback

url = 'https://www.billboard.com/charts/hot-100/'
date = '2005-05-13'
# date =  input("What's the date?")
response = requests.get(url+date)
# print(response.content)
soup = BeautifulSoup(response.content, "html.parser")
# print(soup.title)

title_tags = soup.select("li ul li h3")
artist_tags = soup.select("li ul li h3 + span")

art_track = [(a.get_text().strip(),t.get_text().strip()) for  (a,t) in zip(artist_tags, title_tags)]


# playlist:Track = { search_song(name=a_t[1], artist=a_t[0], year=date.split("-")[0]) for a_t in art_track}
# testing = ('Gwen Stefani', 'Hollaback Girl')
# track = search_song(name=testing[1], 
#                     artist=testing[0], 
#                     year=date.split("-")[0])


for a_t in art_track:
  print(a_t)
  try:
    track = search_song(name=a_t[1], artist=a_t[0], year=date.split("-")[0])
    print("THIS TRACK:\n",track)
  except Exception:
    print("Error on: ", a_t )
    traceback.print_exc()
  break
  
  
# print(playlist)


