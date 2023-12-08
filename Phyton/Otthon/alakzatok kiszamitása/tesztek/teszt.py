import tkinter as tk
from tkinter import messagebox

def menu_kivalasztas():
    valasztott = var.get()  # Itt eltároljuk a választott értéket
    if valasztott == 1:
        messagebox.showinfo("Választott menüpont", "Első menüpont kiválasztva")
    elif valasztott == 2:
        messagebox.showinfo("Választott menüpont", "Második menüpont kiválasztva")
    elif valasztott == 3:
        messagebox.showinfo("Választott menüpont", "Harmadik menüpont kiválasztva")

# Fő ablak létrehozása
ablak = tk.Tk()
ablak.title("Egyedi Gomb Menü")

# Változó a menüpont kiválasztásához
var = tk.IntVar()

# Menüpontok létrehozása
radio_button1 = tk.Radiobutton(ablak, text="Első menüpont", variable=var, value=1)
radio_button2 = tk.Radiobutton(ablak, text="Második menüpont", variable=var, value=2)
radio_button3 = tk.Radiobutton(ablak, text="Harmadik menüpont", variable=var, value=3)

# Gombok hozzáadása az ablakhoz
radio_button1.pack()
radio_button2.pack()
radio_button3.pack()

# Választás gomb
valasztas_gomb = tk.Button(ablak, text="Választás", command=menu_kivalasztas)
valasztas_gomb.pack()

# Fő ablak megjelenítése
ablak.mainloop()

gomb = tk.Button(ablak, text="Gomb", bg="blue", fg="white")
gomb = tk.Button(ablak, text="Gomb", font=("Helvetica", 12))
canvas = tk.Canvas(ablak, width=200, height=200)
canvas.pack()
img = tk.PhotoImage(file="hatterkep.png")
canvas.create_image(0, 0, anchor=tk.NW, image=img)
ablak.geometry("400x400")  # Ablak mérete 400x400 pixel
ablak.title("Egyedi Ablak")  # Az ablak címe
