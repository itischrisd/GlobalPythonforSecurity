import urllib3

conn = urllib3.PoolManager()
req = conn.request("GET", "https://www.hackeru.co.il")
print("Odpowiedź strony to {}".format(req.status))
print("Zawartość strony to \n \n {}".format(req.data))
