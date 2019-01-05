from collections import defaultdict

data = open('r_input.txt').read().splitlines()
data = data[0]
robo_santa_houses = defaultdict(int)
normal_santa_houses = defaultdict(int)
robo_santa_pos = (0,0)
normal_santa_pos = (0,0)

robo_santa_houses[robo_santa_pos] = 1
normal_santa_houses[normal_santa_pos] = 1

for i,val in enumerate(data):
    if (i+1)%2 != 0:
        """ these are santa's coordinates"""
        if val == '^':
            normal_santa_pos[0] +=1
        elif val == 'v':
            normal_santa_pos[0] -=1
        elif val == '>':
            normal_santa_pos[1] +=1
        elif val == '<':
            normal_santa_pos[1] -=1
    else:
        """ these are robo santa's coordinates"""
        if val == '^':
            robo_santa_pos[0] +=1
        elif val == 'v':
            robo_santa_pos[0] -=1
        elif val == '>':
            robo_santa_pos[1] +=1
        elif val == '<':
            robo_santa_pos[1] -=1

    if robo_santa_pos in robo_santa_houses.keys():
        robo_santa_houses[robo_santa_pos] +=1
    else:
        robo_santa_houses[robo_santa_pos] +=1

    if normal_santa_pos in normal_santa_houses.keys():
        normal_santa_houses[normal_santa_pos] +=1
    else:
        normal_santa_houses[normal_santa_pos] +=1
