import requests
from bs4 import BeautifulSoup

session = requests.session()
request = requests.get("https://www.hackeru.co.il")
page_parser = BeautifulSoup(request.text, 'html.parser')

for search in page_parser.find_all('a'):
    try:
        link = search.get('href')
        if link.endswith(".pdf"):
            list1 = link.split("/")
            location = list1[len(list1)-1]
            print("Plik PDF: {}".format(link))
            print("Pobieranie...")
            file = open(r"C:\Users\wnerw\Desktop\pdfs\{}".format(location), "wb")
            file.write(requests.get(link).content)
            file.close()
        else:
            continue
    except Exception as error:
        print(error)
