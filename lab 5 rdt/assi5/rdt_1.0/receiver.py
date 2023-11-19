import socket

def receiver():
    receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    receiver_socket.bind(('localhost', 12345))
    
    while True:
        data, sender_address = receiver_socket.recvfrom(1024)
        print("Received:", data.decode())
        
        # Send acknowledgment
        receiver_socket.sendto("ACK".encode(), sender_address)
        print("Sent ACK")
        
        if data.decode() == "Hello, Receiver!":
            break

    receiver_socket.close()

if __name__ == "__main__":
    receiver()
