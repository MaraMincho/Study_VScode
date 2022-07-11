import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
url = "https://search.shopping.naver.com/search/all?query=%ED%8C%8C%EB%A7%88%EC%82%B0%20%EC%B9%98%EC%A6%88%EA%B0%80%EB%A3%A8&cat_id=&frm=NVSHATC"
res = requests.get(url, headers = headers)
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("a", attrs={"target" :"_blank"})
print(items)
print(type(items))