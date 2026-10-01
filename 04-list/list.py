liczby = input("podaj 5 liczb do listy = ").split(' ')
for i in range(len(liczby)):
    liczby[i] = int(liczby[i])
def suma(liczby:list[int]) -> int:
    wynik = 0
    for liczba in liczby:
        wynik += liczba
    return wynik

def najwieksza(liczby:list[int]) -> int:
    if len(liczby) > 0:
        moja_naj = liczby[0]
        for i in range(1, len(liczby)):
            if liczby[i] > moja_naj:
                moja_naj = liczby[i]
        return moja_naj
    else:
        return "puste"
def najmniejsza(liczby:list[int]) -> int:
    if len(liczby) > 0:
        moja_naj = liczby[0]
        for i in range(1, len(liczby)):
            if liczby[i] < moja_naj:
                moja_naj = liczby[i]
        return moja_naj
    else:
        return "puste"
def srednia(liczby:list[int]) -> float:
    wynik = suma(liczby) / len(liczby)
    return wynik
def ile_parzystych(liczby:list[int]) -> int:
    parzyste = 0
    for liczba in liczby:
        if liczba % 2 == 0:
            parzyste += 1
    return parzyste
def dupicates(liczby:list[int]) -> list[int]:
    duplikaty = []
    mozliwe = []
    for liczba in liczby:
        if liczba in mozliwe:
            duplikaty.append(liczba)
        else:
            mozliwe.append(liczba)
    return duplikaty
def usuwanie_duplikatow(liczby:list[int]) -> list[int]:
    duplikaty = dupicates(liczby)
    for liczba in duplikaty:
        liczby.remove(liczba)
    return liczby
def squares(liczby:list[int]) -> list[int]:
    kwadraty = []
    for liczba in liczby:
        kwadraty.append(liczba ** 2)
    return kwadraty


print(f"suma liczb z listy = {suma(liczby)}")
print(f"najwieksza liczba z listy = {najwieksza(liczby)}")
print(f"najmniejsza liczba z listy = {najmniejsza(liczby)}")
print(f"średnia liczb z listy = {srednia(liczby)}")
print(f"parzyste liczby z listy = {ile_parzystych(liczby)}")
print(f"powtarzające sie liczby z listy = {dupicates(liczby)}")
print(f"kwadraty liczb z listy = {squares(liczby)}")
print(f"lista bez duplikatów = {usuwanie_duplikatow(liczby)}")
