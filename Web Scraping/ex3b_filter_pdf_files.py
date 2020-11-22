import requests
from bs4 import BeautifulSoup

url = "https://www.hackeru.co.il"
req = requests.get(url)
page_parse = BeautifulSoup(req.text, "html.parser")

for search in page_parse.find_all('a'):
    link = search.get('href')
    if link.endswith(".pdf"):
        print("Plik PDF: {}".format(link))
    else:
        continue
