from tkinter import * 
import datetime 
import time
mw = Tk()
mw.geometry("1000x1000")
counter = 0
def password():
	np = new_password.get()
	global cp
	cp= confirm_password.get()
	if cp.strip() == "" or np.strip() == "":
		result.config(text = "enter the password")
	else:
		if cp != np:
			result.config(text= "  Incorrect password.Re-enter",fg = "red")
			new_password.delete(0,END)
			confirm_password.delete(0,END)
		elif cp==np:
			time = str(datetime.datetime.now())
			result.config(text = "  your password is saved successfully",fg = "black")
			btn2.pack()
def test():
	view3.pack(anchor = NW)
	view4.pack(anchor = NW)
	view2.pack_forget()
	btn2.pack_forget()
	result.config(text = " ")
	view1.pack_forget()
	new_password.pack_forget()
	confirm_password.pack_forget()
	btn.configure(command = test2)
	btn.pack_forget()
	result.pack_forget()
	view1.pack(anchor= NW,padx=20)
	new_password.pack(anchor= NW,padx=20,pady= 50)
	btn.pack(pady= 50)
	result.pack(pady= 50,anchor= NW)
	new_password.delete(0,END)
	
def test2():
	global counter
	counter =counter+1
	Np= new_password.get()
	if Np!=cp and counter ==3:
		result.config(text= "Access denied",fg= "red")
		time.sleep(1)
		mw.destroy()
	elif Np != cp:
		result.config(text= "Incorrect password : "+str(counter)+" times",fg= "red")
		new_password.delete(0,END)
	else:
		result.config(text= "correct password",fg = "black")
		
	
	


view1= Label(mw,text="Enter the password")
view1.pack(anchor= NW,padx=20)
new_password= Entry(mw)
new_password.pack(anchor= NW,padx=20,pady= 50)
view2 = Label(mw,text= "Confirm password")
view2.pack(anchor= NW,padx=20)
confirm_password= Entry(mw)
confirm_password.pack(anchor= NW,pady=50,padx=20)
btn= Button(mw,text= "click",command = password)
btn.pack(pady= 50)
result = Label(mw,text= " ")
result.pack(pady= 50,anchor= NW)
btn2 = Button(mw,text= "Next-->",command= test)

view3= Label(mw,text= "BE CAREFUL")
view4 = Label(mw,text = "IF YOU GIVE 3 INCORRECT PASSWORDS"+"\n"+"YOUR ACCESS WILL BE DENIED")
mw.mainloop()