import re

counter = 0
data = open('r_input.txt').read().splitlines()
# print(file_ptr)
rgx = re.compile(r"^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$")
dict = {}
id_ans = 0

for line in data:
    id,x,y,w,h = map(int,rgx.match(line).groups())
    for i in range(x,x+w):
        for j in range(y,y+h):
            if not (i,j) in dict.keys():
                dict[(i,j)] = id
                continue
            elif dict[(i,j)] < id:
                dict[(i,j)] +=1

            if dict[(i,j)] == id:
                id_ans = id
print(id_ans)
# print(dict)
