# iloc & loc yapıları 

import pandas as pd
import seaborn as sns
pd.set_option("display.max_columns", None) # tüm sütunları göster
df =  sns.load_dataset("titanic") # seaborn kütüphanesinden veri seti yükleme
dat = df.head() # ilk 5 satırı al
print(dat) # ilk 5 satırı yazdır


# iloc & loc yapıları

# iloc: integer location, index numarasına göre seçim yapar
# loc: label location, index etiketine göre seçim yapar

# iloc yapısı ile seçim yapma
df.iloc[0:3] # 0'dan 3'e kadar olan satırları al
df.iloc[0,0] # 0. satır ve 0. sütundaki değeri al

#loc yapısı ile seçim yapma

df.loc[0:3] # 0'dan 3 kadar olan satırları al
df.loc[0:3, "age"] # 0'dan 3'e kadar olan satırların age sütununu al
df.loc[0:3, ["age", "alive"]] # 0'dan 3'e kadar olan satırların age ve alive sütununu al