import random,sys

print("ROCK, PAPER, SCISSORS")

print("Whats is your name?")
name = input()

wins = 0
losses = 0
ties = 0

while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))

    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()

        if playerMove == "q":
            sys.exit()
        if playerMove == "r" or playerMove == "p" or playerMove == "s":
            break

    print("Type one of r, p, s or q")

    if playerMove == 'r':
        print(name+' used ROCK')
    elif playerMove == 'p':
        print(name+' used PAPER')
    elif playerMove == 's':
        print(name+' used SCISSORS')

    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = "r"
        print('AI used ROCK')
    if randomNumber == 2:
        computerMove = "p"
        print('AI used PAPER')
    if randomNumber == 3:
        computerMove = "s"
        print('AI used SCISSORS')


    if playerMove == computerMove:
        print('It is a tie!')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1