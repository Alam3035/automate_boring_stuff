import random, time, copy

width = 60
heigth = 20

nextCell = []
for x in range(width):
    column = []
    for y in range(heigth):
        if random.randint(0,1) == 0:
            column.append('#')
        else:
            column.append(' ')

        nextCell.append(column)

    while True:
        print('\n\n\n\n\n')
        currentCell = copy.depcopy(nextCell)
        