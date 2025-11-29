import datetime
import os
closer = " "
while closer != 2:
	print(" ")
	NewPassword = input("Enter your new password : ")
	print(" ")
	confirm_password = input("Confirm your password : ")
	if NewPassword == confirm_password:
		print(" ")
		print("Your password is saved now.Your password is" ,NewPassword)
		variable = datetime.datetime.now()
		with open("password.txt","a") as file:
			file.write(NewPassword+" on "+str(variable)+"\n")
		print("The password is saved on",datetime.datetime.now())
		new_password = NewPassword
		break
print(" ")		
print("BE CAREFUL!!!")
print("IF YOU GIVE 3 INCORRECT PASSWORDS,YOUR ACCESS WILL BE DENIED")

for x in range(3):
	print(" ")
	password = input("Enter your password  : ")
	if password == confirm_password:
		print(" ")
		print("Correct password")
		break
	elif x == 2:
		print(" ")
		print("ACCESS DENIED!!")
	elif password != confirm_password:
			print(" ")
			print("Incorrect password")
# finally i completed this program
# i know this is not a complicated program
# but this works perfectly how i thought