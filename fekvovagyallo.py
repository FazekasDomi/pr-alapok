szam = int(input ('adj egy szélességet'))
szam1 = int(input ('adj egy magasságot'))
if szam == szam1:
  print ("négyzte")
else szam > szam1 :
  print ("fekvő")
else szam < szam1 :
  print ("álló")
szam2 = szam*szam1
print ("területe ",szam2)
