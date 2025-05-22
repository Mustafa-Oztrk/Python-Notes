# Döngüler

# for döngüsü

students = ["Zeynep", "Mustafa", "Ege"]

for student in students:
    print(student)

# elemanları büyük harfle yazdırma
for student in students:
    print(student.upper())

maas = [1000, 2000, 3000, 4000]

for salary in maas:
 
    print(int(salary * 20/100 + salary))

def new_salary(zam):
     for salary in maas:
         print(int(salary * zam/100 + salary))

new_salary(30)


def new_sall(maas,zamm):
    return int(maas * zamm/100 + maas)

new_sall(1000, 20)