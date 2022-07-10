from attr import attr
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status

soup = BeautifulSoup(res.text, "lxml")

print("\n\n")
a = soup.find("ol", attrs={"id" : "realTimeRankFavorite"})
print(a.get_text(), "\n")
print(a.find("li", attrs= {"class" : "rank02"}).get_text(), "\n")
print(a.find("li", attrs={"class": "rank02"}).find_next_sibling("li").get_text())