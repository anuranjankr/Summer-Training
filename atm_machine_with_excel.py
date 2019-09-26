import xlrd
import xlwt
from xlutils.copy import copy
def read_file():
    global rb
    rb=xlrd.open_workbook("database_atm.xls")
    global rs
    rs=rb.sheet_by_index(0)
    global wb
    wb=copy(rb)
    global ws
    ws=wb.get_sheet(0)

read_file()
'''
name=[]
for i in range(1,rs.nrows):
    name.append(rs.cell_value(i,0))
print(name)

pin=[]
for i in range(1,rs.nrows):
    pin.append(rs.cell_value(i,1))
print(pin)

balance=[]
for i in range(1,rs.nrows):
    balance.append(rs.cell_value(i,2))
print(balance)
'''
while True:
    person=input("\nEnter\n1 For Admin\n2 For User\n3 To Exit : ")
    if person=='1':
        print("I am ADMIN")
        adm_passwd=input("Enter the Admin Password : ")
        if adm_passwd=='admin':
            print("Access Guaranteed")
            while True:
                read_file()
                ip=input("\nEnter\n1 To Insert New User\n2 To Delete a User\n3 To exit : ")
                if ip=='1':
                    nuser=input("Enter Name of New User : ")
                    pin=input("Enter Pin  : ")
                    balance=input("Enter Balance of New User : ")
                    ws.write(rs.nrows,0,nuser)
                    ws.write(rs.nrows,1,int(pin))
                    ws.write(rs.nrows,2,int(balance))
                    print("Database Updated")
                elif ip=='2':
                    user=input("Enter the user name : ")
                    pin=input("Enter Pin of the user : ")
                    i=0
                    for i in range(1,rs.nrows):
                        if rs.cell_value(i,0)==user and rs.cell_value(i,1)==int(pin):
                            ws.write(i,0,'Deleted')
                            ws.write(i,1,'Deleted')
                            ws.write(i,2,'Deleted')
                            print("USER Data Deleted\nDatabase Updated")
                            break
                    if(i+1==rs.nrows):
                        print('Either User or Pin is not Valid')
                elif ip=='3':
                    break
                else:
                    print("Invalid Input")
                wb.save('database_atm.xls')
        
    elif person=='2':
        print("I am User")
        attempt=1
        while attempt<=3:
            euser=input("Enter Your Name : ")
            pin=input("Enter Your Pin : ")
            for i in range(1,rs.nrows):
                if rs.cell_value(i,0)==euser and rs.cell_value(i,1)==int(pin):
                    while True:
                        read_file()
                        task=input("\nEnter\n1. Withdrawl\n2. Deposit\n3. Check Balance\n4. Exit\t:")
                        if task=='1':
                            wd_amt=input("Enter the Amount : ")
                            if int(wd_amt)<=rs.cell_value(i,2):
                                print("Take your Amount")
                                a_amt=rs.cell_value(i,2)-int(wd_amt)
                                ws.write(i,2,a_amt)
                                print("Available Balance : ",a_amt)
                            else:
                                print("Insufficient Balance")
                        elif task=='2':
                            d_amt=input("Enter the Amount : ")
                            a_amt=rs.cell_value(i,2)+float(d_amt)
                            ws.write(i,2,a_amt)
                            print("Available Balance : ",a_amt)
                        elif task=='3':
                            print("Available Balance : ",rs.cell_value(i,2))
                        elif task=='4':
                            break
                        else:
                            print("Invalid Input")
                        wb.save('database_atm.xls')
                    break
            if(i+1==rs.nrows):
                print('Either User or Pin is not Valid')
            else:
                break
            attempt+=1
        if attempt==4:
            print("Too Many Attempts")
    elif person=='3':
        break
    else:
        print("Invalid Input")

#ws.write(5,0,'Jai')
#ws.write(5,1,4513)
#ws.write(5,2,8769)

