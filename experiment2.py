import socket
from threading import Thread
from cryptography.fernet import Fernet


c = socket.socket()
c.connect(("localhost", 9993))



def s():
	key = Fernet.generate_key()
	c.send(key)
	print("the key is sent_c",key)
def r():
	s_key = c.recv(1024)
	print("the key is recieved_c",s_key)


s1 = Thread(target = s)
r1 = Thread(target= r)
r1.start()
s1.start()