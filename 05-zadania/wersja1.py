#----------1 V kuli----------
# from math import pi
# r = float(input("r = "))

# print(f"V kuli = {(r ** 3 * pi) * (4 / 3)}")

#----------2 wypisywanie kocham programowac----------
# n = int(input("liczba ile razy mam wypisac tekst = "))
# for i in range(n):
#     print("kocham programować")

#----------3 sumowanie liczb do stopu----------
# wynik = 0

# while True:
#     n = input("liczba/stop ").lower().strip()
#     if n == "stop":
#         break
#     else:
#         wynik += int(n)
# print(wynik)

#----------4 średnia do stopu----------
# suma = 0
# ile_liczb = 0
# while True:
#     n = input("liczba/stop ").lower().strip()
#     if n == "stop":
#         break
#     else:
#         suma += int(n)
#     ile_liczb += 1
# print(f"średnia = {suma / ile_liczb}")

#----------5a potęgi----------
n = int(input("ile potęg mam zsumowac "))
wynik = 0

for i in range(n):
    wynik += 2 ** i
print(f"wynik = {wynik}")
