import requests
from bs4 import BeautifulSoup

def get_soup(date='2020-10-20'):
  url = 'https://www.billboard.com/charts/hot-100/'
  response = requests.get(url+date)
  # print(response.content)
  return BeautifulSoup(response.content, "html.parser")
  # print(soup.title)

if __name__ == '__main__':
  date = '2005-05-13'
  get_soup(date)