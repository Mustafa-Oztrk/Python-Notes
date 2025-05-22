# Local Global Değişkenler 
# Local değişken: Fonksiyon içinde tanımlanan değişkenlerdir.
# Global değişken: Fonksiyon dışında tanımlanan değişkenlerdir.
# Local değişkenler sadece fonksiyon içinde geçerlidir.
# Global değişkenler ise programın her yerinde geçerlidir.

list_Store = [1, 2]

def add_element(a, b):
    c = a * b
    list_Store.append(c)
    print(list_Store)

add_element(1,6)