import socket
import time

host = "127.0.0.1"
port = 8080


packets_counter = 0
expected_sequence = 0


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

while packets_counter < 10:

    buffer = s.recv(1024).decode('utf8')

    packets = buffer.split(' | ')

    for packet in packets:
        if int(packet.split(":")[1]) == expected_sequence and expected_sequence < 4:
            print(packet)
            s.send(bytes(packet.replace('hello', 'ack') + ' ', 'utf8'))
            packets_counter += 1
            expected_sequence += 1
        elif int(packet.split(":")[1]) == expected_sequence and expected_sequence == 4:
            print(packet)
            s.send(bytes(packet.replace('hello', 'ack') + ' ', 'utf8'))
            packets_counter += 1
            expected_sequence = 0
        else:
            s.send(bytes('ack:{}'.format(expected_sequence) + ' ', 'utf8'))

    time.sleep(1)

s.close()





