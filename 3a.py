import re
from collections import defaultdict

counter = 0
data = open('r_input.txt').read().splitlines()
# print(file_ptr)
rgx = re.compile(r"^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$")
dict = defaultdict(int)
id_ans = 0

for line in data:
    id,x,y,w,h = map(int,rgx.match(line).groups())
    for i in range(x,x+w):
        for j in range(y,y+h):
            dict[(i,j)] +=1


for claim in data:
    id, x, y, w, h = map(int, rgx.match(claim).groups())
    overlap_index = None
    for i in range(x, x + w):
        for j in range(y, y + h):
            if dict[(i, j)] > 1:
                overlap_index = id
                continue
    if not overlap_index:
        id_ans = id
        break


print(id_ans)
# print(dict)
