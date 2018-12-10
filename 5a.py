
def breaker(data):
    # assumes data is a string type variable
    len_data = len(data)
    for i,j in enumerate(data):
        if j.upper() == data[(i+1)%len_data] or j.lower() == data[(i+1)%len_data]:
            return data[:i]+data[(i+2):]

data1 = []
with open('input.txt','r') as file:
    for i in file:
        data1.append(i.strip())

# print(data)
data = "".join(data1)
print(len(data) )

while True:
    res = data
    data = breaker(data)
    if not data:
        break


print(len(res))
