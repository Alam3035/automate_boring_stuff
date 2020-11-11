import re

batRegex = re.compile(r'Bat(wo)?man')

mol1 = batRegex.search('The Adventure of Batman')

print(mol1.group())

mol2 = batRegex.search('The Adventure of Batwoman')

print(mol2.group())