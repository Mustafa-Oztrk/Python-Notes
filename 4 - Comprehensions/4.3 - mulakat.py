numbers = range(1, 10)
new_dict = {}

for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n ** 2
        
print(new_dict)

# yukarıdki kodun dict comprehension ile yazımı
{n: n **2 for n in  numbers if n % 2 == 0}