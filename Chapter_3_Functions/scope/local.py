# Local Variables Cannot Be Used in the Global Scope
# def spam():
#     eggs = 31337

# spam()
# print(eggs)


# Local Scopes Cannot Use Variables in Other Local Scopes
def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0

spam()
