import string

fileptr = open('input.txt','r')
outptr = open('output.txt','a')
max_length = (9,9) #arbritrary matrix dimensions
counter = 0

for line in fileptr:
    outptr.seek(0,0)
    data = list(map(int,line.strip().split(',')))
    for i in range(max_length[0]):
        for j in range(max_length[1]):
            if i == data[1] and j == data[0]:
                outptr.write(string.ascii_uppercase[counter])
                counter +=1
            else:
                outptr.write('.')
        outptr.write('\n')
