class Track:
  def __init__(self, name:str, artist:str, spotify_id:str, preview_url:str):
      self.spotify_id = spotify_id
      self.name = name
      self.artist = artist
      self.preview_url = preview_url

  def get_name(self):
      return self.name

  def get_artist(self):
      return self.artist

  def get_id(self):
      return self.spotify_id
    
  def get_preview_url(self):
      return self.preview_url
  
#   Overriding original string method
  def __str__(self):
    string = f"""{{
    track name: {self.name}
    artist: {self.artist}
    spotify track id: {self.spotify_id}
    spotify preview url: {self.preview_url}
}}"""
    return string

if __name__ == '__main__':
  print(Track("Song", "Cantor", "12ikhj3bvp12iuh3b", "URL"))