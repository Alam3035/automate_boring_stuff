import sys, time

indent = 0
indentIncreasing = True

try:
    while True:
        print(' '*indent, end='')
        print('********')
        time.sleep(0.1) # sleep for 0.1 second

        if indentIncreasing:
            indent = indent + 1
            if indent == 5:
                indentIncreasing = False
        else:
            indent = indent - 1
            if indent == 0:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()

