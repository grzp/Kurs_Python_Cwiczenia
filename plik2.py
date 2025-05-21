imie1="Grześ"
nazwisko1="Grzesio"
stanowisko1="kursant"
staż1=2
stawka1=123.67

imie2="Ala"
nazwisko2="Elementarna"
stanowisko2="kociara"
staż2=3.9
stawka2=0.05 * 2

imie3="Olo"
nazwisko3="Ratujczak"
stanowisko3="kum"
staż3=199
stawka3=10.1

nagłówek = f"Imię       Nazwisko       Stanowisko   Staż      Stawka"
napis1 = f"{imie1:10} {nazwisko1:15} {stanowisko1:11} {staż1:^5.0f} {stawka1:>24.20f}"
napis2 = f"{imie2:10} {nazwisko2:15} {stanowisko2:11} {staż2:^5.0f} {stawka2:>24.20f}"
napis3 = f"{imie3:10} {nazwisko3:15} {stanowisko3:11} {staż3:^5.0f} {stawka3:>24.20f}"

print(f"""
    {nagłówek}
    {napis1}
    {napis2}
    {napis3}""")

#Można słownik: osoba ={nazwisko:"ktoś", imie:"ktosiowy"}