from tkinter import * 
mw = Tk()
def choice():
	choice1= choice.get()
	if choice1.strip().lower()== "sc":
		view.pack(anchor= NW,padx= 20)
		input.pack(anchor=NW,padx=20,pady = 50)
		view2.pack(anchor= NW,padx= 20)
		input2.pack(anchor=NW,padx=20,pady = 50)
		click.pack(anchor=NW,padx=20,pady = 50)
		view3.pack(anchor=NW,padx=20)
def sc():
	number1 = input.get()
	number2 = input2.get()
	output = int(number1)+int(number2)
	view3.config(text= "the solution is "+str(output))
#choice block
view = Label(mw,text= "ENTER YOUR CHOICE")
view.pack(anchor= NW,padx= 20)

choice = Entry(mw)
choice.pack(anchor= NW,padx= 20)

choice_button= Button(mw,text = "click here",command = choice)
choice_button.pack(anchor=NW,padx=20,pady = 50)
#input and output blocks
view = Label(mw,text= "ENTER")
input = Entry(mw)
view2 = Label(mw,text= "ENTER")
input2 = Entry(mw)
click= Button(mw,text = "click here",command = sc)
view3 = Label(mw,text= " ")
mw.mainloop()