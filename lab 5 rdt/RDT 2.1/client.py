import socket
import random
import time

CORRUPT_PACKET_THRESHOLD=0.65

def client_fun(server_address, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((server_address, server_port))
    
    sequence_number = 0

    while True:
        message=str(sequence_number)+':'+str(sequence_number%2)
        print(f'Sending Packet with sequence no {sequence_number}.')
        client_socket.send(message.encode())
        response=client_socket.recv(1024).decode()

        curr_pkt_corrupt_prob=random.random()
        if curr_pkt_corrupt_prob>CORRUPT_PACKET_THRESHOLD:
            print(f'Corrupted Packet for sequence no {sequence_number} recieved from server.Resending the packet with sequence no {sequence_number}.\n')
            
        elif response=='NAK':
            print(f'NAK Packet for sequence no {sequence_number} recieved from server.Resending the packet with sequence no {sequence_number}.\n')

        else:
            print(f'ACK Packet for sequence no {sequence_number} recieved from server.\n')
            sequence_number+=1
        
        time.sleep(10)
        

if __name__=='__main__':
    server_address='127.0.0.1'
    server_port=12345
    client_fun(server_address,server_port)