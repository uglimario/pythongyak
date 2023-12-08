import random

szamalso = 0
szamfelso = 0
tipp = 0

szamalso = int(input("Add meg az alsó számot: "))
szamfelso = int(input("Add meg a felső számot: "))

gondoltszam = random.randint(szamalso , szamfelso)

tipp = int(input("Gondoltam egy számra... Tippeld meg: "))

while tipp != gondoltszam:
    if tipp < gondoltszam:
        print("A gondolt szám nagyobb mint a tipped" )
        tipp = int(input("Próbáld újra:"))
    elif tipp > gondoltszam:
        print("A gondolt szám kisebb mint a tipped")
        tipp = int(input("Próbáld újra:"))
    
print("Nyertél!!! ")
print(f"A gondolt szám: {gondoltszam} volt. Kitaláltad ügyes vagy!")