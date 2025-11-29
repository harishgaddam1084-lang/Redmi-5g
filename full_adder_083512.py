
def hf(x):
	input1 = list(inp)
	a = int(input1[0])
	b = int(input1[1])
	c = int(input1[2])	
	print("sum : "+str(a^b^c))
	print( "carry : " + str((a and b) or (b and c ) or (c and a)))


while True:
	inp = input("enter : ")
	hf(inp)