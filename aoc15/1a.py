data = open('r_input.txt').read().splitlines()
close_number = 0
open_number = 0

for i in data[0]:
        if i == '(':
            open_number +=1
        elif i == ')':
            close_number +=1

print(open_number-close_number)
