# Satatement 
# Statement: Bir işlemi gerçekleştiren bir komut.

def say_hi():
    print("Hello")
    print("hi")
    print("Merhaba")

say_hi() # say_hi fonksiyonunu çağırır ve "Hello" ve "hi" yazdırır.


def say_hi(String):
    print(String)
    print("hi")
    print("Merhaba")

say_hi("Hello") 


def mulyiplication(a, b):
    c = a* b 
    print(c)

mulyiplication(2, 3) # 6 döner


# girilen değeleri liste içinde saklayıp döndüren fonksiyon

list_strore = []
def list_strore_fun(a, b):
    c = a * b
    list_strore.append(c)
    print(list_strore)

list_strore_fun(5,24) # [120] döner
list_strore_fun(24,30) # [120, 720] döner