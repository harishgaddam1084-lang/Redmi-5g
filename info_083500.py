import os
def info(information):
	print(" ")
	option = input("do u want a text file(yes/no) : ")
	for x,y in information.items():
		print(x,":",y)
		if option.strip().lower() == "yes":
			with open("information.txt","a") as file:
				file.write(str(x)+" : "+str(y)+"\n")


Info = {}
closer = " "
while closer.strip().lower() != "exit":
	print(" ")
	key = input("enter : ")
	print(" ")
	value = input("enter : ")
	print(" ")
	Info[key] = value
	closer = input("enter 'exit' to exit : ")
	
info(Info)
# finally completed this 
# yeah it is not complicated but this is good program for information