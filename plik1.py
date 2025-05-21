imie="Grześ"
nazwisko="Grzesio"
stanowisko="kursant"

print(imie,nazwisko,stanowisko)

print(imie, "dfsdf", nazwisko)
print(imie)
print(stanowisko)
print(imie,nazwisko,stanowisko, sep='')

calytekst = f"To jest fstring {imie},{nazwisko},{stanowisko}"
tekstinaczej = "Imię: " + imie + "Nazwisko: " + nazwisko + "Stanowisko: " + stanowisko

print(calytekst)
print(tekstinaczej)

help(print)
print('Ala\nma\nkota')
print(""" Ala
    ma
    kota""") #potrójny cudzysłów lub apostrof sprawia, że enter jest traktowany jako znak przeniesienia

#### formatowanie napisów:
#    1. fstringi : f"{zmienna} {innazmienna} jakis napis {zmienna3}"
#   2. formatowanie liczby: cena = 1.2
#            f"{cena:.2f}" - taki fstring bedzie formatował liczbę cena z dwoma miejscami po przecinku
# inne formatery liczb: ??
#
# jeżeli chce się wyrównywać żeby np wygenerować tabelę z wyrównanymi kolumnami
# produkt = f"{nazwa:15} {waga:6.2f} kg {cena:7.2f} PLN"
# można ustawić justowanie umieszczając po dwukropku znaki < ^ >