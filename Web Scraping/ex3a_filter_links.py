import requests
from bs4 import BeautifulSoup

url = "https://www.hackeru.co.il"
req = requests.get(url)
page_parse = BeautifulSoup(req.text, "html.parser")

for search in page_parse.find_all('a'):
    link = search.get('href')
    if link.startswith("https://"):
        print(link)
    else:
        continue
