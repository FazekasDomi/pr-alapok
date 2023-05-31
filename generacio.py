nev=input ("adj meg nevet")
ev=int(input("adja meg a születési dátumát"))
if ev > 2009:
    print("sajnélom nem beazonosíthato év")
elif ev>= 1995:
    print (f"kedves{nev}, ön z generácios")
elif ev>= 1989:
    print (f"kedves{nev}, ön y generácios")
elif ev>= 1965:
    print (f"kedves{nev}, ön x generácios")
else:
    print("sajnélom nem beazonosíthato év")