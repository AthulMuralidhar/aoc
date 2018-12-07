import numpy as np

data = np.genfromtxt('out.txt')
data = np.trim_zeros(data)
print(data)
