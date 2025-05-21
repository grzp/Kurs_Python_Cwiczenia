#Utwórz listę parzystych i nieparzystych, średnią wartość, ilość elementów w liście
# przydatny operator / - dzielenie true div, // - dzielenie całkowite, % - dzielenie modulo (reszta z dzielenia)
# sum(lista) = suma z listy
#

##lista = [1,2,3,4,5,6,7,8,9,10, 11,2,11]
#1. modyfikacja - użytkownik ma podać z konsoli 10 liczb
#2. modyfikacja - użytkownik ma podać s konsoli n liczb

# instrukcja input pobiera string z klawiatury

lista=[]
for i in range(10):
    liczba_str = input("Podaj liczbę lub wciśnij eneter żeby zakończyć: ")
    if liczba_str == "":
        break
    liczba = int(liczba_str)
    lista.append(liczba)







parzyste = []
nieparzyste =[]

for i in lista:
    if i % 2:
        if not (i % 1):
            nieparzyste.append(i)
    else:
        parzyste.append(i)

print("Nieparzyste: ",nieparzyste)
print( f"Ilość nieparzystych: {len(nieparzyste):<5} Srednia: {sum(nieparzyste)/len(nieparzyste)} " )

print("Parzyste: ",parzyste)
print( f"Ilość parzystych: {len(parzyste):<5} Srednia: {sum(parzyste)/len(parzyste)} " )


####  Wykorzystanie idiomów Pythonowych:
parzyste = [l for l in lista if l % 2 == 0]
nieparzyste = [l for l in lista if l % 2 != 0]

kwadraty_liczb = {l: l **2 for l in lista}  # tutaj wygeneruje się słownik - pary elementów!
print(kwadraty_liczb)

#to samo można tak
kwadraty_liczb2 = {}
for liczba in lista:
    kwadraty_liczb2[liczba] = liczba**2