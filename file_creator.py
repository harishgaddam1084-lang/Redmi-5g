import os
def info(*information):
	if selector.strip().lower()== "write":
		with open(file_name , "w") as file:
			file.write(inf)
	elif selector.strip().strip() == "append":
		with open(file_name,"a") as file:
			file.write(inf)
	elif selector.strip().lower() == "readline":
		with open(file_name,"r") as file:
			print(file.readline())
	elif selector.strip().lower() == "readlines":
		with open(file_name,"r") as file:
			print(file.readlines())
	elif selector.strip().lower() == "remove":
		os.remove(file_name)
	elif selector.strip().lower() == "rename":
		os.rename(file_name,inf)
	elif selector.strip().lower() == "size":
		vari1 = os.path.getsize(file_name)
		if vari1 >= 1000000:
			print(vari1/10000000,"Mb")
		elif vari1 >= 1000:
			print(vari1/1000,"Kb")
		elif vari1 > 0:
			print(vari1,"Bytes")
	elif selector.strip().lower() == "time":
		vari2 = os.path.getmtime(file_name)
		print(vari2)

list = ["readlines","readline","append","write","remove","rename","size","time","help","instructions"]
closer = " "
while closer != "exit":
	selector = input("Enter what you want : ")
	if selector.strip().lower() not in ["readlines","readline","append","write","remove","rename","size","time","help","instructions"]:
		print(" ")
		print("Invalid choice")
		print("   ")
		print("Choose valid choice")
		print(" ")
		print("Enter 'help' or 'instructions' for help")
		print(" ")
	if selector.strip().lower() == "write" or selector.strip().lower() == "append"or selector.strip().lower() == "rename":
		file_name = input("Enter your file name : ")
		inf = input("Enter you are info or name : ")
		info(selector,file_name,inf)
	elif selector.strip().lower()== "readlines" or selector.strip().lower() == "readline" or selector.strip().lower() == "remove" or selector.strip().lower() == "size" or selector.strip().lower() == "time":	
		file_name = input("Enter file name : ")
		info(selector,file_name)
	if selector.strip().lower() == "help" or selector.strip().lower() == "instructions":
		print("1.First,select which option you want")
		print(" ")
		print("2.Secondly,enter your file name")
		print(" ")
		print("3.Then,if you want to write or append, you can give the info you want to write or append")
		print(" ")
		print("4.The options are 'write','append','realine',readlines','size of the file','rename',last modification time")
		print(" ")
	closer = input("Enter 'exit' to exit : ")