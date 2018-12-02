b = []
c = []
with open('inp.txt','r') as file:
    for i in file:
        for j in i:
            if i.count(j) == 2:
                b.append(i)
            if i.count(j) == 3:
                c.append(i)
            if i.count(j) > 3:
                print('higher than 3')

# b = set(a)
print(len(set(b))*len(set(c)))
