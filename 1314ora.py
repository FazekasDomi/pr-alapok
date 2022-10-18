'''szam1 = int(input("kérek egy számot"))
szam2 = int(input("kérek egy másik számot"))
if szam1 > szam2:
    print("szam1 nagyobb")
if szam2 > szam1:
    print("szam2 nagyobb")
if szam1 == szam2:
    print("szam1 és szam2 eggyenlő")'''

'''
szam1 = int(input("kérek egy számot"))
szam2 = int(input("kérek egy másik számot"))
if szam1 > szam2:
    print("szam1 nagyobb")
elif szam2 > szam1:
    print("szam2 nagyobb")
elif szam1 == szam2:
    print("szam1 és szam2 eggyenlő")'''

'''szam1 = int(input("kérek egy számot"))
szam2 = int(input("kérek egy másik számot"))
if szam1 > szam2:
    print("szam1 nagyobb")
elif szam2 > szam1:
    print("szam2 nagyobb")
else szam1 == szam2:
    print("szam1 és szam2 eggyenlő")'''

'''x = None
print(x)
print(type(x))

if x:
  print("Do you think None is True?")
elif x is False:
  print ("Do you think None is False?")
else:
  print("None is not True, or False, None is just None...")'''

'''szam1 = int(input("kérek egy osztályzatot"))
 if szam1==5:
     pass print ("jeles")
 elif szam1==4:
     pass print("jó")
     
 elif szam1==3:
     pass print("közepes")
     
 elif szam1==2:
     pass print("elégséges")
     
 elif szam1==1:
     pass print("elégtelen")
     
 elif szam1<1:
     pass print("nem érvényes")
     
 else szam1>5:
     pass print("nem érvényes")''' #házi
 
 #pozitiv egész szám.páros vagy páratran
'''szam=int(input("pozitiv egészszámot kérnék"))
 if szam :
     pass

 else szam :
     pass'''

#véletlen szám előálítás
'''
import random
gondolt_szam = random.randint (1,6)
print("sugok", gondolt_szam)
tipp= input ("gondoltam egy számra")'''

import random
gondolt_szam = random.randint (1,1000)
print(gondolt_szam)
if gondolt_szam%2==0 and gondolt_szam<=500:
     print("megfelelt")
else:
     print("nem felelt meg")
