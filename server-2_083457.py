import os
os.environ['CRYPTOGRAPHY_OPENSSL_NO_LEGACY'] = '1'

import socket
from threading import Thread
from cryptography.fernet import Fernet

server_socket = socket.socket()
print("Socket created")
server_socket.bind(("localhost", 9996)) 
server_socket.listen(3)
print("Waiting for connections...")

def handle_client(client_socket, addr, server_key, client_key):
    print(f"Handling client {addr}")
    
    decryptor = Fernet(client_key)  
    encryptor = Fernet(server_key)  

    def receiving():
        while True:
            try:
                encrypted = client_socket.recv(1024)
                if not encrypted:
                    break
                print("Received encrypted message from client:", encrypted)
                print(" ")
                decrypted = decryptor.decrypt(encrypted).decode()
                print("Decrypted client message:", decrypted)
                print(" ")
            except Exception as e:
                print("Receiving error:", e)
                break

    def sending():
        while True:
            try:
                msg = input("Server: ")
                if msg.lower() == "exit":
                    client_socket.close()
                    break
                encrypted_msg = encryptor.encrypt(msg.encode())
                client_socket.send(encrypted_msg)
                print("Encrypted message from server sent:", encrypted_msg)
                print(" ")
            except Exception as e:
                print("Sending error:", e)
                break

    Thread(target=receiving).start()
    Thread(target=sending).start()

def accepting():
    while True:
        client_socket, addr = server_socket.accept()
        print("Connected with", addr)

        server_key = Fernet.generate_key()
        client_socket.send(server_key)
        print("Server key sent to client:", server_key.decode())

        client_key = client_socket.recv(1024)
        print("Client key received:", client_key.decode())
        print(" ")

        Thread(target=handle_client, args=(client_socket, addr, server_key, client_key)).start()


accepting_thread = Thread(target=accepting)
accepting_thread.start()
