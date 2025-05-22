def ev_satis_fişyati_tahmin(oda_sayisi, genslik, muhit):
    """
    Bu fonksiyon, ev satış fiyatını tahmin etmek için kullanıcıdan veri alır ve
    basit bir formül kullanarak tahmin yapar.
    """


# bulunduğum bölge ortalama metrekare fiyatı 2000
metrakare_fiyati = 2000

if muhit == "kepez":
    metrakare_fiyati = 2500
elif muhit == "konyaaltı":
    metrakare_fiyati = 3000
elif muhit == "antalya":
    metrakare_fiyati = 3500

# evin büyüklüğü 100 metrekare
fiyat = metrakare_fiyati * genslik

# oda sayısıne göre

if oda_sayisi == 0:
    # studyo daireler daha ucuz
    fiyat = fiyat * 0.8
else:
    # oda sayısı arttıkça fiyat artar
    fiyat = fiyat + (oda_sayisi * 1000)

return fiyat
