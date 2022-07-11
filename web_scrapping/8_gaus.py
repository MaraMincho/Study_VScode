import requests
import statistics
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=675554"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")


#평점 정보 구하기
# cartoons = soup.find_all("td", attrs = {"class" : "title"})
# title2 = cartoons[1].a.get_text()
# link = cartoons[0].a["href"]
# print(title2, "\n", link)
# for cartoon in cartoons : 
#   title = cartoon.a.get_text()
#   link = "https://comic.naver.com" + cartoon.a["href"]
#   print(title, link)

import numpy as np
rate = []
cartoons  = soup.find_all("div", attrs = {"class" : "rating_type"})
for cartoon in cartoons :
  temp = cartoon.find("strong").get_text()
  rate.append(float(temp))
  print(temp)

print(statistics.mean(rate))
print(np.mean(rate))