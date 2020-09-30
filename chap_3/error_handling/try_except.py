def spam(number):
    try:
        return 42 / number
    except ZeroDivisionError:
        print('Error: invalid argument')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))