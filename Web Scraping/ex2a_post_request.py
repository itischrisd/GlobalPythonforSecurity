import requests

conn = requests.post("https://www.hackeru.co.il")
print("Odpoiwedź strony to {}".format(conn.status_code))
print("Zawartość strony to \n \n {}".format(conn.text))
