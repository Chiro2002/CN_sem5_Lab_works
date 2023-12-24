import socket
import random
import time

CORRUPT_PACKET_THRESHOLD = 0.65


def server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', port))
    server_socket.listen(1)

    print("Server is waiting ....")

    curr_state = 0
    client_reponse = ''

    while True:
        connection, client_address = server_socket.accept()
        print(f"Connected to {client_address}\n\n")

        while True:
            if curr_state == 0:
                client_reponse = connection.recv(1024).decode()

                pkt_seq_number, mod_val = client_reponse.split(':')
                mod_val = int(mod_val)

                curr_pkt_corrupt_prob = random.random()
                if curr_pkt_corrupt_prob > CORRUPT_PACKET_THRESHOLD:
                    print(
                        f'Recived corrupted packet.\nSending the ACK-1 packet for sequence number {pkt_seq_number}.\n')
                    connection.send('ACK-1'.encode())

                elif mod_val == 1:
                    print(
                        f'Recived mod_val 1 but expected mod_val 0.\nSending the ACK-1 packet for sequence number{pkt_seq_number}.\n')
                    connection.send('ACK-1'.encode())

                else:
                    print(
                        f'Recived mod_val 0 and expected mod_val 0.\nSending the ACK-0 packet for sequence number{pkt_seq_number}.\n')
                    connection.send('ACK-0'.encode())
                    curr_state += 1

            elif curr_state == 1:
                client_reponse = connection.recv(1024).decode()

                pkt_seq_number, mod_val = client_reponse.split(':')
                mod_val = int(mod_val)

                curr_pkt_corrupt_prob = random.random()
                if curr_pkt_corrupt_prob > CORRUPT_PACKET_THRESHOLD:
                    print(
                        f'Recived corrupted packet.\nSending the ACK-0 packet for sequence number {pkt_seq_number}.\n')
                    connection.send('ACK-0'.encode())

                elif mod_val == 0:
                    print(
                        f'Recived mod_val 0 but expected mod_val 1.\nSending the ACK-0 packet for sequence number{pkt_seq_number}.\n')
                    connection.send('ACK-0'.encode())

                else:
                    print(
                        f'Recived mod_val 1 and expected mod_val 1.\nSending the ACK-1 packet for sequence number{pkt_seq_number}.\n')
                    connection.send('ACK-1'.encode())
                    curr_state = 0

            time.sleep(5)


if __name__ == "__main__":
    server(12345)
