# değişkenler üzerinde işlem yapma
import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic") # seaborn kütüphanesinden veri seti yükleme
pd.set_option("display.max_columns", None) # tüm sütunları göster 
data = df.head() # ilk 5 satırı al
print(data) # ilk 5 satırı yazdır

"age" in df # age değişkeni veri setinde var mı
df["age"].head() # age değişkeninin ilk 5 değerini al
df.age.head() # age değişkeninin ilk 5 değerini al


df[["age", "alive"]].head() # age ve alive değişkeninin ilk 5 değerini al

col_names = ["age", "alive", "adult_male"] # değişken isimlerini liste olarak tanımla
datset = df[col_names].head() # değişken isimlerini kullanarak ilk 5 satırı al
print(datset) # ilk 5 satırı yazdır

df["age2"] = df["age"] * 2 # age değişkeninin 2 katını al ve yeni bir değişken oluştur

df.drop("age2", axis=1, inplace=True) # age2 değişkenini kalıcı olarak sil

df.loc[:, ~df.columns.str.contains("age")] # age içeren tüm değişkenleri al "~" bunun dışında kalanları al