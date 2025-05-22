# matemetiklse işlemler
# tüm değerler üzerinde işlem yapar
import numpy  as np

v = np.array([1, 2, 3, 4])

# Çarpma işlemi
v*5
# Toplama işlemi
v+5
# Çıkarma işlemi
v-5
# Bölme işlemi
v/5
# Mod alma işlemi
v%2
# Üst alma işlemi
v**2
# Karekök alma işlemi
np.sqrt(v)
# Logaritma alma işlemi
np.log(v)
# Sinüs alma işlemi
np.sin(v)
# Kosinüs alma işlemi
np.cos(v)
# Tanjant alma işlemi
np.tan(v)

# Aritmetik işlemler
# Toplama işlemi
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = a + b
# Çıkarma işlemi
d = a - b
# Çarpma işlemi
e = a * b
# Bölme işlemi
f = a / b
# Mod alma işlemi
g = a % b
# Üst alma işlemi
h = a ** b
# Karekök alma işlemi
i = np.sqrt(a)
# Logaritma alma işlemi
j = np.log(a)
# Sinüs alma işlemi
k = np.sin(a)
# Kosinüs alma işlemi
l = np.cos(a)
# Tanjant alma işlemi
m = np.tan(a)
# Aritmetik işlemler


# iki bilinmeyenli denklemler
# 2x + 3y = 6
# 4x + 5y = 10
a = np.array([[2, 3], [4, 5]])
b = np.array([6, 10])
x, y = np.linalg.solve(a, b)
print("x:", x)
print("y:", y)
