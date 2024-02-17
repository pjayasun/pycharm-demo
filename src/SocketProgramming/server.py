import socket

import socket

ss=socket.socket()
print("Socket created")

ss.bind(('localhost', 9999))
print("Waiting for connections")

# Number of connections
ss.listen(3)

while True:
    cs, addr = ss.accept()
    name = cs.recv(4096).decode()
    print("Connected with client: ", addr, name)

    cs.send(bytes("Welcome "+name, "utf-8"))

    cs.close()