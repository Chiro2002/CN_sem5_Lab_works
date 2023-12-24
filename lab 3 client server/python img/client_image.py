import socket
import sys

def main(server_ip, server_port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, server_port))

    with open("image.jpg", "rb") as file:
        data = file.read(1024)
        while data:
            client.send(data)
            data = file.read(1024)

    client.close()

# ip=127.0.0.0 port= 9998 or 1234

server_ip = sys.argv[1]
server_port = int(sys.argv[2])
main(server_ip, server_port)
