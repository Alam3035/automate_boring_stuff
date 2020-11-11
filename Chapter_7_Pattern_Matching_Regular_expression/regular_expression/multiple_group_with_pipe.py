import re

heroRegex = re.compile(r'Batman|Tina Fey')

mol1 = heroRegex.search('Batman and Tina Fey')

print(mol1.group())

mol2 = heroRegex.search('Tina Fey and Batman')

print(mol2.group())