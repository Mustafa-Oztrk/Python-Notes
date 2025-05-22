# comprehensions : 

salaries = [1000, 2000, 3000, 4000, 5000]

def calculate_slar(x):
    return x * 20 / 100

for salary in salaries:
    print(calculate_slar(salary))
    
# list comprehension
salaries = [1000, 2000, 3000, 4000, 5000]
salaries = [calculate_slar(salary) for salary in salaries]
print(salaries)