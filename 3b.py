import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('out.txt') # len(data) = 1500
data = data[~(data==0).all(1)] #len(data) = 999
uniques = []
for i in data:
    for j in set(i):
        if j != 0 and np.isnan(j) == False:
            uniques.append(j)

uniques = (uniques)
uniques = [i for i in uniques if i < 240]

# answer less than 242

print(max(uniques))
# plt.plot([i for i in range(len(uniques))],uniques)
# plt.show()
