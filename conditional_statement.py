age = int(input("enter your age:"))

if age >= 18:
    print("you can vote")
    print("you can drive")
else:
    print("you can't vote")


color = input("enter color: ")

if color == "red":
    print("stop")
elif color == "green":
    print("go")
elif color == "yellow":
    print("look")
else:
    print("wrong color for traffic lights")
    

# Quesion :- print the age difference and print it all of the which of them are suitable
age = int(input("enter your age:"))

if (age < 13):
    print("all of them are child")
elif (13<age<18):
    print("all are teenager")
else:    
    print("all are adult")


# Question :- print login sucessfully if we have enter username and password succesfully 
username = input("enter username:-")
password = input("enter passwor:-")

if(username == "admin" and password == "pass"):
    print("Login sucessfully")
elif(username != "admin"):
    print("wrong username")
else:
    print("wrong password")

# Question - if n is a multiple of 5 or not
number = int(input("enter the number:-"))
if(number % 5 == 0):
    print("multiple of 5 ")
else:
    print("not multible of 5")

# Question - print if any number if odd or even
number = int(input("enter a number"))

if(number % 2 == 0):
    print("the number is even")
else:
    print("The number is odd")