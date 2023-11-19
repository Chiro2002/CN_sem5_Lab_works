import socket
import threading

server_running = True

def handle_client(client_socket):
    with open("received_image.jpg", "wb") as file:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            file.write(data)

    print("Client disconnected")
    client_socket.close()

def main():
    global server_running

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 9998))
    server.listen(5)

    print("Server Listening on port 9998...")

    while server_running:
        client_sock, addr = server.accept()
        print(f"Accepted connection from {addr[0]}:{addr[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client_sock,))
        client_handler.start()

    server.close()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nServer shutting down...")
        server_running = False
