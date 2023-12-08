# Oldalhossz beolvasása a felhasználótól
oldalhossz = float(input("Kérem adja meg a négyzet oldalhosszát: "))
magassag = float(input("Kérem adja meg a négyzet magasságát: "))

while True:
    print("Válassz az alábbi mértékegységek közül")
    print("miliméter")
    print("centiméter")
    print("méter")
    print("kilométer")

    choice = input("Add meg a mértékegységet (pl.: dm): ")

    if choice == "mm":
        print("miliméter")
        break
    elif choice == "cm":
        print("centiméter")
        break
    elif choice == "m":
        print("méter")
        break
    elif choice == "km":
        print("kilométer")
        break
    else:
        print("Érvénytelen választás. Kérem adjon meg egy érvényes mértékegységet.")

# Terület kiszámítása
terulet = oldalhossz * oldalhossz

# Kerület kiszámítása
kerulet = 4 * oldalhossz

# Eredmények kiírása
print(f"A négyzet területe: {terulet} {choice} ^2 ")
print(f"A négyzet kerülete: {kerulet} {choice}")

terfogat = terulet * magassag

print("A kocka térfogata:" , terfogat , choice , "^3" )