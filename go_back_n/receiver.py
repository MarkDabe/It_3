import socket

host = "127.0.0.1"
port = 8080


packets = 0
sequence = -1

while 1:

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((host, port))

    buffer = s.recv(1024).decode('utf8')

    if int(buffer.split(":")[1]) - sequence == 1 and sequence < 4:
        print(buffer)
        s.send(bytes(buffer.replace('hello', 'ack'), 'utf8'))
        packets += 1
        sequence += 1
    elif int(buffer.split(":")[1]) - sequence == -4 and sequence == 4:
        print(buffer)
        s.send(bytes(buffer.replace('hello', 'ack'), 'utf8'))
        packets += 1
        sequence = 0
    else:
        s.send(bytes('ack:{}'.format(sequence), 'utf8'))

    s.close()

    if packets == 10:
        break


