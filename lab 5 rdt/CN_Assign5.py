import socket

def sender(message, host, port):
    # Create a UDP socket
    sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    for i in range(len(message)):
        packet = str(i) + '|' + message[i]
        sender_socket.sendto(packet.encode(), (host, port))

    sender_socket.close()

def receiver(host, port, message_length):
    # Create a UDP socket
    receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    receiver_socket.bind((host, port))

    received_message = [''] * message_length

    while True:
        data, addr = receiver_socket.recvfrom(1024)
        packet = data.decode()
        seq_num, packet_data = packet.split('|')
        seq_num = int(seq_num)
        received_message[seq_num] = packet_data

        if None not in received_message:
            break

    receiver_socket.close()

    return ''.join(received_message)

if __name__ == "__main__":
    # Sender
    message = "Hello, this is a test message."
    host = "localhost"
    port = 12345

    sender(message, host, port)

    # Receiver
    received_message = receiver(host, port, len(message))
    print("Received message:", received_message)

    import socket


    def sender(message, host, port):
        sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        seq_num = 0

        for i in range(len(message)):
            packet = str(seq_num) + '|' + message[i]
            sender_socket.sendto(packet.encode(), (host, port))

            ack_received = False
            while not ack_received:
                try:
                    sender_socket.settimeout(1.0)  # Set a timeout for receiving acknowledgments
                    ack_data, addr = sender_socket.recvfrom(1024)
                    ack = ack_data.decode()
                    ack_seq_num = int(ack.split('|')[0])

                    if ack_seq_num == seq_num:
                        ack_received = True
                    else:
                        continue
                except socket.timeout:
                    print("Timeout, resending packet", seq_num)
                    continue

            seq_num = 1 - seq_num  # Toggle sequence number

        sender_socket.close()


    def receiver(host, port, message_length):
        receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        receiver_socket.bind((host, port))

        received_message = [''] * message_length
        expected_seq_num = 0

        while None in received_message:
            data, addr = receiver_socket.recvfrom(1024)
            packet = data.decode()
            seq_num, packet_data = packet.split('|')
            seq_num = int(seq_num)

            if seq_num == expected_seq_num:
                received_message[seq_num] = packet_data
                expected_seq_num = 1 - expected_seq_num  # Toggle expected sequence number

                # Send acknowledgment
                ack = str(seq_num)
                receiver_socket.sendto(ack.encode(), addr)

        receiver_socket.close()

        return ''.join(received_message)


    if __name__ == "__main__":
        message = "Hello, this is a test message."
        host = "localhost"
        port = 12345

        sender(message, host, port)

        received_message = receiver(host, port, len(message))
        print("Received message:", received_message)

import socket

def sender(message, host, port):
    sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    window_size = 4
    seq_num = 0
    receiver_window = [None] * window_size

    def send_packet(seq_num):
        if seq_num < len(message):
            packet = str(seq_num) + '|' + message[seq_num]
            sender_socket.sendto(packet.encode(), (host, port))
            receiver_window[seq_num % window_size] = packet

    for i in range(window_size):
        send_packet(seq_num)
        seq_num += 1

    while None in receiver_window:
        try:
            sender_socket.settimeout(1.0)
            ack_data, addr = sender_socket.recvfrom(1024)
            ack = ack_data.decode()
            ack_seq_num = int(ack.split('|')[0])

            if receiver_window[ack_seq_num % window_size]:
                sender_socket.sendto(receiver_window[ack_seq_num % window_size].encode(), (host, port))
                receiver_window[ack_seq_num % window_size] = None
                send_packet(seq_num)
                seq_num += 1
        except socket.timeout:
            pass

    sender_socket.close()

def receiver(host, port, message_length):
    receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    receiver_socket.bind((host, port))

    received_message = [''] * message_length

    while None in received_message:
        try:
            receiver_socket.settimeout(1.0)
            data, addr = receiver_socket.recvfrom(1024)
            packet = data.decode()
            seq_num, packet_data = packet.split('|')
            seq_num = int(seq_num)

            if received_message[seq_num] == '':
                received_message[seq_num] = packet_data
                # Send acknowledgment
                ack = str(seq_num)
                receiver_socket.sendto(ack.encode(), addr)
        except socket.timeout:
            pass

    receiver_socket.close()

    return ''.join(received_message)

if __name__ == "__main__":
    message = "Hello, this is a test message."
    host = "localhost"
    port = 12345

    sender(message, host, port)

    received_message = receiver(host, port, len(message))
    print("Received message:", received_message)

