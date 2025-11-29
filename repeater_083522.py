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
