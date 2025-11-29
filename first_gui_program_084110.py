from tkinter import * 
mw = Tk()
def Print():
	input1= main_input.get()
	view2.config(text= "hello "+input1)
	main_input.delete(0,END)
	
view = Label(mw,text="Enter your name")
view.pack(padx = 50,pady= 20,anchor = NW)

main_input = Entry(mw)
main_input.pack(padx = 50,pady= 30,anchor = NW)

btn = Button(mw,text="click here",command= Print)
btn.pack(padx = 50,pady= 30,anchor = NW)

view2= Label(mw,text=" ")
view2.pack(padx = 60,pady= 30,anchor = NW)

mw.mainloop()