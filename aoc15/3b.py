"""
sources:https://github.com/ChrisPenner/Advent-Of-Code-Polyglot/blob/master/2015/python/03/part2.py
sources:https://gitlab.com/gregor_ulm/advent_of_code_2015/blob/master/03/part2.py
"""
from collections import defaultdict

houses = defaultdict(int)

def house_counter(data):
    global houses
    north_south_counter = 0
    east_west_counter = 0
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
    return total_houses

if __name__ == '__main__':

    data = open('r_input.txt').read().splitlines()
    robo_santa_data = []
    normal_santa_data = []

    for i,val in enumerate(data[0]):
        if i%2 == 0:
            normal_santa_data.append(val)
        else:
            robo_santa_data.append(val)


    house_counter(robo_santa_data)
    print(house_counter(normal_santa_data))
