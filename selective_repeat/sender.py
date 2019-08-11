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

    clientsocket, address = serversocket.accept()

    while packets_counter < 10:

        time.sleep(1)

        expected_acks = []

        packets = ""

        timeouts = {}

        for number in range(packets_counter, packets_counter + 5):
            expected_acks.append("ack:{}".format(number % 5))

            packets = packets + 'hello:{}'.format(number % 5)

            timeouts["ack:{}".format(number % 5)] = time.time()

            if number < packets_counter + 4:
                packets = packets + ' | '

        clientsocket.send(bytes(packets, 'utf8'))

        print("packets sent: " + packets)

        buffer = clientsocket.recv(1024).decode('utf8')

        print("acks received: " + buffer)

        acks = buffer.split(' | ')

        acks.remove('')

        acks = list(dict.fromkeys(acks))

        for ack in range(len(acks)):
            if acks[ack] in expected_acks and time.time() - timeouts[acks[ack]] < 10:
                packets_counter += 1
                print("accepted ack: " + acks[ack])
            else:
                break

    packets_counter = 0

