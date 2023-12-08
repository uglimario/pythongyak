tomeg = float(input("Kérem adja meg a testsúlyát (kg):"))
magassagcm = float(input("Kérem adja meg a magasságát (cm):"))
magassagm = magassagcm / 100

BMI = 70 / (1.75 * 1.75)
alanyBMI = tomeg / (magassagm * magassagm)
print("A BMI-d:", alanyBMI)

if alanyBMI < 18.5:
    print("Sovány vagy")
elif 18.5 <= alanyBMI < 24.9:
    print("Normál")
elif 25 <= alanyBMI < 29.9:
    print("Túlsúlyos vagy")
elif alanyBMI >= 30:
    print("Elhízott vagy... (túlzottan is)")
    print("  _o_  ")
    print("(     )")
    print(" \   /")
    print("  I^I ")
else:
    print("Nem értelmezhető")  