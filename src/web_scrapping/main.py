from bs4 import BeautifulSoup
import requests
import os
import sys

# BeautifulSoup documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

def file_path(rel_path):
  return os.path.join(sys.path[0], rel_path)




url = 'https://www.timeout.com/film/best-movies-of-all-time'
# url = 'https://www.empireonline.com/movies/features/best-movies-2/'
response = requests.get(url)
# print(response.content)
soup = BeautifulSoup(response.content, "html.parser")
print(soup.title)


def has_span(tag):
  return tag.name == 'h3' and tag.find('span')

# tags = soup.findAll(class_="listicle-item")
# print(tags[0])
titles = soup.find_all(has_span)

print(titles[0].get_text())
# titles = [span.find("a").get_text() for span in tags]

titles_list = [tag.get_text().split('.\xa0',1) for tag in titles]
print(titles_list)


with open("movies.txt", "w") as f:
  for movie in titles_list:
    f.write(", ".join(movie)+'\n')
#
# url ='https://news.ycombinator.com/news'
# response = requests.get(url)
# # print(response.content)
# soup = BeautifulSoup(response.content, "html.parser")
# # print(soup.title)
#
# def get_score(span):
#   score_class = span.find(class_="score")
#   if score_class:
#     return int(score_class.get_text().split(' ')[0])
#   else:
#     return 0
#
# tags = soup.findAll(class_="titleline")
# titles = [span.find("a").get_text() for span in tags]
# urls = [span.find("a").get("href") for span in tags]
# votes = [get_score(span) for span in soup.findAll(class_="subline")]
# list_of_tuples = list(zip(titles, urls, votes))
# sorted_list = sorted(list_of_tuples, key=lambda x: x[2], reverse=True)
# print(sorted_list)











# with open(file_path("website.html"), 'r', encoding='utf-8') as f:
#     content = f.read()
#
# soup = BeautifulSoup(content, 'html.parser')
# # print(soup.prettify())
# print(soup.title)
#
# anchors = soup.findAll('a')
# for a in anchors:
#     print(a.getText())
#     print(a.get("href"))
#
# test = soup.findAll(attrs={'something':True})
# print(test)
#
# heading = soup.select(".heading")
# print(heading)
#
# print(soup.find('h1').get("something"))
#
#
