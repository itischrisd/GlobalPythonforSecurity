import requests

request = requests.get("https://www.hackeru.co.il")
print("Odpoiwedź strony to {}".format(request.status_code))
print("Zawartość strony to \n \n {}".format(request.text))
