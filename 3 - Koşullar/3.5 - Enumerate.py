# Enumerate : otomatik olarak bir nesne içindeki elemanları döngü ile gezmek için kullanılır.

students = ["Zeynep", "Mustafa", "Ege", "Mehmet"]
for student in students:
    print(student)

for index, student in enumerate(students):
    print(index, student)



T = []
C = []
# cift öğrencileri ayrı tek öğrencileri ayrı yazdırma
for index, student in enumerate(students):
   
    if index % 2 ==  0:
        C.append(student)
    else: 
        T.append(student)

print("Çiftler: ", C)
print("Tekler: ", T)