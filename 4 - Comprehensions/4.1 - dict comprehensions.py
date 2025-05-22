# dict comprehensions 

dictinary = {'a': 1, 
             'b': 2, 
             'c': 3, 
             'd': 4}

# key değerleri
dictinary.keys()
# value değerleri
dictinary.values()
# key-value çiftleri
dictinary.items()

{k: v ** 2 for (k,v) in dictinary.items() }
