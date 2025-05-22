# şirket çalışanlarının biligilerini, departmanlarını ve maaşlarını tutan ayrı ayrıo listeler oluşturun
# verileri kullanıcıdan alınmalıdır

persone = int( input(("Çalışan sayısını girin: ")))
departman = []
maas = []
name = []

for i in range(persone):
    name.append(input(str("Adı girin: ")))
    departman.append(input(str("Departmanı girin: ")))
    maas.append(int(input("Maaşını girin: ")))
    
result = list(zip(name, departman, maas))
print("Çalışan Bilgileri:")
for i in result:
    print(f"adı: {i[0]}", 
          f"departmanı: {i[1]}",
          f"maaşı: {i[2]}")
