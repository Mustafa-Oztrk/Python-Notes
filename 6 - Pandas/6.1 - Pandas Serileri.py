# pandas series
import pandas as pd

s = pd.Series([1, 2, 3, 4, 5])  # create a pandas series index bilgisi var 
type(s)
s.dtype # dtype: int64 içindeki verinin türü
s.index # index bilgisi
s.values # değer bilgisi numpty array olarak döner
s.size # uzunluk bilgisi
s.head() # ilk 5 değeri al
s.tail() # son 5 değeri al

s[0] # 0. indexteki değeri al
s[0:3] # 0'dan 3'e kadar olan değerleri al
