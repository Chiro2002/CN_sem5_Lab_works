import socket   
import time

def client(server_address, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((server_address, server_port))
    
    sequence_number = 0

    while True:
        message = f"{sequence_number}"
        client_socket.send(message.encode())
        response=client_socket.recv(1024).decode()

        if response=='ACK':
            print(f"ACK recieved for packet {sequence_number}.")
            sequence_number+=1
        else:
            print(f"NAK recieved for packet {sequence_number} .")
        
        time.sleep(5)


if __name__ == "__main__":
    server_address = '127.0.0.1'  # Replace with the server's IP address
    server_port = 12345  # Replace with the server's port
    client(server_address, server_port)
