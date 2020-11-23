from datetime import datetime
import socket
import random


def roll(bet_number):
    random.seed(datetime.now())
    number = random.randint(0, 6)

    if number == int(bet_number):
        return ("Rolled number: " + str(number)
                + "\nYou win")
    else:
        return ("Rolled number: " + str(number)
                + "\nYou lose")


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('server', 10000)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)

sock.listen(1)
connection, client_address = sock.accept()
client_num = (connection.recv(128).decode())
print("Get number " + client_num)
connection.sendall(roll(int(client_num)).encode())
connection.close()
