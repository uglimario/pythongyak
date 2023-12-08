# Lottó számok listájának létrehozása
import random

lottogomb = []
kihuzottszamok = []
tipp = []
# szam = 0

for i in range (0,5):
    szam = int(input("Kérek egy 1 és 90 közé eső számot: "))
    tipp.append(szam)

for i in range (1, 91):
    lottogomb.append(i)
    
random.shuffle(lottogomb)

for i in range (0,5):
    kihuzottszamok.append(lottogomb[i])

kihuzottszamok.sort()
tipp.sort()

print(f"Az ön tippje: {tipp}")
print(f"A kihúzott számok: {kihuzottszamok}")