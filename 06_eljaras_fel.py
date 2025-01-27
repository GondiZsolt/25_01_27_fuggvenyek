"""Írj eljárást, amely paraméterül kapott számról eldönti, és a képernyőre kiírja, hogy negatív, pozitív vagy nulla-e! Addig lehessen megadni, amíg a felhasználó nem ad meg üres sztringet!"""



def eljaras(szam):
    if szam < 0:
        print("A szám negatív.")
    elif szam > 0:
        print("A szám pozitív.")
    else:
        print("A szám nulla.")

while True:
    szam = input("Kérem adja meg a számot (üres sztring kilépéshez): ")
    if szam == "":
        break
    try:
        szam = int(szam)
        eljaras(szam)
    except ValueError:
        print("Hibás bemenet, kérem adjon meg egy számot!")