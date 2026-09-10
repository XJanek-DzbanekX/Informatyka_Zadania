imie = str(input("imie: "))
wiek = int(input("wiek: "))

if wiek <= 16:
    print("daj ig pogadamy")
    wzrost = int(input("wzrost: "))
    if 160 < wzrost < 180:
        print("podoba mi sie dawaj dalej")
        waga = int(input("waga: "))
        if waga > 70:
            print("ble splywaj")
        else:
            print("spotamy sie")
            rozmiar_stopy = int(input("rozmiar stopy: "))
            if rozmiar_stopy < 39:
                print("splywaj mala")
            else:
                print("wyjdz za mnie czy cos")
    else:
        print("nie ma sensu splywaj")
elif wiek > 90:
    print("szybko zdechnie bede mial spadek...")
else:
    print("splywajjj")