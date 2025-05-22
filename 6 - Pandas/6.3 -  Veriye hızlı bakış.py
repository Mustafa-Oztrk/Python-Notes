# veriye hızlı bakış (Quick Look at Data)

import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic") # seaborn kütüphanesinden veri seti yükleme
df.head() # ilk 5 satırı al
print(df) # veri setini yazdır
df.shape # veri setinin boyutunu al
df.info() # veri setinin bilgilerini al
df.describe() # veri setinin istatistiksel bilgilerini al
df.describe.T # transpoze et (satır ve sütunları değiştir) daha iyi okunabilir
df.columns # veri setinin sütun isimlerini al
df.index # veri setinin index bilgilerini al
df.dtypes # veri setinin veri türlerini al
df.isnull().values.any() # veri setinde eksik değer var mı
df.isnull().sum() # veri setinde eksik değerlerin toplamını al
df["age"].head() # age sütununun ilk 5 değerini al
df["sex"].value_counts # kaçar tane olduğunu al