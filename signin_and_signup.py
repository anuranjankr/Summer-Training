import time
class User:

    def __init__(self, username=None, password=None, mobile_no=None, email_id=None):
        self.username = username
        self.password = password
        self.mobile_no = mobile_no
        self.email_id = email_id

users=[]

# Function to validate the password 
def password_check(passwd): 
      
    SpecialSym =['$', '@', '#', '%'] 
    val = True
      
    if len(passwd) < 6: 
        print("length should be at least 6") 
        val = False
          
    if len(passwd) > 20: 
        print("length should be not be greater than 8") 
        val = False
          
    if not any(char.isdigit() for char in passwd): 
        print("Password should have at least one numeral") 
        val = False
          
    if not any(char.isupper() for char in passwd): 
        print("Password should have at least one uppercase letter") 
        val = False
          
    if not any(char.islower() for char in passwd): 
        print("Password should have at least one lowercase letter") 
        val = False
          
    if not any(char in SpecialSym for char in passwd): 
        print("Password should have at least one of the symbols $@#%") 
        val = False
    if val: 
        return val 
# SIGN IN
def signin():
    allowed1=0
    while True:
        username = input("Username: ")
        allowed1+=1
        if not len(username) > 0:
            print("Username can't be blank")
        if allowed1<3:
            found=0
            for user in users:
                if user.username==username:
                    index=users.index(user)
                    found=1
                    while True:
                        allowed=1
                        password = input("Password: ")
                        if not len(password) > 0:
                            print("Password can't be blank")
                        else:
                            if password == users[index].password:
                                print("Login successfull\n")
                                print("After completing your task.. Enter \'logout\' to exit")
                                while True:
                                    ip=input("....\n")
                                    if ip=='logout':
                                        finished=1
                                        break
                                    else:
                                        print("Please enter \'logout\' to exit..")
                                if finished==1:
                                    break
                            else:
                                print("Invalid password")
                        allowed+=1
                        if allowed>4:
                            print("Too many attempts")
                            break
                    break
        else:
            print("Too many attempts")
            break
        if found==0:
            print("Invalid Username")
        else:
            break
    

# SIGN UP
def signup():
    while True:
        username = input("New username: ")
        if not len(username) > 0:
            print("Username can't be blank")
            continue
        for user in users:
            if user.username==username:
                print("Username already taken")
                break
        else:
            break
    while True:
        password = input("New password: ")
        if not len(password) > 0:
            print("Password can't be blank")
            continue
        valid=password_check(password)
        if not valid:
            continue
        else:
            break
    while True:
        mobile_no = input("Mobile No. : ")
        if len(mobile_no) == 0:
            print("Mobile No. can't be blank")
            continue
        if not len(mobile_no) == 10:
            print("Mobile No. length must be 10")
            continue
        else:
            break
    while True:
        email_id = input("Email : ")
        if not len(email_id) > 0:
            print("Email can't be blank")
            continue
        if not '@' in email_id :
            print("Email must contain \'@\' symbol")
            continue
        else:
            break
    print("Creating account...")
    users.append(User(username, password, mobile_no,email_id))
    time.sleep(1)
    print("Account has been created")

print("\n\t\tWelcome to Training Center")
while True:
    print("\nEnter\n1 Sign IN\n2 Sign UP\n3 Exit")
    ip=input("\nEnter your Choice : ")
    if ip=='1':
        signin()
    elif ip=='2':
        signup()
    elif ip=='3':
        break
    else:
        print("Wrong Input")
