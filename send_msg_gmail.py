import smtplib as s

#creates session(for gmail port 587)
a = s.SMTP('smtp.gmail.com', 587)

# start TLS security
a.starttls()

# gmail and password
a.login("kumaranuranjan652@gmail.com","Caj3ZSPbthisisme")

msg="Hello"

#sending mail
a.sendmail("kumaranuranjan652@gmail.com","anu131298@gmail.com",msg)

print("msg sent")

#session quit
a.quit()
