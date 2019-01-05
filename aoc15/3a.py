"""
this code works for the test cases
sources:
https://gitlab.com/gregor_ulm/advent_of_code_2015/blob/master/03/part1.py
"""
from collections import defaultdict

data = open('r_input.txt').read().splitlines()
data = data[0]
north_south_counter = 0
east_west_counter = 0

houses = defaultdict(int)
houses[(north_south_counter,east_west_counter)] = 1

for i in data:
    if i == '^':
        north_south_counter +=1
    elif i == 'v':
        north_south_counter -=1
    elif i == '>':
        east_west_counter +=1
    elif i == '<':
        east_west_counter -=1

    if (north_south_counter,east_west_counter) in houses.keys():
        houses[(north_south_counter,east_west_counter)] +=1
    else:
        houses[(north_south_counter,east_west_counter)] = 1

total_houses = 0
for _ in houses.keys():
    total_houses +=1
print(total_houses)
