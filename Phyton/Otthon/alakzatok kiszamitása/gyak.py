import tkinter as tk
from tkinter import messagebox

# Függvények a gombok kattintásának kezelésére
def gomb1_click():
    print("Kiválasztottad a háromszöget.")
    ablak.destroy()  # Az ablak bezárása
       
    while True:
        print("Válassz az alábbi mértékegységek közül")
        print("milliméter")
        print("centiméter")
        print("méter")
        print("kilométer")

        choice = input("Add meg a mértékegységet (pl.: dm): ")

        if choice == "mm":
            print("milliméter")
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
    
    print("HA ERROR A HÁROMSZÖG NEM KISZÁMOLHATÓ!!!")
    oldalhossza = float(input("Kérem adja meg a háromszög (a) oldalhosszát: "))
    oldalhosszb = float(input("Kérem adja meg a háromszög (b) oldalhosszát: "))
    oldalhosszc = float(input("Kérem adja meg a háromszög (c) oldalhosszát: "))
    magassag = float(input("Kérem adja meg a háromszög alapú hasáb magasságát: "))        

    # Kerület kiszámítása
    kerulet = oldalhossza + oldalhosszb + oldalhosszc
    
    # Félkerület kiszámítása
    s = kerulet / 2
    
    import math
    # Terület kiszámítása
    terulet = math.sqrt(s * (s - oldalhossza) * (s - oldalhosszb) * (s - oldalhosszc))

    # Eredmények kiírása
    print(f"A háromszög területe: {terulet} {choice} ^2 ")
    print(f"A háromszög kerülete: {kerulet} {choice}")

    terfogat = terulet * magassag

    print("A háromszög alapú hasáb térfogata:" , terfogat , choice , "^3" )
    
def gomb2_click():
    print("A négyszöget választottad.")
    ablak.destroy()
    
    def menu_kivalasztas():
            valasztott = var.get()  # Itt eltároljuk a választott értéket
            if valasztott == 1:
                messagebox.showinfo("Választott alakzat/test", "   Négyzet/kocka   " )
                ablak2.destroy()
                while True:
                    print("Válassz az alábbi mértékegységek közül")
                    print("milliméter")
                    print("centiméter")
                    print("méter")
                    print("kilométer")

                    choice = input("Add meg a mértékegységet (pl.: dm): ")

                    if choice == "mm":
                        print("milliméter")
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
                        
                # Oldalhossz beolvasása a felhasználótól
                oldalhossz = float(input("Kérem adja meg a négyzet oldalhosszát: "))
                magassag = float(input("Kérem adja meg a négyzet magasságát: "))

                # Terület kiszámítása
                terulet = oldalhossz * oldalhossz

                # Kerület kiszámítása
                kerulet = 4 * oldalhossz

                # Eredmények kiírása
                print(f"A négyzet területe: {terulet} {choice} ^2 ")
                print(f"A négyzet kerülete: {kerulet} {choice}")

                terfogat = terulet * magassag

                print("A kocka térfogata:" , terfogat , choice , "^3" )
                
            elif valasztott == 2:
                messagebox.showinfo("Választott alakzat/test", "Téglalap/téglatest")
                ablak2.destroy()
                while True:
                    print("Válassz az alábbi mértékegységek közül")
                    print("milliméter")
                    print("centiméter")
                    print("méter")
                    print("kilométer")

                    choice = input("Add meg a mértékegységet (pl.: dm): ")

                    if choice == "mm":
                        print("milliméter")
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
                    
                    # Oldalhossz beolvasása a felhasználótól
                oldalhossza = float(input("Kérem adja meg a téglalap (a)oldalhosszát: "))
                oldalhosszb = float(input("Kérem adja meg a téglalap (b)oldalhosszát: "))
                magassag = float(input("Kérem adja meg a téglatest magasságát: "))

                # Terület kiszámítása
                terulet = oldalhossza * oldalhosszb

                # Kerület kiszámítása
                kerulet = (oldalhossza + oldalhosszb) * 2

                # Eredmények kiírása
                print(f"A téglalap területe: {terulet} {choice} ^2 ")
                print(f"A téglalap kerülete: {kerulet} {choice}")

                terfogat = terulet * magassag

                print("A téglatest térfogata:" , terfogat , choice , "^3" )
                        
            elif valasztott == 3:
                        messagebox.showinfo("Bocsánat... :(", "Elnézést, de a programom még nem elég fejlett, hogy más négyszögek számítását végezze...")
                        print("JELENLEG ITT A PROGRAM VÉGE!!!")
                        ablak2.destroy()
 # JELENEG ITT A PROGRAM VÉGE                      
                        
                        while True:
                            print("Válassz az alábbi mértékegységek közül")
                            print("milliméter")
                            print("centiméter")
                            print("méter")
                            print("kilométer")

                            choice = input("Add meg a mértékegységet (pl.: dm): ")

                            if choice == "mm":
                                print("milliméter")
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
 # JELENEG ITT A PROGRAM VÉGE    
                                
    import tkinter as tk
    from tkinter import messagebox

    # Fő ablak létrehozása
    ablak2 = tk.Tk()
    ablak2.title("Alakzatok és testek")

    # Ablak méretének beállítása
    ablak2.geometry("1000x500")  # Például 1000 pixel széles és 500 pixel magas

    # Ablak középre pozicionálása
    ablak2.update_idletasks()  # Ablak frissítése
    ablak2_width = ablak2.winfo_width()
    ablak2_height = ablak2.winfo_height()
    screen_width = ablak2.winfo_screenwidth()
    screen_height = ablak2.winfo_screenheight()
    x = (screen_width // 2) - (ablak2_width // 2)
    y = (screen_height // 4) - (ablak2_height // 3)
    ablak2.geometry(f"{ablak2_width}x{ablak2_height}+{x}+{y}")

    # Háttérkép betöltése
    hatter_img = tk.PhotoImage(file="Mellékek/alakzatok hatter.png")

    # Háttérkép megjelenítése egy Label widgeten keresztül
    hatter_label = tk.Label(ablak2, image=hatter_img)
    hatter_label.place(relwidth=1, relheight=1)  # A hátteret kitöltjük az ablak teljes területével

    # "Mondat" szöveg elhelyezése a lap tetején
    mondat_label = tk.Label(ablak2, text="Mit szeretnél kiszámolni?", font=("Algerian", 30))
    mondat_label.pack(side="top", pady=20)  # pady=20 helyezze el a szöveget fentről lefelé

    # Változó a menüpont kiválasztásához
    var = tk.IntVar()

    # Menüpontok létrehozása jobb oldalon, egymás alatt
    radio_button1 = tk.Radiobutton(ablak2, text="Négyzet/kocka", variable=var, value=1)
    radio_button2 = tk.Radiobutton(ablak2, text="Téglalap/téglatest", variable=var, value=2)
    radio_button3 = tk.Radiobutton(ablak2, text="Egyik sem", variable=var, value=3)

    # Menüpontok elrendezése egymás alatt
    radio_button1.pack(anchor='w')
    radio_button2.pack(anchor='w')
    radio_button3.pack(anchor='w')

    # "Választás" gomb középen
    valasztas_gomb = tk.Button(ablak2, text="Ezt szeretném!", command=menu_kivalasztas, font=("Copper" , 15))
    valasztas_gomb.pack(side="bottom")

    # Fő ablak megjelenítése
    ablak2.mainloop()

        
def gomb3_click():
    print("A kört választottad")
    ablak.destroy()  # Az ablak bezárása

    while True:
        print("Válassz az alábbi mértékegységek közül")
        print("milliméter")
        print("centiméter")
        print("méter")
        print("kilométer")

        choice = input("Add meg a mértékegységet (pl.: dm): ")

        if choice == "mm":
            print("milliméter")
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
        
        
    sugar = float(input("Kérem adja meg a kör sugarát: "))

    import math
    atmero = sugar * 2
    kerulet = 2 * sugar * math.pi
    terulet = sugar * sugar * math.pi
    felszin = 4 * math.pi * sugar * sugar
       
    # Eredmények kiírása
    print(f"A kör átmérője: {atmero} {choice}")
    print(f"A kör területe: {terulet} {choice} ^2 ")
    print(f"A kör kerülete: {kerulet} {choice}")
    print(f"A kör felszíne: {felszin} {choice} ^2")
    
    terfogat = (4/3) * math.pi * sugar * sugar * sugar

    print("A kör térfogata:" , terfogat , choice , "^3" )
   
ablak = tk.Tk()
ablak.title("Gombok")
ablak.geometry("1000x500")   
    
ablak.update_idletasks()
ablak_width = ablak.winfo_width()
ablak_height = ablak.winfo_height()
screen_width = ablak.winfo_screenwidth()
screen_height = ablak.winfo_screenheight()
x = (screen_width // 2) - (ablak_width // 2)
y = (screen_height // 4) - (ablak_height // 3)
ablak.geometry(f"{ablak_width}x{ablak_height}+{x}+{y}")

hatter_img2 = tk.PhotoImage(file="Mellékek/negyzet kor haromszog.png")
hatter_label2 = tk.Label(ablak, image=hatter_img2)
hatter_label2.place(relx=0, rely=0, relwidth=1, relheight=1)  # A háttérkép a teljes ablakot kitölti

# Mondatazon elhelyezése
mondat_label = tk.Label(ablak, text="Mit szeretnél kiszámolni?", font=("Algerian", 30))
mondat_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)  # A főcím középen legyen

gomb1 = tk.Button(ablak, text="Háromszög", command=gomb1_click, bg="yellow", fg="black", font=("Helvetica", 22))
gomb2 = tk.Button(ablak, text="Sokszög", command=gomb2_click, bg="red", fg="blue", font=("Helvetica", 22))
gomb3 = tk.Button(ablak, text="Kör", command=gomb3_click, bg="blue", fg="white", font=("Helvetica", 22))

gomb1.place(relx=0.8605, rely=0.67, anchor=tk.CENTER)
gomb2.place(relx=0.14, rely=0.5, anchor=tk.CENTER)
gomb3.place(relx=0.52, rely=0.5, anchor=tk.CENTER)

ablak.mainloop()