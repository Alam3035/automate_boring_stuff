import re

phoneNumRegex = re.compile(r'(\+\d\d\d) (\d\d\d\d \d\d\d\d)')

mo = phoneNumRegex.search('My number is +852 1234 5678.')

print('phone number found: ' + mo.group())

print(mo.group(0))

print(mo.group(1))

print(mo.group(2))

