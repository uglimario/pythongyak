alsohatar = 0
felsohatar = 0
osszeg = 0 

alsohatar = int(input("Kérem a sorozat alsó határát:"))
felsohatar = int(input("Kérem a sorozat felső határát:"))

while alsohatar <= felsohatar:
    osszeg = osszeg + alsohatar
    alsohatar = alsohatar + 1

print("A sorozat tagjainak összege=" , osszeg)