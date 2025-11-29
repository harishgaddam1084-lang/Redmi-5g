import socket 
from threading import Thread 
c = socket.socket()
c.connect(("localhost",9997))
file_name = c.recv(1024).decode()


def recieving():
	with open(file_name,"wb") as file:
		while True:
			data = c.recv(1024)
			if not data:
				break
				print("successfully recieved")
			file.write(data)
	
	
recieving_thread = Thread(target= recieving)
recieving_thread.start()