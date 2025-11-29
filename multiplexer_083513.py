def mux(x,y):
	input1 = list(inp)
	s1 = int(sel[0])
	s0 = int(sel[1])
	i = 1
	if ((not s1)and(not s0) and (i)) == True:
		print(input1[0])
	elif ((not s1) and (s0) and (i)) == True:
		print(input1[1])
	elif ((s1) and (not s0) and (i)) == True:
		print(input1[2])
	elif (s1 and s0 and i) == True:
		print(input1[3])

inp = input("enter the data : ")

while True :
	if len(inp) != 4:
		print("Invalid data")
		inp = input("enter the data : ")
	sel = input("enter the selection input: ")
	mux(inp,sel)