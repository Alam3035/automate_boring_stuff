# Use global statement to change a global variable
def spam():
    # access the global variable
    global eggs
    # change the global variable in function
    eggs = 'spam'

eggs = 'global'
print(eggs)
spam()
print(eggs)