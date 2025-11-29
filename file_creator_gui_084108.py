from tkinter import * 
import os
mw = Tk()
def packer():
	fv.pack_forget()
	file_name.pack_forget()
	iv.pack_forget()
	info.pack_forget()
	remain.pack_forget()
	output.pack_forget()
	wr_ap.pack_forget()
	remain.pack_forget()
	select = selection.get()
	if select.strip().lower() in ["write","append","rename"]:
		fv.pack(anchor= NW,padx = 15)
		file_name.pack(anchor= NW,padx = 15,pady = 25)
		iv.pack(anchor= NW,padx = 15)
		info.pack(anchor= NW,padx = 15,pady= 25)
		wr_ap.pack(pady= 15)
		output.pack(anchor = NW)
	elif select.strip().lower() in ["readline","readlines","remove","size"]:
		fv.pack(anchor= NW,padx = 15)
		file_name.pack(anchor= NW,padx = 15,pady = 25)
		remain.pack()
		output.pack(anchor = NW)
	else:
		output.pack(anchor = NW,padx = 15)
		output.config(text = "Invalid input")
		
	

def wa():
	select = selection.get()
	if select.strip().lower() in ["write","append","rename"]:
		file = file_name.get()
		inf = info.get()
		if select.strip().lower()== "write":
			with open(file,"w") as File:
				File.write(inf)
				output.config(text = "Writing contents is done")
		elif select.strip().lower() == "append":
			with open(file,"a") as File:
				File.write(inf)
				output.config(text = "Appending contents is done")
		elif select.strip().lower()=="rename":
			os.rename(file,inf)
			output.config(text = "Renaming the file is done")
	else:
		pass

def remaining():
	select1 = selection.get()
	if select1.strip().lower() in ["readline","readlines","remove","size"]:
		file1 = file_name.get()
		if select1.strip().lower()=="readline":
			with open(file1,"r") as file:
				output.config(text = file.readline())
		elif select1.strip().lower()=="readlines":
			with open(file1,"r") as file:
				output.config(text = file.readlines())
		elif select1.strip().lower() == "remove":
			os.remove(file1)
			output.config(text = "removing the file is done")
		elif select1.strip().lower()=="size":
			vari1 = os.path.getsize(file1)
			if vari1 >= 1000000:
				output.config(text = str(vari1/10000000)+" Mb")
			elif vari1 >= 1000:
				output.config(text = str(vari1/1000)+" Kb")
			elif vari1 > 0:
				output.config(text = str(vari1)+" Bytes")
	else:
		pass







sv = Label(mw,text = "select the mode")
sv.pack(anchor = NW,padx = 15)
selection = Entry(mw)
selection.pack(anchor= NW,padx = 15,pady= 50)
sb = Button(mw,text = "click",command = packer)
sb.pack()
fv = Label(mw,text = "Enter the file name")
file_name = Entry(mw)
iv= Label(mw,text = "Enter the info")
info= Entry(mw)
wr_ap= Button(mw,text= "click",command = wa)
remain = Button(mw,text= "click",command = remaining)
output = Label(mw,text=" ")
mw.mainloop()