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

    packets_list = list()

    packet_index = 0

    packets_counter = 0

    clientsocket, address = serversocket.accept()

    expected_acks = []

    ignore_3_once = False

    timeouts = {"ack:0": 0, "ack:1": 0, "ack:2": 0, "ack:3": 0, "ack:4": 0, "ack:5": 0, "ack:6": 0, "ack:7": 0, "ack:8": 0, "ack:9": 0,}

    while packets_counter < 10:

        time.sleep(1)

        for key, value in timeouts.items():
            if value != 0 and time.time() - value > 1:
                packets_list.append(key.replace("ack", "hello"))

        for number in range(packet_index, packet_index + 5):

            if number > 9:
                continue

            if len(packets_list) == 5 or (10 - packets_counter) - len(packets_list) + 1 < 0:
                break

            expected_acks.append("ack:{}".format(number))

            packets_list.append('hello:{}'.format(number))

            timeouts["ack:{}".format(number)] = time.time()

            if number == 3 and ignore_3_once:
                ignore_3_once = False
                packets_list.remove('hello:{}'.format(number))

        packets = " | ".join(packets_list)

        clientsocket.send(bytes(packets, 'utf8'))

        packets_list.clear()

        # print("packets sent: " + packets)

        buffer = clientsocket.recv(1024).decode('utf8')

        # print("acks received: " + buffer)

        acks = buffer.split(' | ')

        for ack in range(len(acks)):
            if acks[ack] in expected_acks:
                timeouts[acks[ack]] = 0
                packets_counter += 1
                if int(acks[ack].split(":")[1]) + 1 > packet_index:
                    packet_index = int(acks[ack].split(":")[1]) + 1
                # print("accepted ack: " + acks[ack])
                print(acks[ack])


    packets_counter = 0

