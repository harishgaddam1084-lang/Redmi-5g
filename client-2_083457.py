import socket
from threading import Thread
from cryptography.fernet import Fernet
c = socket.socket()
c.connect(("localhost", 9996))
key = Fernet.generate_key()
s_key = c.recv(1024)
print("The key received from server:", s_key)
c.send(key)
print("The key is sent to server:", key)

def receiving():
    while True:
        try:
            text = c.recv(1024)
            print("Encrypted message from server:", text)
            print(" ")
            decrypted = Fernet(s_key).decrypt(text).decode()
            print("Decrypted message from server:", decrypted)
            print(" ")
        except Exception as e:
            print("Error in receiving:", e)
            break

def sending():
    while True:
        msg = input("Client: ")
        encrypted = Fernet(key).encrypt(msg.encode())
        c.send(encrypted)
        print("Encrypted message sent to server:", encrypted)
        print(" ")


Thread(target=receiving).start()
Thread(target=sending).start()
