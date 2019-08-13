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

    packet_index = 0

    clientsocket, address = serversocket.accept()

    packets_list = []

    ignore_3_once = False

    expected_acks = []

    while packets_counter < 10:

        time.sleep(1)

        for number in range(packet_index, packet_index + 5):

            if number > 9:
                continue

            if len(packets_list) == 5 or (10 - packets_counter) - len(packets_list) + 1 < 0:
                break

            expected_acks.append("ack:{}".format(number))

            packets_list.append('hello:{}'.format(number))

            if number == 3 and ignore_3_once:
                ignore_3_once = False
                packets_list.remove('hello:{}'.format(number))

        packets = " | ".join(packets_list)

        clientsocket.send(bytes(packets, 'utf8'))

        packets_list.clear()

        print("packets sent: " + packets)

        buffer = clientsocket.recv(1024).decode('utf8')

        # print("acks received: " + buffer)

        ack = buffer.split(":")

        # print("acks accepted: " + buffer)

        print(buffer)


        packets_counter += (int(ack[1]) % 5) + 1

        packet_index =  int(ack[1]) + 1

        # acks = buffer.split(' ')
        #
        # acks.remove('')
        #
        # acks = list(dict.fromkeys(acks))

        # for ack in range(len(acks)):
        #     if acks[ack] in expected_acks:
        #         packets_counter += 1
        #         print(acks[ack])


    packets_counter = 0

