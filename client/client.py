from datetime import datetime
import socket
import random

random.seed(datetime.now())
number = random.randint(0, 6)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('server', 10000)
print('connecting to %s port %s' % server_address)
sock.connect(server_address)

sock.sendall(str(number).encode())
data = sock.recv(128).decode()
print('received "%s"' % data, end='\n')

sock.close()
