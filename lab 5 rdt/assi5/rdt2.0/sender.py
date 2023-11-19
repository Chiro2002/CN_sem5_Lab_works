import socket
import time

def sender():
    sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    receiver_address = ('localhost', 12345)
    message = "Hello, Receiver!"
    window_size = 4
    base = 0
    next_seq_num = 0
    packets = []

    while base < len(message):
        # Send packets within the window
        for i in range(next_seq_num, min(base + window_size, len(message))):
            packet = f"{next_seq_num}:{message[i]}"
            sender_socket.sendto(packet.encode(), receiver_address)
            print(f"Sent: {packet}")
            packets.append(packet)
            next_seq_num += 1

        # Receive acknowledgments
        try:
            sender_socket.settimeout(2)  # Timeout for acknowledgments
            ack, _ = sender_socket.recvfrom(1024)
            ack_num = int(ack.decode())
            print(f"Received ACK: {ack_num}")

            if ack_num >= base:
                # Slide the window
                while base <= ack_num:
                    packets.pop(0)
                    base += 1
        except socket.timeout:
            # Timeout, retransmit the packets in the window
            print("Timeout, retransmitting...")
            for packet in packets:
                seq_num, payload = packet.split(':')
                sender_socket.sendto(packet.encode(), receiver_address)
                print(f"Sent: {packet}")

    sender_socket.close()

if __name__ == "__main__":
    sender()
