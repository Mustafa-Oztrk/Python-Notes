# Set
# Değiştirilebilir (mutable) veri yapısıdır.
# Sırasızdır (unordered)
# Tekrar eden elemanları kabul etmez (unique)
# Set veri yapısı, bir küme gibi düşünülebilir. Yani, bir küme içinde tekrar eden elemanlar yoktur.

set1 = {1,  3,  5}
set2 = set([1,  3, 4]) # set() fonksiyonu ile de set oluşturulabilir.

# set1'de olup set2'de olmayan elemanları bulma
set1.difference(set2) # {5} döner

#set2'de olup set1'de olmayan elemanları bulma
set2.difference(set1) # {4} döner

# iki kümede de olan elemanları bulma
set1.symmetric_difference(set2) # {4, 5} döner

# iki kümenin kesişimini bulma
set1.intersection(set2) # {1, 3} döner

