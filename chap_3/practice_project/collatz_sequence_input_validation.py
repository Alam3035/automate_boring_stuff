def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1

print('Enter Number')
try:
    userNumber = int(input())

    while userNumber != 1:
        userNumber = collatz(userNumber)
except ValueError:
    print("Please insert a number")




