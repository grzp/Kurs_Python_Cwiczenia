
lista=[]

while True:
    liczba_str = input("Podaj liczbę lub wciśnij eneter żeby zakończyć: ")
    if liczba_str == "":
        break
    if liczba_str.isdigit() is False:
        print("wpisuj tylko liczby")
        continue
    liczba = int(liczba_str)
    lista.append(liczba)

parzyste = [l for l in lista if l % 2 == 0]
nieparzyste = [l for l in lista if l % 2 != 0]


try:
    print("Parzyste: ", parzyste)
    print(f"Ilość parzystych: {len(parzyste):<5} Srednia: {sum(parzyste) / len(parzyste)} ")
    print("Nieparzyste: ",nieparzyste)
    print( f"Ilość nieparzystych: {len(nieparzyste):<5} Srednia: {sum(nieparzyste)/len(nieparzyste)} " )

except:
    print("Jest jakiś błąd w danych")