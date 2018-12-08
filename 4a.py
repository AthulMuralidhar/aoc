import numpy as np
from datetime import datetime

data = []
with open('inp.txt','r') as file:
    for i in file:
        i = i.strip()
        i = i.split()
        if not i:
            break
        date = datetime.strptime("".join(i[:2]),"[%Y-%m-%d%H:%M]")
        data.append((date," ".join(i[2:])))

data = sorted(data)
sleep_time = []
time_counter = 0

for i in data:
    j = i[1]
    if j.find("Guard") is not -1:
        name = j
    if j.find("falls asleep") is not -1:
        start_min = i[0].time()
        time_counter = i[0]
    if j.find("wakes up") is not -1:
        time_counter = i[0] - time_counter  #assuming that the data is sorted!!
        sleep_time.append((name,start_min,time_counter))
        time_counter = 0

sleep_delta = [i[2] for i in sleep_time]
print(np.argmax(sleep_delta))
print(sleep_time[52])
