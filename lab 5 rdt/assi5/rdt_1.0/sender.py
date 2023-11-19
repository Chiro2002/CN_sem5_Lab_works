import socket
import time

def sender():
    sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    receiver_address = ('localhost', 12345)
    message = "Hello, Receiver!"
    
    while True:
        sender_socket.sendto(message.encode(), receiver_address)
        print("Sent:", message)
        
        # Wait for acknowledgment
        sender_socket.settimeout(2)  # Set a timeout for acknowledgment reception
        try:
            ack, _ = sender_socket.recvfrom(1024)
            if ack.decode() == "ACK":
                print("Received ACK")
                break
        except socket.timeout:
            print("Timeout, no ACK received. Resending...")

    sender_socket.close()

if __name__ == "__main__":
    sender()
