"""
this code works for the test cases
"""
data = open('r_input.txt').read().splitlines()
data = data[0]
north_south_counter = 0
east_west_counter = 0
total_houses = 2

for i in data:
    if i == '^':
        north_south_counter +=1
    elif i == 'v':
        north_south_counter -=1
    elif i == '>':
        east_west_counter +=1
    elif i == '<':
        east_west_counter -=1

    if north_south_counter !=0 or east_west_counter !=0:
        total_houses +=1

    if north_south_counter + east_west_counter == 0:
        total_houses -=1

print(total_houses)
