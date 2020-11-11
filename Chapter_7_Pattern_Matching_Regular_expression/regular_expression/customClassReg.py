import re

vowelRegex = re.compile(r'[aeiouAEIOU]')

mo = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')

print(mo)

negativeRegex = re.compile(r'[^aeiouAEIOU]')

mo1 = negativeRegex.findall('RoboCop eats baby food. BABY FOOD.')

print(mo1)