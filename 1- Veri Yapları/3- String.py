# Metinler

# Stringler, Python'da metin verilerini temsil etmek için kullanılan veri türleridir.
# Stringler, tek tırnak (' ') veya çift tırnak (" ") içinde tanımlanabilir.
# Stringler, bir veya daha fazla karakter içerebilir. Örneğin:
# metin1 = "Merhaba, Dünya!"
# metin2 = 'Python programlama dili'
# metin3 = """Bu birden fazla satır içeren
# bir string örneğidir."""

a = "Merhaba, Dünya!" # string
print(a) # stringi ekrana yazdırma

b = "Python" 
b[2] # stringin 2. indeksindeki karakteri alır"
print(b[2]) # stringin 2. indeksindeki karakteri ekrana yazdırma
print(b[0:3]) # stringin 0'dan 3'e kadar olan kısmını alır

long_str = "Pythonu Çok seviyorum"
c ="Python" in long_str # "Python" kelimesi long_str içinde var mı? büyük küçük harf duyarlıdır
print(c) 