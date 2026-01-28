#chat app using sockets.py
import socket
import threading
import sys
import select
HOST = '127.0.0.1'  # Localhost IP address
PORT = 12345  # Port number for the server
def handle_client(client_socket, clients):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Received: {message}")
                broadcast(message, client_socket, clients)
            else:
                remove_client(client_socket, clients)
                break
        except:
            continue
def broadcast(message, sender_socket, clients):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                remove_client(client, clients)
def remove_client(client_socket, clients):
    if client_socket in clients:
        clients.remove(client_socket)
        client_socket.close()
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Server started on {HOST}:{PORT}")
    clients = []
    while True:
        client_socket, addr = server.accept()
        print(f"New connection from {addr}")
        clients.append(client_socket)
        client_handler = threading.Thread(target=handle_client, args=(client_socket, clients))
        client_handler.start()
def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    print(f"Connected to server at {HOST}:{PORT}")
    def receive_messages():
        while True:
            try:
                message = client.recv(1024).decode('utf-8')
                if message:
                    print(f"\n{message}\n> ", end='', flush=True)
            except:
                print("Connection closed by the server.")
                break
    threading.Thread(target=receive_messages, daemon=True).start()
    while True:
        message = input("> ")
        if message.lower() == 'exit':
            break
        client.send(message.encode('utf-8'))
    client.close()
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python chat_app.py [server|client]")
        sys.exit(1)
    if sys.argv[1] == 'server':
        start_server()
    elif sys.argv[1] == 'client':
        start_client()
    else:
        print("Invalid argument. Use 'server' or 'client'.")
        sys.exit(1)
        