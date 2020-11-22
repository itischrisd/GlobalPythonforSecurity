import socket

target = input("Podaj cel: ")
name = socket.gethostbyname(target)

while True:
    try:
        s = socket.socket()
        port = int(input("Wprowadź port do zeskanowania: "))
        s.connect((target, port))
        s.send("Co to za usługa?".encode())
        ret = s.recv(1024).decode()
        print("[+] " "Usługa to {}".format(ret))
        s.close()
    except:
        print("Ten port jest zamknięty.")
