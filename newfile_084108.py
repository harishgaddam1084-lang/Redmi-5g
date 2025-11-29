import cProfile
from tkinter import * 
import os 
def hi():
	mw = Tk()	
	def all_options():
		starter.pack_forget()
		wr_btn.pack(pady = 100)
		ap_btn.pack()
		rd_btn.pack(pady = 100)
		rds_btn.pack()
		rn_btn.pack(pady = 100)
		rm_btn.pack()
		si_btn.pack(pady = 100)


	def inputs(x):
		global y
		y = x 
	#all options unpacker 
		wr_btn.pack_forget()
		ap_btn.pack_forget()
		rd_btn.pack_forget()
		rds_btn.pack_forget()
		rn_btn.pack_forget()
		rm_btn.pack_forget()
		si_btn.pack_forget()
	#inputs unpacker 
		fv.pack_forget()
		file_name.pack_forget()
		iv.pack_forget()
		info.pack_forget()
		wr_ap.pack_forget()
		output.pack_forget()
	#unpack back button
		if y == 1 or y == 2 or y == 3:
			if y == 3:
				iv.config(text = "Enter another name")
		#packs
			fv.pack(anchor= NW,padx = 15)
			file_name.pack(anchor= NW,padx = 15,pady = 25)
			iv.pack(anchor= NW,padx = 15)
			info.pack(anchor= NW,padx = 15,pady= 25)
			wr_ap.pack(pady= 15)
			output.pack(anchor = NW)
			b_btn.pack()
	
		elif y == 4 or y ==5 or y ==6 or y ==7:
			fv.pack(anchor= NW,padx = 15)
			file_name.pack(anchor= NW,padx = 15,pady = 25)
			wr_ap.pack()
			output.pack(anchor = NW)
			b_btn.pack()


	def codeforinputs():
		filename = file_name.get()
		inf = info.get()
		if y == 1:
			with open(filename,"w") as file:
				file.write(inf)
				output.config(text = "writing the info is done")
		elif y ==2:
			with open(filename,"a") as file:
				file.write(inf)
				output.config(text= "appending the info is done")
		elif y == 3:
			os.rename(filename,inf)
			output.config(text = "renaming the file is done")
		elif y == 4:
			with open(filename,"r") as file:
				output.config(text = file.readline())
		elif y == 5:
			with open(filename,"r") as file:
				output.config(text = file.readlines())
		elif y ==6:
			os.remove(filename)
			output.config(text = "removing the file is done")
		elif y ==7:
			vari1 = os.path.getsize(filename)
			if vari1 >= 1000000:
				output.config(text = str(vari1/10000000)+" Mb")
			elif vari1 >= 1000:
				output.config(text = str(vari1/1000)+" Kb")
			elif vari1 > 0:
				output.config(text = str(vari1)+" Bytes")
			






	
	def back():
		#unpack inputs and back button
		fv.pack_forget()
		file_name.pack_forget()
		iv.pack_forget()
		info.pack_forget()
		wr_ap.pack_forget()
		output.pack_forget()
		b_btn.pack_forget()
		output.config(text = " ")
		file_name.delete(0,END)
		info.delete(0,END)
	#pack options
		starter.pack_forget()
		wr_btn.pack(pady = 100)
		ap_btn.pack()
		rd_btn.pack(pady = 100)
		rds_btn.pack()
		rn_btn.pack(pady = 100)
		rm_btn.pack()
		si_btn.pack(pady = 100)
			
#start option
	starter = Button(mw,text = "Start the program",pady = 45,command = all_options)
	starter.pack(pady = 850)
#all options
	wr_btn= Button(mw,text = "   write   ",command = lambda : inputs(1))
	ap_btn = Button(mw,text = " append ",command = lambda : inputs(2))
	rn_btn = Button(mw,text = "  rename  ",command = lambda : inputs(3))
	rd_btn = Button(mw,text = " readline ",command = lambda : inputs(4))
	rds_btn = Button(mw,text = "readlines ",command = lambda : inputs(5))
	rm_btn = Button(mw,text = "  remove  ",command = lambda : inputs(6))
	si_btn = Button(mw,text = "   size   ",command = lambda : inputs(7))
#inputs 
	fv = Label(mw,text = "Enter the file name")
	file_name = Entry(mw)
	iv= Label(mw,text = "Enter the info")
	info= Entry(mw)
	wr_ap= Button(mw,text= "click",command = codeforinputs)
	output = Label(mw,text=" ")
# back button 
	b_btn = Button(mw,text = "back<--",command = back)
	mw.mainloop()

cProfile.run("hi()")