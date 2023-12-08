import tkinter as tk

def gomb1_click():
    print("1. gombra kattintottál")
    ablak.destroy()

def gomb2_click():
    print("kutyusssss gombra kattintottál")
    ablak.destroy()

def gomb3_click():
    print("halooo gombra kattintottál")
    ablak.destroy()

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
gomb2 = tk.Button(ablak, text="Négyzet", command=gomb2_click, bg="red", fg="blue", font=("Helvetica", 22))
gomb3 = tk.Button(ablak, text="Kör", command=gomb3_click, bg="blue", fg="white", font=("Helvetica", 22))

gomb1.place(relx=0.8605, rely=0.67, anchor=tk.CENTER)
gomb2.place(relx=0.14, rely=0.5, anchor=tk.CENTER)
gomb3.place(relx=0.52, rely=0.5, anchor=tk.CENTER)

ablak.mainloop()
