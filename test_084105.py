balance = []
with open("bank_info.txt","r") as file1:
	bank_info = file1.readlines()
	for detail in bank_info:
		if detail[0:7].strip() == "balance":
			balan = detail
			lengthofbalance = len(balan)
			realbalance = lengthofbalance-10
			balanceindex = "-"+str(realbalance)
			balance.append(balan[balanceindex:])