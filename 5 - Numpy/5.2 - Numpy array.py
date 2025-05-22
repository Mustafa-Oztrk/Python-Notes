import numpy as np

np.array([1, 2, 3, 4])

print(type(np.array([1, 2, 3, 4])))

# girilen sayı adedince 0 olutşurma 
np.zeros(5, dtype=int)


# rasgele sayı oluşturma
np.random.randint(1, 10, size = 5) # 1 ile 10 arasında 5 tane rasgele sayı oluştur

# normal dağılım
normal = np.random.normal(10,4, (3, 4)) # 10 ortalama, 4 standart sapma, 3 satır 4 sütun
print(normal)


##### Özeliklerii #####

a = np.random.randint(10, size = 5) # 0 ile 10 arasında 5 tane rasgele sayı oluştur

a.ndim # boyut sayısı 
a.shape # boyutları
a.size # eleman sayısı
a.dtype # veri tipi
a.itemsize # eleman boyutu


### Reshape ###
a = np.random.randint(10, size= 10) # 0 ile 10 arasında 10 tane rasgele sayı oluştur
a = np.random.randint(10, size= 10).reshape(2, 5) # 0 ile 10 arasında 10 tane rasgele sayı oluştur ve 2 satır 5 sütun yap

