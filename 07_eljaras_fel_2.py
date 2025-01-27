"""Írj egy programot, amely a felhasználótól bekér szavakat, ezeket egy listában tárolja, és egy eljárás segítségével meghatározza, és a képernyőre kiírja, melyik a legrövidebb szó!
"""

def legrövidebb_szó(szavak):
    if len(szavak) == 0:
        print("Nincs szó a listában.")
        return
    legrövidebb = min(szavak, key=len)
    print(f"A legrövidebb szó: {legrövidebb}")

szavak = []
while True:
    szó = input("Kérem adj meg szavakat (ne adj emg semmit a befejezéshez): ")
    if szó == "":
        break
    szavak.append(szó)

legrövidebb_szó(szavak)