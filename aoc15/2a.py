data = open('r_input.txt').read().splitlines()
total_wrap = 0

for i in data:
    l,w,h = map(int,i.split('x'))
    total_wrap += 2*(l*w + w*h+h*l) + min(l*w,w*h,h*l)

print(total_wrap)
