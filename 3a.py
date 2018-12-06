import numpy as np

data = []
with open('inp.txt','r') as file:
    for i in file:
        data.append(i.rstrip())

data = data[:-1]
# print(data)
# print(len(data))
for n,d in enumerate(data):
    key,carpet = d.split(':')
    key = key.split('@')[1]
    key = (int(key.split(',')[0]),int(key.split(',')[1]))
    carpet = (int(carpet.split('x')[0]),int(carpet.split('x')[1]))
    data[n] = (key,carpet)

# print(data)

matrix = np.zeros((1500,1500))
counter = 0
nan_counter = 0

for d in data:
    counter +=1
    for i in range(1500):
        for j in range(1500):
            if i in range(d[0][0],d[0][0]+d[1][0]) and j in range(d[0][1],d[0][1]+d[1][1]):
                    if matrix[j,i] == 0:
                        matrix[j,i] = counter
                    else:
                        matrix[j,i] = np.nan

np.savetxt('out.txt',matrix)
