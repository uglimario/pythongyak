import tkinter as tk
from tkinter import PhotoImage

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

# Ablak méretének beállítása
ablak.geometry("1000x500")  # Például 400 pixel széles és 200 pixel magas

canvas = tk.Canvas(ablak, width=800, height=600)
canvas.pack()
img = PhotoImage(file= "Mellékek/alakzatok hatter.png")
canvas.create_image(0, 0, anchor=tk.NW, image=img)

# Ablak középre pozicionálása
ablak.update_idletasks()  # Ablak frissítése
ablak_width = ablak.winfo_width()
ablak_height = ablak.winfo_height()
screen_width = ablak.winfo_screenwidth()
screen_height = ablak.winfo_screenheight()
x = (screen_width // 2) - (ablak_width // 2)
y = (screen_height // 4) - (ablak_height // 3)
ablak.geometry(f"{ablak_width}x{ablak_height}+{x}+{y}")

# Mondatazon elhelyezése
mondat_label = tk.Label(ablak, text="Ez egy középre pozícionált félkövér mondat." , font=("Algerian" , 30))
mondat_label.pack()

# Gombok létrehozása és hozzárendelése a függvényekhez
gomb1 = tk.Button(ablak, text="1", command=gomb1_click)
gomb2 = tk.Button(ablak, text="kutyusssss", command=gomb2_click, bg="blue", fg="white" , font=("Helvetica", 22 ))
gomb3 = tk.Button(ablak, text="halooo", command=gomb3_click, font=("Helvetica", 12))

# Gombok elhelyezése az ablakban
gomb1.pack()
gomb2.pack()
gomb3.pack()

# Fő ablak megjelenítése
ablak.mainloop()
