print(" ")
print("For help, Enter 'help', 'instructions'or 'in' at 'enter what calculations you want' input.")
print(" ")
import math
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
# finally completed this program
# i was like 😐😑😵 while making this program