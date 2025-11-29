from tkinter import * 
mw = Tk()

balance = []
def options(x):
	#unpack
	pass_label.pack_forget()
	pass_entry.pack_forget()
	cpass_label.pack_forget()
	cpass_entry.pack_forget()
	pass_button.pack_forget()
	result.pack_forget()
	next_button.pack_forget()
	#pack
	deposit_btn.pack(pady = 250)
	withdraw_btn.pack()
	balance_btn.pack(pady = 250)
	if x == "deposit":
		deposit_btn.pack_forget()
		withdraw_btn.pack_forget()
		balance_btn.pack_forget()
		deposit_label.pack(anchor = NW,pady = 30,padx = 15)
		deposit_entry.delete(0,END)
		deposit_entry.pack(anchor = NW,padx = 15)
		depositing_btn.pack(pady= 30)
		result_label.config(text = " ")
		result_label.pack()
	if x == "withdraw":
		deposit_btn.pack_forget()
		withdraw_btn.pack_forget()
		balance_btn.pack_forget()
		withdraw_label.pack(anchor = NW,pady = 30,padx = 15)
		withdraw_entry.delete(0,END)
		withdraw_entry.pack(anchor = NW,padx = 15)
		withdraw_btn1.pack(pady = 30)
		withdraw_rlabel.config(text = " ")
		withdraw_rlabel.pack()
	if x == "balance":
		deposit_btn.pack_forget()
		withdraw_btn.pack_forget()
		balance_btn.pack_forget()
		balance_label.pack(anchor = NW,padx = 15)
		


def deposit():
	amount = deposit_entry.get()
	if balance == []:
		with open("bank_info.txt","a") as file2:
			file2.write("\n"+"balance = "+amount)
			result_label.config(text = "your current balance is : "+str(amount))
		back_btn.pack(pady = 30)
		balance.append(int(amount))
	elif balance != []:
		with open("bank_info.txt","a") as file1:
			currentbalance = int(amount)+int(balance[-1])
			file1.write("\n"+"balance = "+str(currentbalance))
		result_label.config(text = "your current balance is : "+str(currentbalance))
		back_btn.pack(pady = 30)
		balance.append(int(currentbalance))

def withdraw():
	withdraw_amount = withdraw_entry.get()
	if balance == []:
		withdraw_rlabel.config(text = "insufficient balance",fg = "red")
		back_btn.pack(pady = 30)
	elif int(withdraw_amount) > int(balance[-1]):
		withdraw_rlabel.config(text = "insufficient balance",fg = "red")
		back_btn.pack(pady = 30)
	elif int(withdraw_amount)<= int(balance[-1]):
		balance_amount = int(balance[-1])- int(withdraw_amount)
		with open("bank_info.txt","a") as file:
			file.write("\n"+"balance = "+str(balance_amount))
		withdraw_rlabel.config(text = "Withdrawal amount is "+str(withdraw_amount)+"\n"+"Your current balance is "+str(balance_amount),fg = "black")
		back_btn.pack(pady = 30)
		balance.append(int(balance_amount))


def balance1(x):
	if balance == []:
		balance_label.config(text = "you haven't deposited the amout yet",fg = "red")
		back_btn.pack(pady = 30)
	else:
		balance_label.config(text = "your current balance is "+str(balance[-1]),fg = "black")
		back_btn.pack(pady = 30)
	
	


def back():
	#unpack options
	deposit_label.pack_forget()
	deposit_entry.pack_forget()
	depositing_btn.pack_forget()
	result_label.pack_forget()
	withdraw_label.pack_forget()
	withdraw_entry.pack_forget()
	withdraw_btn1.pack_forget()
	withdraw_rlabel.pack_forget()
	balance_label.pack_forget()
	back_btn.pack_forget()
	deposit_btn.pack(pady = 250)
	withdraw_btn.pack()
	balance_btn.pack(pady = 250)
	
	
	
	
	
	
	
	
	
	
def confirming_password():
	input_password = pass_entry.get()
	realpassword1 = our_password
	totallength = len(realpassword1)
	passwordlength = totallength-11
	realpasswordindex = "-"+str(passwordlength)
	
	if realpassword1[int(realpasswordindex):].strip()== input_password:
		result.config(text = "correct password",fg = "black")
		result.pack(pady = 30)
		next_button.pack(pady = 30)
	else:
		result.pack(pady = 30)
		result.config(text = "incorrect password",fg= "red")

def Taking_password():
	password = pass_entry.get()
	confirm_password = cpass_entry.get()
	if password.strip() == confirm_password.strip():
		with open("bank_info.txt","w") as file:
			file.write("password = "+str(password))
		result.config(text = "your password is saved",fg = "black")
		result.pack(pady = 30)
		next_button.pack(pady = 30)
	else:
		result.pack(pady = 30)
		result.config(text = "incorrect password",fg = "red")


pass_label = Label(mw,text= "enter the password")
pass_entry = Entry(mw)
cpass_label = Label(mw,text = "confirm the password")
cpass_entry = Entry(mw)
pass_button= Button(mw,text = "click",command = confirming_password)
result = Label(mw,text = " ")
next_button = Button(mw,text = "Next-->",command = lambda : (options(1)))
#options 
deposit_btn = Button(mw,text = "Deposit",command = lambda : (options("deposit")))

withdraw_btn = Button(mw,text = "Withdraw",command = lambda : (options("withdraw")))

balance_btn = Button(mw,text = "Balance",command = lambda : (options("balance"),balance1(1)))
#deposit 
deposit_label = Label(mw,text = "Enter amount")
deposit_entry = Entry(mw)
depositing_btn = Button(mw,text = "Deposit",command = deposit)
result_label = Label(mw,text = " ")
#withdraw
withdraw_label = Label(mw,text= "Enter amount")
withdraw_entry = Entry(mw)
withdraw_btn1 = Button(mw,text = "Withdraw",command = withdraw)
withdraw_rlabel = Label(mw,text = " ")
#balance 
balance_label = Label(mw,text = " ")
#back button
back_btn = Button(mw,text = "Back<--",command = back)
try:
	with open("bank_info.txt","r") as file:
		info = file.readlines()
		for password in info:
			if password[0:8] == "password":
				global our_password 
				our_password = password
				pass_label.pack(anchor = NW,pady = 30,padx = 15)
				pass_entry.pack(anchor = NW,padx = 15)
				pass_button.config(command = confirming_password)
				pass_button.pack(pady = 30)
	with open("bank_info.txt","r") as file1:
		bank_info = file1.readlines()
		for detail in bank_info:
			if detail[0:7].strip() == "balance":
				balan = detail
				lengthofbalance = len(balan)
				realbalance = lengthofbalance-10
				balanceindex = "-"+str(realbalance)
				balance.append(balan[int(balanceindex):])

except FileNotFoundError:
				pass_label.pack(anchor = NW,pady = 30,padx = 15)
				pass_entry.pack(anchor = NW,padx = 15)
				cpass_label.pack(anchor = NW,pady = 30,padx = 15)
				cpass_entry.pack(anchor = NW,padx = 15)
				pass_button.config(command = Taking_password)
				pass_button.pack(pady = 30)

				
mw.mainloop()