# veri okuma 
import pandas as pd

# dosya yolu ekleme
df = pd.read_csv("Advertising.csv")

dat = df.head() # ilk 5 satırı al

print(dat) # ilk 5 satırı yazdır
print(df.shape) # veri setinin boyutunu al



import pandas as pd 
df = pd.read_csv("../datasets/Advertising.csv") # veri setini oku
data = df.head() # ilk 5 satırı al
print(data) # ilk 5 satırı yazdır

