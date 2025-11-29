import socket
import os 
import subprocess

s = socket.socket()
s.bind(("localhost",9999))
s.listen(3)
print("waiting")
c,addr= s.accept()

def commands():
	print("command mode")
	command_type = c.recv(1024).decode()
	instructions = "0 = directory_name \n"+"1= ls\n"
	c.sendall(instructions.encode())
	message = c.recv(1024)
	message_decode = message.decode()
	if command_type == "0":
		message1 = message_decode
		os.chdir(message1)
		verification = "succesfully dir changed "
		c.sendall(verification.encode())
	elif command_type =="1":
		message2 = message_decode
		output = subprocess.run(message2,capture_output = True)
		print("done")
		output1 = output.stdout
		c.sendall(output1)
		print("sent")
	elif command_type.strip() == "exit":
		pass
	else:
		error = "invalid command"
		c.sendall(error.encode())

def file_transfer():
	print("ftp mode")
	file_name = c.recv(1024)
	print("recieved")
	filename = file_name.decode()
	print("decoded")
	try:
		with open(filename,"rb") as file:
			data = file.read()
		c.sendall(data)
		print("successfully sent")
	except FileNotFoundError:
		print("file not found. Give the correct file name")
	if file_name.decode().strip() == "exit":
		pass
		
	
	
	
	
	
while True:
	type = c.recv(1024).decode()
	if type.strip().lower() == "command":
		commands()
	elif type.strip().lower() == "ftp":
		file_transfer()