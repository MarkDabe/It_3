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

    print("received packets: " + buffer)

    packets = buffer.split(' | ')

    expected_packets = []

    acks = ""

    for number in range(expected_sequence, expected_sequence + 5):
        expected_packets.append('hello:{}'.format(number % 5))

    for packet in packets:
        if packet in expected_packets:
            print("accepted packets: " + packet)
            acks = acks + packet.replace('hello', 'ack') + ' | '
            packets_counter += 1
            expected_sequence += 1


    print("sent acks: " + acks)

    s.send(bytes(acks, 'utf8'))

    expected_packets = []

    time.sleep(1)

s.close()





