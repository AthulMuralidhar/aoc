"""
AOC day 1
using Beautiful Soup implimentation to get data from AOC website
Language: Python 3+
AM
"""
# import ipdb; ipdb.set_trace()
b = []
a = 0
c=[]
# b.append(a)
counter = 0

while True:
    with open('inp.txt','r') as file:
        for i in file:
            if i.rstrip('\n'):
                a+=int(i)
                b.append(a)
            if len(b) != len(set(b)):
                c = b
                break
    if c:
        break
print(b[-1])
# print()
