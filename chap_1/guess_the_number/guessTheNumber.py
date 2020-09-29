import random

secretNumber = random.randint(1,20)

for guessTaken in range(1,7):
    print("take a guess")
    guess = int(input())

    if guess < secretNumber:
        print("too low bro")
    elif guess > secretNumber:
        print("too high bro")
    else:
        break

if guess == secretNumber:
    print("good job, you guess my number in "+str(guessTaken)+" guesses!")
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))

