# str methdodları
# Stringler üzerinde çeşitli işlemler yapmamızı sağlayan birçok yerleşik yöntem (method) vardır.

dir(str) # str sınıfının tüm methodlarını gösterir
name = "Mustafa"
len(name) # stringin uzunluğunu döndürür
name.upper() # stringi büyük harfe çevirir  
name.lower() # stringi küçük harfe çevirir
name.title() # stringin ilk harfini büyük yapar
name.replace("a","u") # Yer değiştirme
name.split("a") # stringi "a" karakterine göre böler ve liste döndürür
name.strip() # stringin başındaki ve sonundaki boşlukları siler
name.find("a") # stringde "a" karakterinin ilk geçtiği yeri döndürür. Eğer yoksa -1 döner
name.index("a") # stringde "a" karakterinin ilk geçtiği yeri döndürür. Eğer yoksa hata verir
name.count("a") # stringde "a" karakterinin kaç kez geçtiğini döndürür
name.startswith("M") # string "M" ile başlıyorsa True döner
name.capitalize() # stringin ilk harfini büyük yapar ve diğer harfleri küçük yapar
name.isalpha() # stringin sadece harflerden oluşup oluşmadığını kontrol eder
name.isdigit() # stringin sadece rakamlardan oluşup oluşmadığını kontrol eder
name.isalnum() # stringin sadece harf ve rakamlardan oluşup oluşmadığını kontrol eder
name.islower() # stringin sadece küçük harflerden oluşup oluşmadığını kontrol eder
name.isupper() # stringin sadece büyük harflerden oluşup oluşmadığını kontrol eder
name.isnumeric() # stringin sadece sayılardan oluşup oluşmadığını kontrol eder
name.isdecimal() # stringin sadece ondalık sayılardan oluşup oluşmadığını kontrol eder