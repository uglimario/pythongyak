szam = 0
hatarertek = int(input("Kérem a határértéket: "))
lepesek = 0
leghosszabszekvencia = -1
leghosszabszekvszam = -1
vizsgaltszam = 0
legmagasabbszam = 0
maximumvizsgaltszam = 0
maximumlepes = 0
maximumlepesszamszam = 0

for szamlalo in range (2, hatarertek):
    szam = szamlalo
    vizsgaltszam = szam
    while szam > 1:
        if szam % 2 == 0:
            szam = int(szam / 2)
            lepesek = lepesek + 1
        else:
            szam = int((szam * 3) + 1)
            lepesek = lepesek + 1
        
        if lepesek > leghosszabszekvencia:
            leghosszabszekvencia = lepesek
            leghosszabszekvszam = vizsgaltszam
            print(f"Új leghosszabb szekvenciát találtam: {leghosszabszekvencia} a vizsgalt szam: {leghosszabszekvszam}")
            
        if szam > legmagasabbszam:
            legmagasabbszam = szam
            maximumvizsgaltszam = vizsgaltszam
            print(f"Új legmagasabb számot találtam: {legmagasabbszam} a vizsglat szam: {maximumvizsgaltszam}")
            
    lepesek = 0
            
print(f"A leghosszabb sorozat: {leghosszabszekvencia} és a hozzá tartozó szám: {leghosszabszekvszam}")
print(f"A legmagasabb szám: {legmagasabbszam} és a hozzá tartozó érték: {maximumvizsgaltszam}")