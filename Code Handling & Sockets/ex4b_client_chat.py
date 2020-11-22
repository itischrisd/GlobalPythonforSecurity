import socket

client_socket = socket.socket()
client_socket.connect(("192.168.56.1", 4444))
while True:
    try:
        server_data = client_socket.recv(2048).decode()
        message = input("Wiadomość do serwera: ")
        client_socket.send(message.encode())
        if message == "exit" or server_data == "exit":
            print("Zamykanie połączenia")
            client_socket.close()
            break
        else:
            print("Wiadomość z serwera: ", server_data)
    except Exception as error:
        if "ConnectionAbortedError" in error:
            print("Serwer zakończył połączenie")
