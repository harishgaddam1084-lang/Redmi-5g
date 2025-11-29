print("This single program provides all programs")
print("The programs are 'calculator','file_creator','info','password','possible_combinations','random_sums','repeator'")
print("")
import math
import os
import datetime
from itertools import permutations
import random
def all_programs(*program):
						#CALCULATOR
	if program_selector.strip().lower() == "calculator":
		print(" ")
		print(" " *25+"CALCULATOR")
		print(" ")
		print("For help, Enter 'help', 'instructions'or 'in' at 'enter what calculations you want' input.")
		print(" ")
		def get_numbers(*numbers):
			if choice.strip().lower() == "tr" or choice == "trignometric ratios":
		#trignometric ratios
				if t.strip().lower()== "sin" or t.strip().lower() == "s":
					if angle == 30:
						angles = math.radians(angle)
						sin1 = math.sin(angles)
						print("1/2","or",sin1)
					elif angle == 45:
						angles = math.radians(angle)
						sin1 = math.sin(angles)
						print("1/√2","or",sin1)
					elif angle == 60:
						angles = math.radians(angle)
						sin1 = math.sin(angles)
						print("√3/2","or",sin1)
					else:
						angles = math.radians(angle)
						sin1 = math.sin(angles)
						print(sin1)
				elif t.strip().lower()== "cos" or t.strip().lower() == "c":
					if angle == 30:
						angles = math.radians(angle)
						cos1 = math.cos(angles)
						print("√3/2","or",cos1)
					elif angle == 45:
						angles = math.radians(angle)
						cos1 = math.cos(angles)
						print("1/√2","or",cos1)
					elif angle == 60:
						angles = math.radians(angle)
						cos1 = math.cos(angles)
						print("1/2","or",cos1)
					else:
						angles = math.radians(angle)
						cos1 = math.cos(angles)
						print(cos1)
					
				elif t.strip().lower()== "tan" or t.strip().lower() == "t":
					if angle == 30:
						angles = math.radians(angle)
						tan1 = math.tan(angles)
						print("1/√3","or",tan1)
					elif angle == 60:
						angles = math.radians(angle)
						tan1 = math.tan(angles)
						print("√3","or",tan1)
					elif angle == 90:
						print("infinite")
					else:
						angles = math.radians(angle)
						tan1 = math.tan(angles)
						print(tan1)
				elif t.strip().lower()== "cot":
					if angle == 0:
						print("infinite")
					elif angle == 30:
						angles = math.radians(angle)
						tan = math.tan(angles)
						print("√3", "or",1/tan)
					elif angle == 45:
						tan = math.tan(angles)
						print(1)
					elif angle == 60:
						angles = math.radians(angle)
						tan = math.tan(angles)
						print("1/√3", "or",1/tan)
					else:
						angles = math.radians(angle)
						tan = math.tan(angles)
						print(1/tan)	
				elif t.strip().lower()== "secant" or t.strip().lower()== "sec" :
					if angle == 30:
						angles = math.radians(angle)
						cos = math.cos(angles)
						secant = 1/cos
						print("2/√3","or",secant)
					elif angle == 45:
						angles = math.radians(angle)
						cos = math.cos(angles)
						secant = 1/cos
						print("√2","or",secant)
					elif angle == 90:
						print("infinite")
					else:
						angles = math.radians(angle)
						sin = math.sin(angles)
						cosec = 1/sin
						print(cosec)
				elif t.strip().lower() == "cosecant" or t.strip().lower()== "cosec":
					if angle == 0:
						print("infinite")
					elif angle == 45:
						angles = math.radians(angle)
						sin = math.sin(angles)
						cosec = 1/sin
						print("√2","or",cosec)
					elif angle == 60:
						angles = math.radians(angle)
						sin = math.sin(angles)
						cosec = 1/sin
						print("2/√3","or",cosec)
					else:
						angles = math.radians(angle)
						sin = math.sin(angles)
						cosec = 1/sin
						print(cosec)
				else:
					print(" ")
					print(t,"is a invalid function")
					print(" ")
					print("Please read the instructions by entering 'in','instructions' or 'help' at calculation input")
#simple calculations 
			if choice.strip().lower() == "sc"or choice.strip().lower() == "simple calculations":
				if y.strip().lower() == "add" or y.strip().lower() == "addition":
					print(x+z)
# Here i have written as much as combinations for math operator so that it doesnt give any type of error
				elif y.strip().lower() == "sub" or y.strip().lower()== "substraction":
					print(x-z)
				elif y.strip().lower()== "multiply" or y.strip().lower()== "multiplication":
					print(x*z)
				elif y.strip().lower()=="div" or y.strip().lower()== "division":
					if z == 0:
						print("Infinite")
					else:
						print(x/z)
				elif y.strip().lower()== "power" or y.strip().lower() == "expo" or  y.strip().lower()== "exponential":
					print(x**z)
				elif y.strip().lower() == "root" or y.strip().lower() == "r":
					root = math.sqrt(x)
					root2 = math.sqrt(z)
					print(root)
					print(root2)
				else:
					print(" ")
					print(y,"is a invalid function")
					print(" ")
					print("Please read the instructions by entering 'in' or 'instructions' or 'help' at calculation input")
					print(" ")
			
			
		closer = " "
		while closer.strip().lower() != "exit" :
# here this may give an error. if someone give a string to "x" or "y" it may give a error as the "x" and "y" only take integer
			choice = input("enter what calculations you want : ")
			if choice.strip().lower() not in ["tr", "trignometric ratios", "trignometricratios", "sc", "simple calculations", "simplecalculations","in","instructions","help"]:
				print(" ")
				print(choice,"is invalid input")
				print(" ")
				print("Please read the instructions by entering 'in' or 'instructions' or 'help' at calculation input")
				print(" ")
		
			if choice.strip().lower() in ["in","instructions","help"]:
				print(" ")
				print("1.This software provides simple calculations and trignometric ratios.")
				print(" ")
				print("2. For simple calculations, Enter 'simple calculations' or short form 'sc'.")
				print(" ")
				print("3. For trignometric ratios, Enter 'trignometric ratios' or short form 'tr'.")
				print(" ")
				print("4. You can do simple calculations like add,sub,multiplication,division,exponetials.")
				print("5. Enter 'add','sub','multiply','div','expo' for simple calculations.")
				print(" ")
				print("6. You can do trignometric ratios like sin,cos,tan,cot,secant,cosecant.")
				print(" ")
				closer = ("enter 'exit' to exit : ")
		
			if choice.strip().lower() == "tr" or choice.strip().lower() == "trignometryratios":
				print(" ")
				t = input("enter your trignometric ratio : ")
				print(" ")
				angle = float(input("enter your angle : "))
				print(" ")
				get_numbers(choice,t,angle)
				closer = input("enter 'exit' to exit : ")
			elif choice.strip().lower() == "simplecalculation" or choice.strip().lower() ==  "simplecalculations" or choice.strip().lower() == "sc":
				print(" ")
				x = float(input("enter your first number : "))
				print(" ")
				z = float(input("enter your second number or exponetial : "))
				print(" ")
				y = input("enter your math operator : ")
				get_numbers(choice,x,z,y)

				closer = input("enter 'exit' to exit : ")
	elif program_selector.strip().lower() in ["file_creator","file creator","filecreator"]:
						#FILE_CREATOR
		print(" "*25+"FILE_CREATOR")
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
	elif program_selector.strip().lower() in ["information","info"]:
					#INFO
		print(" "*25+"INFO")
		def info(information):
			print(" ")
			option = input("do u want a text file(yes/no) : ")
			for x,y in information.items():
				if option.strip().lower() == "yes":
					with open("information.txt","a") as file:
						file.write(str(x)+" : "+str(y)+"\n")
				elif option.strip().lower() == "no":
					print(x,":",y)
				else:
					print("Invalid choice")


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
	elif program_selector.strip().lower() in ["password"]:
						#PASSWORD
		print(" "*25+"PASSWORD")
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
	elif program_selector.strip().lower() in ["pc","possible_combinations","possiblecombinations"]:
				#POSSIBLE_COMBINATIONS
		print(" "*20+"POSSIBLE_COMBINATIONS")
		def word_combinations(word):
   		 y= 0
   		 for p in permutations(word):
		        y+=1
		        combined_word = ''.join(p)
		        print(y,":",combined_word)
		      
		input_word= input("enter your word : ")
		word_combinations(input_word)
	elif program_selector.strip().lower()in ["random_sums","randomsums"]:
					#RANDOM_SUMS
		print(" "*20+"RANDOM_SUMS")
		def random_sum(*sum):
			list = []
			list2=[]
			for x in range(start,end):
				list.append(x)
			zero = 0
			for z in range(sums):	
				indexes = random.sample(range(len(list)),2)
				for y in indexes:
					zero = zero+1
					if zero%2 ==1 :
						first_value = y
					elif zero%2 ==0:
						second_value = y
						if sums_type.strip().lower()== "add":
							print(z+1,":",str(list[first_value]),"+",str(list[second_value]))
						elif sums_type.strip().lower()== "sub":
							print(z+1,":",str(list[first_value]),"-",str(list[second_value]))
						elif sums_type.strip().lower()== "multi":
							print(z+1,":",str(list[first_value]),"*",str(list[second_value]))
						elif sums_type.strip().lower()== "div":
							print(z+1,":",str(list[first_value]),"/",str(list[second_value]))
				if sums_type.strip().lower()== "add":
					addition = list[first_value]+list[second_value]
					list2.append(addition)
		
				elif sums_type.strip().lower()== "sub":
					substraction  = list[first_value]-list[second_value]
					list2.append(substraction)
		
				elif sums_type.strip().lower()== "multi":
					multiplication  = list[first_value]*list[second_value]
					list2.append(multiplication)
			
				elif sums_type.strip().lower() == "div":
					if second_value == 0:
						continue
					division = list[first_value]/list[second_value]
					list2.append(division)
			input()
			counter = 0
			if sums_type.strip().lower()== "add":
				for add in list2:
					counter = counter +1 
					print(str(counter)+":"+str(add))
			elif sums_type.strip().lower()== "sub":
				for sub in list2:
						counter = counter +1 
						print(str(counter)+":"+str(sub))
			elif sums_type.strip().lower()== "multi":
				for multi in list2:
					counter = counter +1 
					print(str(counter)+":"+str(multi))
			elif sums_type.strip().lower() == "div":
				for div in list2:
					counter = counter +1 
					print(str(counter)+":"+str(div))
	
		

		closer = " "
		while closer.strip().lower() != "exit":
			start = int(input("enter your starting range : "))
			end = int(input("enter your ending range : "))
			sums = int(input("enter how many sums you want : "))
			sums_type= input("enter what type of sum you want : ")
			random_sum(start,end,sums,sums_type)
			closer = input("enter 'exit' to exit : ")
	elif program_selector.strip().lower() in ["repeator"]:
						#REPEATOR
		print(" "*25+"REPEATOR")
		def repeater(*words):
			for x in range(times):
				print(x+1," : ",word)

		x = " "
		while x.strip().lower() != "exit":
		    word = input("Enter your word or sentence : ")
		    if word.strip().lower() in ["help()","help","instructions"]:
		    	print(" ")
		    	print("1.Enter any word or sentence ")
		    	print(" ")
		    	print("2.Enter number that  how many times you want to repeat")
		    	print(" ")
		    	print("3.Copy it and paste it where ever you want ")
		    	print(" ")
		    	continue
		    times = int(input("Enter how many times you want to repeat : "))
		    repeater(word, times)
		    x = input("Enter 'exit' to exit or any other character to continue : ")


closer = " "
while closer.strip().lower() != "exit":
	program_selector = input("enter which program you want : ")
	if program_selector.strip().lower() not in ['calculator','file_creator','info','password','possible_combinations','random_sums','repeator']:
		print("Invalid choice")
		continue
	all_programs(program_selector)
	closer = input("enter 'exit' to exit from the entire program : ")