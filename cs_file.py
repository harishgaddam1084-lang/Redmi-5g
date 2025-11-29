import os 

def commands(*x):
	if type == "path":
		os.chdir(command)
		print(f"the directory is changed to {command}")
	else:
		x = os.system(command)
		print(x)
		return x 
	


while True:
	type = input("enter type : ")
	command = input("enter : ")
	commands(command,type)