from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

data = []
with open('inp.txt','r') as file:
    for i in file:
        data.append(i)

ans = []
for i in data:
    for j in range(len(data)):
        if similar(i,data[j]) > 0.96 and similar(i,data[j]) != 1:
            ans.append([i,data[j]])
# print(ans)
a1 = ans[0]
a2 = ans[1]
print(a1)
print(a2)

for i in a1[0]:
    for j in a1[1]:
        if i != j:
            print(i)
            break
for i in a2[0]:
    for j in a2[1]:
        if i != j:
            print(i)
            break
