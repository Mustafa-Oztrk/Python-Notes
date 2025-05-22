# çifleri büyük harf tekleri küçük harf yazdırma

cum = "Hi my name is mustafa and i am learning python"


def kelime(string):
  new_string = ""
# verilen stringin her bir karakterini tek tek alır
  for string_index in range(len(string)):
        # stringin index değeri çift ise büyük harf 
        if string_index % 2 == 0:
          new_string += string[string_index].upper()
        # stringin index değeri tek ise küçük harf
        else:
            new_string += string[string_index].lower()
  print(new_string)
kelime(cum)
