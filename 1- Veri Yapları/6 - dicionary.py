# sözlükler key value çiftlerinden oluşur
# değiştirilebilir
# sıralı (Python 3.7 ve üzeri)
# anahtarlar benzersizdir (her anahtar sadece bir kez kullanılabilir)

disctionary = {"name" : "Mustafa", 
               "age" : 30 , 
               "city" : "Antalya"}

disctionary["name"] # "Mustafa" döner

#Sorgulama yapma
"Mustafa" in disctionary # False döner (key'e göre sorgulama yapıldığı için)

"Mustafa" in disctionary.values() # True döner

# keye göre value erişme
disctionary["name"] # "Mustafa" döner
disctionary.get("name") # "Mustafa" döner

#value değiştirme
disctionary["name"] = "Zeynep" # "Zeynep" döner

#Tüm keylere erişme
disctionary.keys() # dict_keys(['name', 'age', 'city']) döner

#Tüm value'lara erişme
disctionary.values() # dict_values(['Zeynep', 30, 'Antalya']) döner

#Tüm key-value çiftlerine erişme
disctionary.items() # dict_items([('name', 'Zeynep'), ('age', 30), ('city', 'Antalya')]) döner

#update
disctionary.update({"name" : "Zeynep"}) # {"name" : "Zeynep", "age" : 30 , "city" : "Antalya"} döner

#Silme
disctionary.pop("name") # "Zeynep" siler ve disctionary = {"age" : 30 , "city" : "Antalya"} olur
disctionary.popitem() # son elemanı siler ve döner






