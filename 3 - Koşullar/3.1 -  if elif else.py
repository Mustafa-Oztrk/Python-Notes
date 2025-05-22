
love = True
def love_check(love):
    if love == True:
        print("Sen beni seviyorsun")
    else:
        print("Yoksa yok")


love_check(True)


# Koşullar

if 1 == 2:
    print("Eşittir")
else:
    print("Eşitt değilll")


num = 11

if num == 11:
    print("Sayı 11'e eşit")
else:
    print("Değil")


# No repate 

def num_check(num):
    if num == 11:
        print("Eşittir")
    else:
        print("Değildir")

num_check(12)

# elif

number = 12

def mumber_check(number):
    if number <10:
        print("sayı 10 dan küçük")
    elif number > 10:
        print("Sayı 10 dan nüyük")
    else:
        print("Sayı 10'a eşit")