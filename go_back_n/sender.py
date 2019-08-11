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

    packets_counter = 0
    packets = ""

    for number in range(packets_counter, packets_counter + 5):
        clientsocket, address = serversocket.accept()

        clientsocket.send(bytes('hello:{}'.format(number % 5), 'utf8'))

        buffer = clientsocket.recv(1024).decode('utf8')

        if buffer == "ack:{}".format(number % 5):
            packets_counter += 1
            print(buffer)

        if packets_counter == 10:
            break

        clientsocket.close()

