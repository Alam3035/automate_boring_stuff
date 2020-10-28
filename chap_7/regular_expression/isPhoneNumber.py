import re

phoneNumRegex = re.compile(r'(\+\d\d\d)?\d\d\d\d \d\d\d\d')

mo = phoneNumRegex.search('My number is +852 1234 5678.')

print('phone number found: ' + mo.group())

mo1 = phoneNumRegex.search('My number is 1234 5678.')

print('phone number found: ' + mo1.group())
