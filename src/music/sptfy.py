import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_TOKEN
from track import Track

# SPOTITY documentation:
# https://spotipy.readthedocs.io/en/2.22.1/
# https://spotipy.readthedocs.io/en/2.22.1/#api-reference

redirect_uri = 'http://example.com'
# redirect_uri = 'https://gmtommasini.github.io/my-page/'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(   client_id=SPOTIFY_CLIENT_ID,
                                                  client_secret=SPOTIFY_CLIENT_TOKEN,
                                                  redirect_uri=redirect_uri,
                                                  scope="playlist-modify-private,playlist-modify-public"))
def get_me():
     return sp.me()['id']
USER_ID = get_me()


def create_playlist(user_id, list_name, tracks=None)->str:
     """Creates a Playlist for the user and return the list ID"""
     resp = sp.user_playlist_create(user=user_id, name=list_name)
     list_id = resp['id']
     # print(list_id)
     if tracks:
          add_tracks(user_id=user_id, playlist_id=list_id)
     return list_id


def add_tracks(user_id, list_id, tracks):
     sp.user_playlist_add_tracks(user_id, list_id, tracks, position=None)

def search_song(name:str=None, artist:str=None, year:str=None )->Track:
     # print(name, artist, year)
     query = ""
     if name:
          query+= f"track:{name} " 
     if artist:
          query+= f"artist:{artist} "
     if year:
          query+= f"year:{year} "
     print(query)
     try:
          resp = sp.search(q=query.strip(), type="track")
          first_item=resp['tracks']['items'][0]
          print("SEARCH RESP:\n",resp)
          return Track(  spotify_id=first_item['id'], 
                         name=first_item['name'], 
                         artist=first_item['artists'][0]['name'], 
                         preview_url=first_item['preview_url']   )
     except IndexError as e:
          print("INDEX ERROR:\n",e)

# search_song(artist="Michael Jackson", year="1972")

if __name__ == '__main__':
     print("RUNNING A TEST...")
     # create_playlist(USER_ID, "Test List")
     # print( search_song(name="Hate It Or Love It", year="2005"))
     testing = ('Gwen Stefani', 'Hollaback Girl')
     track = search_song(name=testing[1], 
                    artist=testing[0], 
                    year="2005"
                    )
     print(track)
  