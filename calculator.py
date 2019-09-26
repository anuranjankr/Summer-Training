print("\t\tCALCULATOR")
num1=int(input("Enter First number : "))
t=True
while t:
    print("\nEnter\n1 For ADDITION\n2 For SUBSTRACTION\n3 For MULTIPLICATION\n4 For DIVISION")
    ip=input("Enter your choice : ")
    num2=int(input("Ente number for calculation : "))
    if ip=='1':
        num1+=num2
        print("\nYour Result ",num1)
    elif ip=='2':
        num1-=num2
        print("\nYour Result ",num1)
    elif ip=='3':
        num1*=num2
        print("\nYour Result ",num1)
    elif ip=='4':
        num1/=num2
        print("\nYour Result ",num1)
    else:
        print("Wrong Input")
    i=input("\nDo you want to proceed (0 for NO 1 for YES) : ")
    if i=='1':
        pass
    elif i=='0':
        t=False
        print("\nProgram Ends\n")
    else:
        print("Wrong Input")
    
