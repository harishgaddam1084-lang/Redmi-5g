print(" ")
print("RULES : ")
print(" ")
print("1.ENTER YOUR FIRST NUMBER")
print(" ")
print("2.SECONDLY,ENTER YOUR SECOND NUMBER")
print(" ")
print("3.THEN ENTER YOUR MATH OPERATOR")
print(" ")
print("4.YOU CAN ONLY USE 'ADD','SUB','MULTI','DIV' and 'exponential'")
print(" ")
def get_numbers(*number):
	if y.strip().lower() == "add" or y.strip().lower() == "addition":
		print(x+z)
# Here i have written as much as combinations for math operator so that it doesnt give any type of error
	elif y.strip().lower() == "sub" or y.strip().lower()== "substraction":
		print(x-z)
	elif y.strip().lower()== "multi" or y.strip().lower()== "multiplication":
		print(x*z)
	elif y.strip().lower()=="div" or y.strip().lower()== "division":
		print(x/z)
	elif y.strip().lower()== "power" or y.strip().lower() == "expo" or y == "expo" or  y.strip().lower()== "exponential":
			print(x**z)

closer = " "
while closer != "exit" and closer != "exit " :
# here this may give an error. if someone give a string to "x" or "y" it may give a error as the "x" and "y" only take integer 
	x = int(input("enter your first number : "))
	print(" ")
	z = int(input("enter your second number or exponetial : "))
	print(" ")
	y = input("enter your math operator : ")
	get_numbers(x,z,y)
	closer = input("enter 'exit' to exit or enter any character to continue : ")