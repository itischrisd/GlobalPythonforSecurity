import socket
import time

this_socket = socket.socket()
this_socket.connect(("192.168.56.1", 1424))
time.sleep(30)
this_socket.close()
