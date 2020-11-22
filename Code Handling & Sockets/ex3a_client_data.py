import socket

client_socket = socket.socket()
client_socket.connect(("192.168.56.1", 4444))
data = client_socket.recv(2048).decode()
print(data)
client_socket.close()
