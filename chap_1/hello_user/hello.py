# This program says hello and ask for users name. 
print("Hello from the program!")
print("What is your name?")
myname = input()
print("hello " + myname, ". How are you?")
print("also the length of your name is " + str(len(myname)))
print("whats you age?")
age = input()
print("You will be "+str(int(age)+23)+" in 23 years")