import numpy as np

a = np.arange(25).reshape(5,5)

print("kelt:", a[4, 0:5])

print("puna:", a[0:-1, 1:-1:2])#, [1, 3]])

print("sini:", a[1:-1:2, 0:-1:2])