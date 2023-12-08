import tkinter as tk
from tkinter import messagebox

def menu_kivalasztas():
    valasztott = var.get()  # Itt eltároljuk a választott értéket
    if valasztott == 1:
        messagebox.showinfo("Választott alakzat/test", "Négyzet/kocka")
        ablak2.destroy()
    elif valasztott == 2:
        messagebox.showinfo("Választott alakzat/test", "Téglalap/téglatest")
        ablak2.destroy()
    elif valasztott == 3:
        messagebox.showinfo("Választott menüpont", "Harmadik menüpont kiválasztva")
        ablak2.destroy()

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
valasztas_gomb = tk.Button(ablak2, text="Választás", command=menu_kivalasztas)
valasztas_gomb.pack(side="bottom")

# Fő ablak megjelenítése
ablak2.mainloop()
