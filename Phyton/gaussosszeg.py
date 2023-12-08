alsohatar = 0
felsohatar = 0
osszeg = 0 

alsohatar = int(input("Kérem a sorozat alsó határát:"))
felsohatar = int(input("Kérem a sorozat felső határát:"))

szamossag = (felsohatar - alsohatar) + 1

osszeg = int(((alsohatar + felsohatar) * szamossag) / 2)

print("A sorozat elemeinek az összege=" , osszeg)