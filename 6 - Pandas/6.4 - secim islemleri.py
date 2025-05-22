# seçim işlemleri
import pandas as pd
import seaborn as sns

df = sns.load_daataset("titanic") # seaborn kütüphanesinden veri seti yükleme
df.head() # ilk 5 satırı al

df.index # index bilgisi
df[0:13] # 0'dan 13'e kadar olan satırları al
df.drop(0, axis=0) # 0. satırı sil
df.drop([0, 1, 2]) # 0, 1 ve 2. satırları sil
df.drop([0, 1, 2], axis=0) # 0, 1 ve 2. satırları sil
# df.drop([0, 1, 2], axis=0, inplace=True) # 0, 1 ve 2. satırları sil ve kalıcı olarak değişiklikleri kaydet

# değişkeni indexe çevirme 
df["age"].head() # age sütununun ilk 5 değerini al
df.age.head() # age sütununun ilk 5 değerini al
df.index # index bilgisi

df.index = df["age"] # age sütununu index olarak ayarla
df.drop("age", axis=1, inplace = True) # age sütununu sil

df["age"] = df.index # indexteki değeri age sütununa ata                                        
df.head() # ilk 5 satırı al


df.reset_index().head() # indexi sıfırla ve ilk 5 satırı al