import socket
import random
import time

CORRUPT_PACKET_THRESHOLD = 0.65

def client_fun(server_address, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((server_address, server_port))
    
    curr_state = 0
    sequence_number = 0

    server_response = ''

    while True:
        if curr_state == 0:
            message = str(sequence_number)+':'+str(sequence_number % 2)
            timeout=False
            print(f'Sending Packet with sequence number {sequence_number}.\n')
            client_socket.send(message.encode())
            server_response = client_socket.recv(1024).decode()
            curr_state += 1

        elif curr_state == 1:
            curr_pkt_corrupt_prob = random.random()

            if curr_pkt_corrupt_prob > CORRUPT_PACKET_THRESHOLD:
                print(
                    f'Corrupted Packet for sequence number {sequence_number} recieved from server.\n')
                timeout=True

            elif server_response == 'ACK-1':
                print(f'ACK-1 recieved from server but expected was ACK-0.\n')
                timeout=True

            elif server_response=='ACK-0':
                print(f'ACK-0 recieved from server and expected was ACK-0.\n')
                curr_state += 1
                sequence_number += 1
            
            if timeout==True:
                print(
                    f'Timeout for packet with sequence number {sequence_number}.Resending the packet.\n')
                print(
                    f'Sending Packet with sequence number {sequence_number}.\n')
                
                timeout=False
                client_socket.send(message.encode())
                server_response = client_socket.recv(1024).decode()

        elif curr_state == 2:
            message = str(sequence_number)+':'+str(sequence_number % 2)
            timeout=False
            print(f'Sending Packet with sequence number {sequence_number}.\n')
            client_socket.send(message.encode())
            server_response = client_socket.recv(1024).decode()
            curr_state += 1

        elif curr_state == 3:
            curr_pkt_corrupt_prob = random.random()

            if curr_pkt_corrupt_prob > CORRUPT_PACKET_THRESHOLD:
                print(
                    f'Corrupted Packet for sequence number {sequence_number} recieved from server.\n')
                timeout=True

            elif server_response == 'ACK-0':
                print(f'ACK-0 recieved from server but expected was ACK-1.\n')
                timeout=True
                

            elif server_response=='ACK-1':
                print(f'ACK-1 recieved from server and expected was ACK-1.\n')
                curr_state = 0
                sequence_number += 1
            
            if timeout==True:
                print(
                    f'Timeout for packet with sequence number {sequence_number}.Resending the packet.\n')
                print(
                    f'Sending Packet with sequence number {sequence_number}.\n')
                
                timeout=False
                client_socket.send(message.encode())
                server_response = client_socket.recv(1024).decode()

        time.sleep(7)


if __name__ == '__main__':
    server_address = '127.0.0.1'
    server_port = 12345
    client_fun(server_address, server_port)
