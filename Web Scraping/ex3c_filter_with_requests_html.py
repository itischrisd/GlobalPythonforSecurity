from requests_html import HTMLSession

session = HTMLSession()
req = session.get("https://www.hackeru.co.il")
all_links = req.html.links
print(all_links)
