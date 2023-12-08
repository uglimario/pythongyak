import tkinter as tk

# Függvények a gombok kattintásának kezelésére
def gomb1_click():
    print("1. gombra kattintottál")
    ablak.destroy()  # Az ablak bezárása

def gomb2_click():
    print("2. gombra kattintottál")
    ablak.destroy()  # Az ablak bezárása

def gomb3_click():
    print("3. gombra kattintottál")
    ablak.destroy()  # Az ablak bezárása

# Fő ablak létrehozása
ablak = tk.Tk()
ablak.title("Gombok")

# Gombok létrehozása és hozzárendelése a függvényekhez
gomb1 = tk.Button(ablak, text="1", command=gomb1_click)
gomb2 = tk.Button(ablak, text="anyaaaaaas", command=gomb2_click , bg="blue", fg="white" )
gomb3 = tk.Button(ablak, text="kurvaaaa", command=gomb3_click , font=("Helvetica", 12))

# Gombok elhelyezése az ablakban
gomb1.pack()
gomb2.pack()
gomb3.pack()

# Fő ablak megjelenítése
ablak.mainloop()

gomb1 = tk.Button(ablak, text="Gomb", bg="blue", fg="green" )
gomb2 = tk.Button(ablak, text="Gomb", font=("Helvetica", 12))
canvas = tk.Canvas(ablak, width=200, height=200)
canvas.pack()
img = tk.PhotoImage(file="hatterkep.png")
canvas.create_image(0, 0, anchor=tk.NW, image=img)