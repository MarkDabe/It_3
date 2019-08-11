import socket
import time

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 8080

serversocket.bind((host, port))
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

serversocket.listen(5)
print('Sender ready and is listening for receiver to connect')

while 1:

    for number in range(0, 10):
        give_up = False

        clientsocket, address = serversocket.accept()

        clientsocket.send(bytes('hello:{}'.format(number), 'utf8'))

        buffer = clientsocket.recv(1024).decode('utf8')

        print(buffer)

        start = time.time()

        while buffer != "ack:{}".format(number):
            time.sleep(1)
            clientsocket.close()
            clientsocket, address = serversocket.accept()
            clientsocket.send(bytes('hello:{}'.format(number), 'utf8'))
            buffer = clientsocket.recv(1024).decode('utf8')

        clientsocket.close()