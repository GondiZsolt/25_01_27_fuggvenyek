"""Írj eljárást, amely paraméterül kapott számról eldönti, és a képernyőre kiírja, hogy negatív, pozitív vagy nulla-e! Addig lehessen megadni, amíg a felhasználó nem ad meg üres sztringet!"""

szam = int(input("Kérem adjon meg egy számot (üres sztring kilépéshez): "))
def eljaras(szam):
    while True:

        if szam < 0:
            print("A szám negatív.")
        elif szam > 0:
            print("A szám pozitív.")
        else:
            print("A szám nulla.")

        if szam == "":
            break
eljaras(szam)