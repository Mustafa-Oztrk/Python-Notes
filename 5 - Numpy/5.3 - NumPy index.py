# index seçimi (index selelection)
import numpy as np
a =  np.random.randint(10, size = 10)
print(a)
print(a[0]) # 0. index
print(a[0:5]) # 0. index ile 5. index arası sol taraf dahil sağ taraf hariç
print(a[0:5:2]) # 0. index ile 5. index arası 2'şer atlayarak
a[0] = 100 # 0. indexi 100 yap
print(a)

m =  np.random.randint(10,size =(3,5))  # 3 satır 5 sütun
print(m)

m[0, 5] = 100 # 0. satır 0. sütun
m [2,5] = 200 # 2. satır 0. sütun 200 değerini atama
m[1, :] # 1. satır tüm sütunlar
m[:, 1] # tüm satırlar 1. sütun


