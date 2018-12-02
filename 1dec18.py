"""
AOC day 1
using Beautiful Soup implimentation to get data from AOC website
Language: Python 3+
AM
"""
a = []
with open('inp.txt','r') as file:
    a = 0
    while True:
        for i in file:
            if i.rstrip('\n'):
                a.append(int(i))


print(a)
# print(b)
