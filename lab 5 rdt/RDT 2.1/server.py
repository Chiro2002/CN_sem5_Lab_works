import socket
import random
import time

CORRUPT_PACKET_THRESHOLD=0.65

def server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', port))
    server_socket.listen(1)

    print("Server is waiting ....")

    expected_rem=0

    while True:
        connection, client_address = server_socket.accept()
        print(f"Connected to {client_address}")

        while True:
            data = connection.recv(1024).decode()

            pkt_seq_number,rem=data.split(':')
            rem=int(rem)

            curr_pkt_corrupt_prob=random.random()
            if curr_pkt_corrupt_prob>CORRUPT_PACKET_THRESHOLD:
                print(f'Sending the NAK packet for sequence no {pkt_seq_number}.\n')
                time.sleep(2)
                connection.send('NAK'.encode())
            
            elif rem!=expected_rem:
                print(f'Recieved Packet no {pkt_seq_number}.Expected rem : {expected_rem} but recieved Rem : {rem}.\n')
                time.sleep(2)
                connection.send('ACK'.encode())

            else:
                print(f'Recieved Packet no {pkt_seq_number}.Expected rem : {expected_rem} and recieved Rem : {rem}.\n')
                time.sleep(2)
                connection.send('ACK'.encode())
                expected_rem=(expected_rem+1)%2


if __name__ == "__main__":
    server(12345)
