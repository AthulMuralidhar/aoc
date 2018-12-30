data = open('r_input.txt').read().splitlines()
# print(data)

number = 0
# open_number = 0

for index,i in enumerate(data[0]):
        if i == '(':
            number +=1
        elif i == ')':
            number -=1
        if number == -1:
            break

print(index) # 1782: wrong answer, too low
