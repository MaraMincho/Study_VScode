import requests

res = requests.get("http://google.com")
print(res.status_code)

res.raise_for_status()
print("실행.")

print(len(res.text))
print("trackted")
with open("mygoogle.html", "w", encoding = "utf8") as f :
  f.write(res.text)