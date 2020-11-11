#! python3
# bulletPointAdd.py - Adds Wikipedia bullet points to the start
# of each lin of text on the clipboard

import pyperclip

text = pyperclip.paste()

# Seperate line and add stars at the start of each lines
lines = text.split('\n')

for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)
pyperclip.copy(text)
