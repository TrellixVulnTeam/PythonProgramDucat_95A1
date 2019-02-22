import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.login("baghelhimanshu35@gmail.com", "palsohan738")
msg = "Hello!"
server.sendmail("baghelhimanshu35@gmail.com", "ajeetbissp5@gmail.com", msg)