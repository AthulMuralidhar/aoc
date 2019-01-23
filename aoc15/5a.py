nice_counter = 0
vowels = list('aeiou')
data = open('t_input.txt').read().splitlines()

for value in data:
    print(value)
    chunks = [value[i:(i+2%len(value))] for i in range(len(value))]
    print(chunks)
