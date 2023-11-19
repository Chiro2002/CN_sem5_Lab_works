import socket

def receiver():
    receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    receiver_socket.bind(('localhost', 12345))
    expected_seq_num = 0

    while True:
        data, sender_address = receiver_socket.recvfrom(1024)
        message = data.decode()

        seq_num, payload = message.split(':')
        seq_num = int(seq_num)

        if seq_num == expected_seq_num:
            print(f"Received: {payload}")
            receiver_socket.sendto(str(seq_num).encode(), sender_address)
            expected_seq_num += 1
        else:
            # Out-of-order packet, ignore and request retransmission of the expected packet
            receiver_socket.sendto(str(expected_seq_num - 1).encode(), sender_address)

if __name__ == "__main__":
    receiver()
