import random
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
	input("Press enter to reveal answers ")
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
	start = int(input("enter your range : "))
	end = int(input("enter your range : "))
	sums = int(input("enter how many sums you want : "))
	sums_type= input("enter what type of sum you want : ")
	random_sum(start,end,sums,sums_type)
	closer = input("enter 'exit' to exit : ")