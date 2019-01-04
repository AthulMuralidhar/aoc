data = open('r_input.txt').read().splitlines()
total_ribbon = 0

for i in data:
    l,w,h = map(int,i.split('x'))
    total_ribbon += 2*(l+w+h - max(l,w,h)) + l*w*h

print(total_ribbon)
