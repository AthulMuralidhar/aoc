import numpy as np
from datetime import datetime
from collections import defaultdict

data = open('t_input.txt').read().splitlines()
record = defaultdict(list)
# print(data)


for line in data:
    record[datetime.strptime("".join(line[:18]),'[%Y-%m-%d %H:%M]')] = line[18:]
print(sorted(record))

# with open('inp.txt','r') as file:
#     for i in file:
#         i = i.strip()
#         i = i.split()
#         if not i:
#             break
#         date = datetime.strptime("".join(i[:2]),"[%Y-%m-%d%H:%M]")
#         data.append((date," ".join(i[2:])))

#
# data = sorted(data)
# sleep_time = []
# guard_names = []
# time_counter = 0
#
# for i in data:
#     j = i[1]
#     if j.find("Guard") is not -1:
#         name = j
#         guard_names.append(j)
#     if j.find("falls asleep") is not -1:
#         start_min = i[0].time()
#         time_counter = i[0]
#     if j.find("wakes up") is not -1:
#         time_counter = i[0] - time_counter  #assuming that the data is sorted!!
#         sleep_time.append((name,start_min,time_counter))
#         time_counter = 0
#
# # print(sleep_time)
# guard_names = set(guard_names)
# # print(guard_names)
# cumulative_sleep_time = []
#
# for i in guard_names:
#     cum_sum = datetime.now()-datetime.now()
#     for j,k,l in sleep_time:
#         if i == j:
#             cum_sum +=l
#     cumulative_sleep_time.append((i,cum_sum))
#
# # print(max(cumulative_sleep_time)) #guard 983
#
# for i,j,k in sleep_time:
#     if i.find('Guard #983') is not -1:
#         print(i,j,k)
# # sleep_delta = [i[1] for i in cumulative_sleep_time]
# # print(np.argmax(sleep_delta))
# # print(cumulative_sleep_time[18])
