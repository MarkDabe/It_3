import socket
import re
import time

host = "127.0.0.1"
port = 8080


for number in range(1, 11):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((host, port))

    buffer = s.recv(1024)

    print(buffer.decode('utf8'))

    s.send(bytes('ack:{}'.format(number), 'utf8'))

    if number == 2:
        s.close()
        time.sleep(2)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.send(bytes('ack:{}'.format(number), 'utf8'))

    if number == 3:
        s.close()
        time.sleep(2)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.send(bytes('ack:{}'.format(number), 'utf8'))

    if number == 3:
        s.close()
        time.sleep(2)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.send(bytes('ack:{}'.format(number), 'utf8'))


    s.close()