passwordFile = open('passwrd.txt')
secretPassword = passwordFile.read()
print('Enter password')
typedPassword = input()
if typedPassword == secretPassword:
    print("access granted")
    if typedPassword == '12345':
        print("this password is one that idiot use on their luggage or simple 123 which is even more worse")
else:
   print("access denied!!!!!")