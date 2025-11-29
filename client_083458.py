import socket
from threading import Thread
from cryptography.fernet import Fernet

c = socket.socket()
c.connect(("localhost", 9996))
key = Fernet.generate_key()
s_key = c.recv(1024)
print("the key is recieved from server : ",s_key)
c.send(key)
print("the key is sent to server",key)

def receiving():
	while True:
		try:
		    text = c.recv(1024)
		    print("/n recieved encrypted message from server : ",text)
		    print(" ")
		    text1 = Fernet(s_key).decrypt(text).decode()
		    print("decrypted message from server : ", text1)
		    print(" ")
		except Exception as e:
			print(e)
			break

def sending():
	while True:
		x = input("Client: ")
		print(" ")
		x1 = x.encode()
		x2 = Fernet(key).encrypt(x1)
		c.send(x2)
		print("the encrypted message sent to server : ",x2)
		print(" ")



send = Thread(target=sending)
send.start()
rec = Thread(target=receiving)
rec.start()