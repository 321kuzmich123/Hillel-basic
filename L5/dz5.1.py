import keyword
import string
from string import punctuation

name = input('Input name: ')
res = True
punctuation = string.punctuation.replace('_', '')

if name[0].isdigit():
    res = False
elif name in keyword.kwlist:
    res = False
elif any(i in punctuation for i in name):
    res = False
elif '__' in name:
    res = False
elif not all(i.islower() or i.isdigit() or i == '_' for i in name):
    res = False
print(res)