import socket

this_socket = socket.socket()
this_socket.bind(("0.0.0.0", 1424))
this_socket.listen(1)
conn, addr = this_socket.accept()
this_socket.close()
