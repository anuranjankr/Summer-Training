name=['anu','ram','shyam']
pin=[1514,3213,1765]
balance=[5330,3634,7000]
#FOR ADMIN
user=['admin']
password=[1231]
def ask_name():
	j=input("Enter your name : ")
	if j in name:
		index=name.index(j)
	else:
		index=len(name)
	return index

def pin_check(index):
	k=int(input("Enter your pin: "))
	if pin[index]==k:
		return True
	else:
		return False

def check_avaibility(amt,index):
	if amt<=balance[index]:
		return True
	else:
		return False


t=True
while t:
	print("Are you a user or admin :\nEnter 1 for ADMIN\nEnter 2 for USER LOGIN\n")
	a=input("Enter your choice : ")
	if a=='1':
		print("I am ADMIN")
		allowed2=1
		while allowed2<=3:
			usr=input("Enter your name : ")
			if usr==user[0]:
				allowed3=1
				while allowed3<=3:
					ps=int(input("Enter password : "))
					if ps==password[0]:
						d=True
						while d:
							print("\nEnter\n1 To insert a new USER\n2 To Delete a USER \n3 Exit")
							ip=input("Enter your choice : ")
							if ip=='1':
								usr_name=input("Enter name : ")
								usr_pin=input("Enter pin : ")
								usr_balance=input("Enter balance : ")
								name.append(usr_name)
								pin.append(usr_pin)
								balance.append(usr_balance)
								print("\nNew User Inserted\n")
							elif ip=='2':
								usr_name=input("Enter the user You want to delete ")
								if usr_name in name:
									index1=name.index(usr_name)
								else:
									index1=len(name)
								if index1<len(name):
									name.pop(index1)
									pin.pop(index1)
									balance.pop(index1)
								else:
									print("\nWrong input\n")
							elif ip=='3':
								d=False
								print("\n\nYour Changes are Saved\n")
							else:
								printf("\nWrong input\n")
						allowed3=5
					else:
						allowed3+=1
						print("\nEnter correct password\n")
				allowed2=5
			else:
				allowed2+=1
				print("Enter Correct name \n")

	elif a=='2':
		print("I am user")
		allowed=1
		while allowed<=3:
			index=ask_name()
			print(index)
			if index<len(name):
				allowed1=1
				while allowed1<=3:
					check=pin_check(index)
					if check:
						b=True
						while b:
							print("\nEnter\n1 For WITHDRAWL\n2 DEPOSIT\n3 CHECK BALANCE\n4 Exit")
							m=input("Enter your choice : ")
							if m=='1':
								wd_amt=int(input("Enter the amount you want to withdraw : "))
								check1=check_avaibility(wd_amt,index)
								if check1:
									balance[index]-=wd_amt
									print("Withdraw sucessfull")
									print("\nYour Remaining balance is ",balance[index],"\n")
								else:
									print("Insufficient BALANCE")
							elif m=='2':
								dp_amt=int(input("Input amout to be deposited : "))
								balance[index]+=dp_amt
								print("Deposit sucessfull")
								print("\nYour current balance is ",balance[index],"\n")
							elif m=='3':
								print("\nYour Current Balance is ",balance[index],"\n")
							elif m=='4':
								b=False
								print("\nYour Transaction was SUCESSFULL \n\n PLEASE VISIT AGAIN\n")
							else:
								print("\nWrong Input")
						allowed1=5
					else:
						print("\nYour PIN is incorrect\n\nGive appropriate input\n")
						allowed1+=1
					if allowed1==4:
						print("too many attempts\nSTART AGAIN")
				allowed=5
			else:
				print("\nYour name was not in the list\n\nGive appropriate input\n")
				allowed+=1
			if allowed==4:
				print("too many attempts\nSTART AGAIN")
	else:
		print("Wrong input")
	t=False
