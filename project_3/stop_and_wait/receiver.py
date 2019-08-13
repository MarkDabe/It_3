import socket


host = "127.0.0.1"
port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

for number in range(0, 10):

    buffer = s.recv(1024)

    print(buffer.decode('utf8'))

    s.send(bytes('ack:{}'.format(number), 'utf8'))

s.close()