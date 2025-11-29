import time
minutes = int(input("enter minutes : "))
seconds = minutes*60
sec = 0
if seconds >60:
	mint = seconds % 60
for min in range(mint):
	for x in range(seconds):
		sec = sec +1
		if sec >= 60:
			sec = 0
		time.sleep(1)
		print(str(min)+" : "+str(sec))