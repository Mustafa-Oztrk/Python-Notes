# Elemanlarını eşleme 

student = ['Ali', 'Veli', 'Ayşe']
depertment = ['Bilgisayar', 'Elektrik', 'Makine']
number = [1, 2, 3]

# zip() fonksiyonu ile birleştirme
list(zip(student, depertment, number))
# [('Ali', 'Bilgisayar', 1), ('Veli', 'Elektrik', 2), ('Ayşe', 'Makine', 3)]