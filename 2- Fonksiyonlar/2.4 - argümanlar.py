# ön tanımlı argümanlar/ parametreler
# # Fonksiyon tanımlarken argümanlara varsayılan değerler atayabiliriz. Bu sayede fonksiyonu çağırırken bu argümanları vermek zorunda kalmayız.

def divide(x,y):
    print(x/y)

divide(10,2) # 5 döner

def divide(x,y=2): # y argümanına varsayılan değer atandı.
    print(x/y)

divide(10) # 5 dönersdx 


def cal(varm,moisture,charge):
    print(varm + moisture) / charge

cal(92,10,78)