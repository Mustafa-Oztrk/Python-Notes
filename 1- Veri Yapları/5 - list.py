# listeler
# değiştirilebilir index işlemleri yapılabilir
# kapsayıcıdır
# list = [1, 2, 3, 4, 5] # liste tanımlama

notes = [1,2,3,4,5]
type(notes) # list

# Metinlerden oluşan bir liste
notesSrt =["a", "b", "c", "d", "e"]
type(notesSrt) # list

notes[1] # 2. eleman seçilir

notes[1] = 10 # 2. eleman değiştirilir
notes[0:3] # 0'dan 3'e kadar olan elemanları alır (0,1,2)

len(notes) # liste uzunluğu

notes.append(6) # sona 6 ekler

notes.pop() # son elemanı siler
notes.pop(0) # 0. elemanı siler

notes.insert(0, 10) # 0. index'e 10 ekler

notes.remove(10) # 10'u siler (ilk bulduğu elemanı siler)
notes.sort() # sıralar (küçükten büyüğe)
notes.reverse() # ters çevirir (büyükten küçüğe)
