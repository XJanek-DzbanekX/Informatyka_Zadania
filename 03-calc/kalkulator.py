from math import pi, sqrt
def wczytywanie(nazwy : list[str]) -> dict[str, float]:
    wczytane = dict()
    for n in nazwy:
        wczytane[n] = float(input(f"{n} = "))
        if wczytane[n] <= 0:
            print(f"nie mozesz miec ujemnego {n}...")
            exit()

    return wczytane


#pytamy użytkownika co chce liczyc najpierw czy w 3d czy plaskie a potem czy pc czy ob/V
wybor = int(input("figury plaskie -> 1, figury 3d -> 2   =   "))              
if wybor == 1:
    wybor = int(input("pole calkowite -> 1, obwod -> 2   =   "))
    if wybor == 1:
        wybor = int(input("kwadrat -> 1, prostokat -> 2, rownoleglobok -> 3, trapez - > 4, trojkat -> 5, trojkat rownoboczny -> 6, kolo -> 7, romb -> 8   =   "))
        #wczytujemy tylko potrzebne wymiary i liczymy
        #pc figur plaskich
        if wybor == 1:
            wymiary = wczytywanie(["a"])                                     
            print(f"pc kwadratu = {wymiary["a"] ** 2}")
        elif wybor == 2:
            wymiary = wczytywanie(["a", "b"])
            print(f"pc prostokatu = {wymiary["a"] * wymiary["b"]}")
        elif wybor == 3:
            wymiary = wczytywanie(["a", "h"])
            print(f"pc rownolegloboku = {wymiary["a"] * wymiary["h"]}")
        elif wybor == 4:
            wymiary = wczytywanie(["a", "b", "h"])
            print(f"pc trapezu = {((wymiary["a"] + wymiary["b"]) * wymiary["h"]) / 2}")
        elif wybor == 5:
            wymiary = wczytywanie(["a", "h"])
            print(f"pc trojkata = {(wymiary["a"] * wymiary["h"]) / 2}")
        elif wybor == 6:
            wymiary = wczytywanie(["a"])
            print(f"pc trojkata rownobocznego = {(wymiary["a"] ** 2 * sqrt(3)) / 4}")
        elif wybor == 7:
            wymiary = wczytywanie(["r"])
            print(f"pc kola = {wymiary["r"] ** 2 * pi}")
        elif wybor == 8:
            wymiary = wczytywanie(["a", "h"])
            print(f"pc rombu = {wymiary["a"] * wymiary["b"]}")
        else:
            print("nie ma takiej komendy...")
    # teraz obwody
    elif wybor == 2:
        wybor = int(input("kwadrat -> 1, prostokat -> 2, rownoleglobok -> 3, trapez - > 4, trojkat -> 5, trojkat rownoboczny -> 6, kolo -> 7, romb -> 8   =   "))
        if wybor == 1:
            wymiary = wczytywanie(["a"])
            print(f"ob kwadratu = {wymiary["a"] * 4}")
        elif wybor == 2:
            wymiary = wczytywanie(["a", "b"])
            print(f"ob prostokatu = {wymiary["a"] * 2 + wymiary["b"] * 2}")
        elif wybor == 3:
            wymiary = wczytywanie(["a", "b"])
            print(f"ob rownolegloboku = {wymiary["a"] * 2 + wymiary["b"] * 2}")
        elif wybor == 4:
            wymiary = wczytywanie(["a", "b", "c", "d"])
            print(f"ob trapezu = {wymiary["a"] + wymiary["b"] + wymiary["c"] + wymiary["d"]}")
        elif wybor == 5:
            wymiary = wczytywanie(["a", "b", "c"])
            print(f"ob trojkata = {wymiary["a"] + wymiary["b"] + wymiary["c"]}")
        elif wybor == 6:
            wymiary = wczytywanie(["a"])
            print(f"ob trojkata rownobocznego = {wymiary["a"] * 3}")
        elif wybor == 7:
            wymiary = wczytywanie(["r"])
            print(f"ob kola = {wymiary["r"] * 2 * pi}")
        elif wybor == 8:
            wymiary = wczytywanie(["a"])
            print(f"ob rombu = {wymiary["a"] * 4}")
        else:
            print("nie ma takiej komendy...")
































# wymiary = wczytywanie(["a", "b"])
# print(wymiary["a"] * wymiary["b"])
