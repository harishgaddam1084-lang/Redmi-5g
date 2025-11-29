import random
from datetime import datetime
time = datetime.now()

def random_sum(*sum):
	list = []
	list2=[]
	answer = []
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
					ans = int(input(str(z+1)+":"+str(list[first_value])+"+"+str(list[second_value])+" : "))
				elif sums_type.strip().lower()== "sub":
					ans = int(input(str(z)+":"+str(list[first_value])+"-"+str(list[second_value])+" : "))
				elif sums_type.strip().lower()== "multi":
					ans = int(input(str(z+1)+":"+str(list[first_value])+"*"+str(list[second_value])+" : "))
				elif sums_type.strip().lower()== "div":
					ans = float(input(str(z+1)+":"+str(list[first_value])+"/"+str(list[second_value])+" : "))
		answer.append(ans)
					
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
			
	print(b_mint,b_sec)
	a_sec = time.second
	a_mint= time.minute
	print(a_mint,a_sec)
	input("Press enter to reveal answers ")
	c_no = 0
	w_no = 0
	counter = 0
	if sums_type.strip().lower()== "add":
		for add in list2:
			counter = counter +1
			if add in answer:
				c_no +=1
				print(counter,"correct answer")
			else:
				w_no +=1
				print(f"{counter} wrong answer : {add}")
	elif sums_type.strip().lower()== "sub":
		for sub in list2:
			counter = counter +1 
			if sub in answer:
				c_no +=1
				print(counter,"correct answer")
			else:
				w_no +=1
				print(f"{counter} wrong answer : {sub}")
	elif sums_type.strip().lower()== "multi":
		for multi in list2:
			counter = counter +1 
			if multi in answer:
				c_no +=1
				print(counter,"correct answer")
			else:
				w_no +=1
				print(f"{counter} wrong answer : {multi}")
	elif sums_type.strip().lower() == "div":
		for div in list2:
			counter = counter +1 
			if div in answer:
				c_no +=1
				print(counter,"correct answer")
			else:
				w_no +=1
				print(f"{counter} wrong answer : {div}")
	print(f"you got {c_no} correct answers and {w_no} wrong answer in {a_mint-b_mint} minutes {a_sec-b_sec} seconds")
		

closer = " "
while closer.strip().lower() != "exit":
	start = int(input("enter your range : "))
	end = int(input("enter your range : "))
	sums = int(input("enter how many sums you want : "))
	sums_type= input("enter what type of sum you want : ")
	b_mint= time.minute
	b_sec = time.second
	print(b_mint,b_sec)
	random_sum(start,end,sums,sums_type,b_mint,b_sec)
	closer = input("enter 'exit' to exit : ")