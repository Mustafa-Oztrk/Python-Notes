eski_fiyat = {'süt': 1.02, 'kahve': 2.5, 'ekmek': 2.5}

dolar_tl = 0.76
yeni_fiyat = {item: value*dolar_tl for (item, value) in eski_fiyat.items()}
print(yeni_fiyat)