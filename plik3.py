napis = "Ala ma kota burego, czystego i miłego."
samogloski = list("aeiouy .,") #konwertuje string na listę - tylko tak dla ćwiczenia
#dodaj kod, który zliczy liczbę spółgłosek w napis
ciag = []


for i in napis:     #mogę pobierać litery bezpośrednio ze stringu
    if i.lower() in samogloski: #konwertuję każdą literę na mały znak przed porównaniem z listą samogłoski
        ciag.append(i)

dlugosc = len(napis) - len(ciag)

print(dlugosc)
print(samogloski)
