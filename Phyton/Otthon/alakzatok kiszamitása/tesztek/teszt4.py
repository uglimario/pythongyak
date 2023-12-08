import tkinter as tk

def gomb1_click():
    print("1. gombra kattintottál")
    ablak.destroy()  # Az ablak bezárása

def gomb2_click():
    print("kutyusssss gombra kattintottál")
    ablak.destroy()  # Az ablak bezárása

def gomb3_click():
    print("halooo gombra kattintottál")
    ablak.destroy()  # Az ablak bezárása

# Fő ablak létrehozása
ablak = tk.Tk()
ablak.title("Gombok")

# Ablak méretének beállítása
ablak.geometry("1000x500")  # Például 1000 pixel széles és 500 pixel magas

# Ablak középre pozicionálása
ablak.update_idletasks()  # Ablak frissítése
ablak_width = ablak.winfo_width()
ablak_height = ablak.winfo_height()
screen_width = ablak.winfo_screenwidth()
screen_height = ablak.winfo_screenheight()
x = (screen_width // 2) - (ablak_width // 2)
y = (screen_height // 4) - (ablak_height // 3)
ablak.geometry(f"{ablak_width}x{ablak_height}+{x}+{y}")

# Háttérkép betöltése
hatter_img = tk.PhotoImage(file="Mellékek/alakzatok hatter.png")

# Háttérkép megjelenítése egy Label widgeten keresztül
hatter_label = tk.Label(ablak, image=hatter_img)
hatter_label.place(relwidth=1, relheight=1)  # A hátteret kitöltjük az ablak teljes területével

# Mondatazon elhelyezése átlátszó háttérrel
mondat_label = tk.Label(ablak, text="Ez egy középre pozícionált félkövér mondat.", font=("Algerian", 30))
mondat_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
mondat_label.config(bg="white", highlightthickness=0, bd=0)

# Gombok létrehozása és hozzárendelése a függvényekhez átlátszó háttérrel
gomb1 = tk.Button(ablak, text="1", command=gomb1_click, highlightthickness=0, bd=0)
gomb2 = tk.Button(ablak, text="kutyusssss", command=gomb2_click, bg="blue", fg="white", font=("Helvetica", 22), highlightthickness=0, bd=0)
gomb3 = tk.Button(ablak, text="halooo", command=gomb3_click, font=("Helvetica", 12), highlightthickness=0, bd=0)

# Gombok elhelyezése az ablakban
gomb1.place(relx=0.2, rely=0.4, anchor=tk.CENTER)
gomb2.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
gomb3.place(relx=0.8, rely=0.4, anchor=tk.CENTER)

# Fő ablak megjelenítése
ablak.mainloop()
