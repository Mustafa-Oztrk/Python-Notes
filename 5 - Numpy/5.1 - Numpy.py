import numpy as np

a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

# listelerin tüm elemanlarını çarpma
ab =[]

for i in range(0, len(a)):
    ab.append(a[i] * b[i])
print(ab)

# numpy ile çarpma
a = np.array(a)
b = np.array(b)

print(a * b)


arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('1. boyuttaki 2.eleman: ', arr[0, 1])