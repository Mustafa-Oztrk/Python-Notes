# break continue & while

salaries = [1000, 2000, 3000, 4000, 5000]

# verilen değere gelene kadar döngüyü devam ettirir
for salary in salaries:
    if salary  == 3000:
        break
    print(salary)

# verilen değeri atla ve döngüyü devam ettirir
for salary in salaries:
    if salary == 3000:
        continue
    print(salary)

# while döngüsü

num = 0
while num  <10:
    print(num)
    num +=1
    