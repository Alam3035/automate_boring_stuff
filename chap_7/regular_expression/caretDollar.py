import re

beginWithHello = re.compile(r'^Hello')

print(beginWithHello.search('Hello, World!'))

print(beginWithHello.search('He said hello.') == None)

endsWithNumber = re.compile(r'\d$')

print(endsWithNumber.search('your number is 42'))

print(endsWithNumber.search('Your number is forty two.'))