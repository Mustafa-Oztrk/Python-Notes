# uyglama mükalat sorusu

divide_student = ["Zeynep", "Mustafa", "Ege", "Mehmet", "Ahmet",]



def divide(students):
    groups = [[], []]
    for index, student in enumerate(students):
        if index %2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)
    print("Gruplar: ", groups)
    return groups

st = divide(divide_student)

st[0]