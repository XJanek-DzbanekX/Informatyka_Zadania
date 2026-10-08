#----------1 V ostroslupa----------
# pp = float(input("pp = "))
# h = float(input("H = "))
# print(f"V ostrosłupa = {(pp * h) / 3}")

#----------2 zgadywanie cyfry----------
# from random import randint
# pruby = 0
# liczba = randint(1, 10)

# while pruby < 3:
#     n = int(input("zgaduj liczbe "))
#     if n == liczba:
#         print("Wygrales!!")
#         break
#     else:
#         print("przegrales")
#     pruby += 1

#---------- 3 najwiekszy element----------
# liczby = []

# while True:
#     n = input("liczba/stop ").lower().strip()
#     if n == "stop":
#         break
#     else:
#         liczby.append(int(n))
# if len(liczby) > 0:
#     print(max(liczby))
# else:
#     print("matole nie ma żadnej liczby")

#---------- 4 sprawdzanie czy mozna zrobic trojkat----------
# a = float(input("bok a = "))
# b = float(input("bok b = "))
# c = float(input("bok c = "))
# boki = [a, b, c]
# boki = sorted(boki)
# if boki[0] ** 2 + boki[1] ** 2 == boki[2] ** 2:
#     print("mozna zrobic trójkat")
# else:
#     print("NIE MOZNA")

#---------- 5 3 losowe odcinki----------
from random import randint
odcinek = int(input("długosc odcinka = "))
odcinki = []

for i in range(3):
    if odcinek <= 0:
        print("oj za za duzo ucialem wiec mamy tylko", len(odcinki))
    else:
        losowa_dlugosc = randint(1, odcinek)
        odcinki.append(losowa_dlugosc)
        odcinek -= losowa_dlugosc
print(f"odcinki = {odcinki}")
