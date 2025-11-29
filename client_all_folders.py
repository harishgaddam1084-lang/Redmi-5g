import socket 
from threading import Thread 

c = socket.socket()
c.connect(("localhost",9999))
print("connected")


def recieving():
	while True:
		text= c.recv(1024)
		text1 = text.decode()
		print(text1)
		if not text:
			break
	
receive = Thread(target = recieving)
receive.start()