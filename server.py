import os
os.environ['CRYPTOGRAPHY_OPENSSL_NO_LEGACY'] = '1'

import socket
from threading import Thread
from cryptography.fernet import Fernet
count = 0
s = socket.socket()
print('socket created')
s.bind(("100.69.45.231", 9997))
s.listen(3)
print("waiting for connections")
print(" ")

def handle_client(c, addr,key,c_key):
    def receiving():
        while True:
        	       try:
        	       	text = c.recv(1024)
        	       	print("/n recieved encrypted message from clinet : ",text)
        	       	print(" ")
        	       	text1 = Fernet(c_key).decrypt(text).decode()
        	       	print("decrypted Client message  :", text1)
        	       	print(" ")
        	       except Exception as e:
        	       	print(e)
        	       	break

    def sending():
    	while True:
    		x = input("Server: ")
    		print("  ")
    		x1 = x.encode()
    		x2 = Fernet(key).encrypt(x1)
    		c.send(x2)
    		print("encrypted message from server that is sent : ",x2)
    		print(" ")

    rec = Thread(target=receiving)
    send = Thread(target=sending)
    rec.start()
    send.start()

def accepting():
    key = Fernet.generate_key()
    while True:
        c, addr = s.accept()
        print("connected with", addr)
        c.send(key)
        print("The key is sent to client : ",key)
        c_key= c.recv(1024)
        print("The key is recieved from client: ",c_key)
        client_handler = Thread(target=handle_client, args=(c, addr,key,c_key))
        client_handler.start()

accept_thread = Thread(target=accepting)
accept_thread.start()