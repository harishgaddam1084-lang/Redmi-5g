from tkinter import * 
mw= Tk()
counter = 0
mw.geometry("1000x1000")
def ff():
	pass
	
def f1(x):
	if x ==1:
		global counter 
		counter = counter +1
		#this is for player 1 
		if counter%2==1 or counter%9==0:
			click.configure(bg = 'red',command = ff,text= "X")
		#this is for player 2 
		elif counter%2==0:
			click.configure(bg= 'blue',command =ff,text= "O")

def f2(x):
	if x ==2:
		global counter 
		counter = counter +1
		if counter%2==1 or counter%9==0:
			click1.configure(bg = 'red',command = ff,text= "X")
		elif counter%2==0:
			click1.configure(bg= 'blue',command =ff,text= "O")
			
def f3(x):
	if x ==3:
		global counter 
		counter = counter +1
		if counter%2==1 or counter%9==0:
			click2.configure(bg = 'red',command = ff,text= "X")
		elif counter%2==0:
			click2.configure(bg= 'blue',command =ff,text= "O")
			
def f4(x):
	if x ==4:
		global counter 
		counter = counter +1
		if counter%2==1 or counter%9==0:
			click3.configure(bg = 'red',command = ff,text= "X")
		elif counter%2==0:
			click3.configure(bg= 'blue',command =ff,text= "O")

def f5(x):
	if x ==5:
		global counter 
		counter = counter +1
		if counter%2==1 or counter%9==0:
			click4.configure(bg = 'red',command = ff,text= "X")
		elif counter%2==0:
			click4.configure(bg= 'blue',command =ff,text= "O")

def f6(x):
	if x ==6:
		global counter 
		counter = counter +1
		if counter%2==1 or counter%9==0:
			click5.configure(bg = 'red',command = ff,text= "X")
		elif counter%2==0:
			click5.configure(bg= 'blue',command =ff,text= "O")

def f7(x):
	if x ==7:
		global counter 
		counter = counter +1
		if counter%2==1 or counter%9==0:
			click6.configure(bg = 'red',command = ff,text= "X")
		elif counter%2==0:
			click6.configure(bg= 'blue',command =ff,text= "O")

def f8(x):
	if x ==8:
		global counter 
		counter = counter +1
		if counter%2==1 or counter%9==0:
			click7.configure(bg = 'red',command = ff,text= "X")
		elif counter%2==0:
			click7.configure(bg= 'blue',command =ff,text= "O")

def f9(x):
	if x ==9:
		global counter 
		counter = counter +1
		if counter%2==1 or counter%9==0:
			click8.configure(bg = 'red',command = ff,text= "X")
		elif counter%2==0:
			click8.configure(bg= 'blue',command =ff,text= "O")

def result(x):
	if x ==10:
		if (click["bg"]== "red" and click1["bg"]=="red" and click2["bg"]== "red") or(click3["bg"]=="red" and click4["bg"]=="red" and click5["bg"]=="red") or (click6["bg"]=="red" and click7["bg"]=="red" and click8["bg"]=="red") or (click["bg"]== "red" and click3["bg"]== "red" and click6["bg"]== "red") or (click1["bg"]== "red" and click4["bg"]== "red" and click7["bg"]== "red") or (click2["bg"]== "red" and click5["bg"]== "red" and click8["bg"]== "red") or (click["bg"]== "red" and click4["bg"]== "red" and click8["bg"]== "red") or (click2["bg"]== "red" and click4["bg"]== "red" and click6["bg"]== "red"):
			label.config(text= "player 1 is winner")

		elif (click["bg"]== "blue" and click1["bg"]=="blue" and click2["bg"]== "blue") or(click3["bg"]=="blue" and click4["bg"]=="blue" and click5["bg"]=="blue") or(click6["bg"]=="blue" and click7["bg"]=="blue" and click8["bg"]=="blue") or (click["bg"]== "blue" and click3["bg"]== "blue" and click6["bg"]== "blue") or (click1["bg"]== "blue" and click4["bg"]== "blue" and click7["bg"]== "blue") or (click2["bg"]== "blue" and click5["bg"]== "blue" and click8["bg"]== "blue") or (click["bg"]== "blue" and click4["bg"]== "blue" and click8["bg"]== "blue") or (click2["bg"]== "blue" and click4["bg"]== "blue" and click6["bg"]== "blue"):
			label.config(text= "player 2 is the winner")
		elif counter ==9:
			if 1==2:
				pass
			else:
				label.config(text= "Draw")
	
	

label = Label(mw,text= " ")
label.grid(column = 0,row=3,sticky=E)
label2= Label(mw,text= " ")
label2.grid(column=1,row=3,sticky=W)
click = Button(mw,text= " ",command = lambda : (f1(1),f2(1),f3(1),f4(1),f5(1),f6(1),f7(1),f8(1),f9(1),result(10)),padx = 75,pady=50)
click.grid(column= 0,row=0,sticky= E)
click1 = Button(mw,text= " ",command = lambda : (f1(2),f2(2),f3(2),f4(2),f5(2),f6(2),f7(2),f8(2),f9(2),result(10)),padx = 75,pady=50)
click1.grid(column= 1,row= 0,sticky= W)

click2 = Button(mw,text= " ",command = lambda : (f1(3),f2(3),f3(3),f4(3),f5(3),f6(3),f7(3),f8(3),f9(3),result(10)),padx = 75,pady=50)
click2.grid(column= 2,row= 0,sticky= E)

click3 = Button(mw,text= " ",command = lambda : (f1(4),f2(4),f3(4),f4(4),f5(4),f6(4),f7(4),f8(4),f9(4),result(10)),padx = 75,pady=50)
click3.grid(column= 0,row= 1,sticky= E)

click4 = Button(mw,text= " ",command = lambda : (f1(5),f2(5),f3(5),f4(5),f5(5),f6(5),f7(5),f8(5),f9(5),result(10)),padx = 75,pady=50)
click4.grid(column= 1,row= 1,sticky= E)

click5 = Button(mw,text= " ",command = lambda : (f1(6),f2(6),f3(6),f4(6),f5(6),f6(6),f7(6),f8(6),f9(6),result(10)),padx = 75,pady=50)
click5.grid(column= 2,row= 1,sticky= W)

click6= Button(mw,text= " ",command = lambda : (f1(7),f2(7),f3(7),f4(7),f5(7),f6(7),f7(7),f8(7),f9(7),result(10)),padx = 75,pady=50)
click6.grid(column= 0,row= 2,sticky= E)

click7= Button(mw,text= " ",command = lambda : (f1(8),f2(8),f3(8),f4(8),f5(8),f6(8),f7(8),f8(8),f9(8),result(10)),padx = 75,pady=50)
click7.grid(column= 1,row= 2,sticky= E)

click8= Button(mw,text= " ",command = lambda : (f1(9),f2(9),f3(9),f4(9),f5(9),f6(9),f7(9),f8(9),f9(9),result(10)),padx = 75,pady=50)
click8.grid(column= 2,row= 2,sticky= E)
mw.mainloop()