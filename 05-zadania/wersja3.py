#---------- 1 V sześcianu----------
# a = float(input("a = "))

# print(f"V szescianu = {a ** 3}")

#---------- 2 losowe liczby----------
# from random import randint

# for i in range(10):
#     print(randint(1, 1000000))

#---------- 3 suma i srednia do stop----------

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
# print(f"suma = {suma}")

#---------- 4 czy trójkąt równoramienny----------
# a = float(input("bok a = "))
# b = float(input("bok b = "))
# c = float(input("bok c = "))
# boki = [a, b, c]
# boki = sorted(boki)
# if boki[0] ** 2 + boki[1] ** 2 == boki[2] ** 2:
#     print("mozna zrobic trójkat")
#     if a == b:
#         print("równoramienny")
#     else:
#         print("różnoboczny")
# else:
#     print("NIE MOZNA")

#---------- 5 reszta z dzielenia----------
# k = int(input("podaj liczbe którą chcesz podzielic = "))
# m = int(input("podaj liczbe przez którą chcesz dzielic = "))

# print(f"reszta z dzielenia = {k % m}")

#---------- 6 ile razy k dzieli sie przez m----------
# k = int(input("podaj liczbe którą chcesz podzielic = "))
# m = int(input("podaj liczbe przez którą chcesz dzielic = "))

# if m > k:
#     print(0, "nie da sie")
# else:
#     print(k // m)





