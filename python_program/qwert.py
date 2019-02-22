a=open('email.txt')
msg = MIMEText(a.read())
print(msg)