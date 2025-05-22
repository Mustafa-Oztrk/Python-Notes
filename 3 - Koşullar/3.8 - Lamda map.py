# lambda , map, filter, reduce
# lambda : tek satırlık fonksiyon tanımlamak için kullanılır.
# map : bir fonksiyonu bir iterable (liste, tuple, set) üzerinde uygular.
# filter : bir fonksiyonu bir iterable üzerinde uygular ve True olanları döner.
# reduce : bir fonksiyonu bir iterable üzerinde uygular ve tek bir değer döner.

# lambda : tek satırlık fonksiyon tanımlamak için kullanılır.

new_sum = lambda x, y: x + y
print(new_sum(5, 10))  # 15

# map : bir fonksiyonu bir iterable (liste, tuple, set) üzerinde uygular.
salaries = [1000, 2000, 3000, 4000, 5000]
list(map(lambda x: x * 1.5, salaries))  # [1500.0, 3000.0, 4500.0, 6000.0, 7500.0]

# filter : bir fonksiyonu bir iterable üzerinde uygular ve True olanları döner.
salaries = [1000, 2000, 3000, 4000, 5000]
list(filter(lambda x: x > 3000, salaries))  # [4000, 5000]

# reduce : bir fonksiyonu bir iterable üzerinde uygular ve tek bir değer döner.
from functools import reduce
salaries = [1000, 2000, 3000, 4000, 5000] #


list_store= [1,2,3,4]
reduce(lambda a,b: a+b, list_store)

