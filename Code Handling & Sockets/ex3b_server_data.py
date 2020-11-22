import socket

server_socket = socket.socket()
server_socket.bind(("0.0.0.0", 4444))
server_socket.listen(1)
conn, addr = server_socket.accept()
conn.send("Hello World!".encode())
server_socket.close()
