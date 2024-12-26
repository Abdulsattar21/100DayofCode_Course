import smtplib

my_email = "asdfghkjjewirwiuriwuriwu@gmail.com"
password = "pdisrmyrchrlraca"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls() # for securing the connection
connection.login(user=my_email, password= password)
connection.sendmail(from_addr=my_email, to_addrs="abdasierk1@gmail.com", msg="Hello")
connection.close()