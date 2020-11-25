from replit import db

user = input("enter your name >>>")
passwd = input("enter password >>>")

if user == db["user"] and passwd == db["passwd"]:
  print("logged in ")

else:
  print("Incorrect username and passwd")
