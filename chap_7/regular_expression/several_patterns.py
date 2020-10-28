import re

batRegrex = re.compile(r'Bat(man|mobile|copter|bat)')

mo = batRegrex.search('Batmobile lost a Batman')

print(mo.group())

print(mo.group(1))

