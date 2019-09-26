print("\tWelcome to Encryption Center\n")
word=input("Enter the Word you want to encrypt : ")
key=5
print("Encrypting...\n")
temp=''
for w in word:
    a=ord(w)
    a+=key
    ch=chr(a)
    temp=temp+ch
print("Your encrypted word is ",temp)
t=True
while t:
    i=input("Do you want to decryt the word (0 for NO 1 for YES) : ")
    if i=='1':
        allowed=1
        while allowed<=3:
            key_ask=int(input("Give you key : "))
            if key==key_ask:
                print("Decrpting....\n")
                temp1=''
                for w in temp:
                    a=ord(w)
                    a-=key
                    ch=chr(a)
                    temp1=temp1+ch
                print("Your word is ",temp1)
                allowed=5
            else:
                allowed+=1
                print("Enter correct key")
    elif i=='0':
        t=False
        print("Thank you for choosing our service")
    else:
        print("wrong input")
    

