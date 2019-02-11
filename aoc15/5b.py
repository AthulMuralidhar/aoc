nice_counter = 0
data = open('t_input.txt').read().splitlines()
repeat_counter = 0
# print(data)

for value in data:
    chunks = [value[i:(i+2%len(value))] for i in range(len(value))]
    print(chunks)
    print()

    for index,chunk in enumerate(chunks):
        # print(index,chunk)
        # print(chunks.remove(index))
        if chunk in chunks.remove(index):
            print(chunks.remove(index))
            repeat_counter +=1
    break

print()
print(repeat_counter)
