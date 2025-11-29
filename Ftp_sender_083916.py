import socket 
from threading import Thread

s = socket.socket()
print('socket created')
s.bind(("192.168.29.255", 9997))
s.listen(3)
file_name = input("Enter the file name : ")
print("waiting for connections...")
print(" ")
c, addr = s.accept()
print("connected with", addr)
c.sendall(file_name.encode())
def sending(c,addr):
	try:
		with open(file_name,"rb") as file:
			data = file.read()
		c.sendall(data)
		print("successfully sent")
	except FileNotFoundError:
		print("file not found. Give the correct file name")
	
	
sending_thread = Thread(target = sending,args=(c,addr))
sending_thread.start()
	