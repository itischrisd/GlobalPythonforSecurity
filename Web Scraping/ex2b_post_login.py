import requests

url = "https://hack-yourself-first.com/Account/Login"
session = requests.session()
payload = {"Email": "wnerw.mail@gmail.com", "Password": "Zaq123wsxc"}
conn = session.post(url, data=payload)
print("Odpowiedź strony to: {}".format(conn.status_code))
if "Log off" in conn.text:
    print("True")
