import socket
import time

host = "127.0.0.1"
port = 8080


packets_counter = 0
expected_sequence = 0


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

expected_packets = []

while packets_counter < 10:

    buffer = s.recv(1024).decode('utf8')

    # print("received packets: " + buffer)

    packets = buffer.split(' | ')

    ack_list = []

    for number in range(expected_sequence, expected_sequence + 5):
        expected_packets.append('hello:{}'.format(number))

    for packet in packets:
        if packet in expected_packets:
            # print("accepted packets: " + packet)
            print(packet)

            expected_packets.remove(packet)
            ack_list.append(packet.replace('hello', 'ack'))
            packets_counter += 1
            expected_sequence += 1

    acks = " | ".join(ack_list)

    # print("sent acks: " + acks)

    s.send(bytes(acks, 'utf8'))

    ack_list.clear()

    time.sleep(1)

s.close()





