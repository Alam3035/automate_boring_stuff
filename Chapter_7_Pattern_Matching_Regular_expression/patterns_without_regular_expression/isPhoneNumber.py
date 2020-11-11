def isPhoneNumber(text):
    if len(text) != 9:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    
    if text[4] != ' ':
        return False

    for i in range(5, 9):
        if not text[i].isdecimal():
            return False

    return True

print('Is 1234 5678 a phone number?')
print(isPhoneNumber('1234 5678'))
print('Is Moshi Moshi a phone number?')
print(isPhoneNumber('Moshi Moshi'))

message = 'Call me at 1234 5678 tmr. 8765 4321 is my office.'

for i in range(len(message)):
    chunk = message[i:i+9]
    if isPhoneNumber(chunk):
        print('Phone number found: '+ chunk)

print('Done')
