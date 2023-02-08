'''számok=[3,21,7,63,9,27]'''

#összegzés tetele: van egy n elemü sorozat és az algoritmus kiszámolja az elemek összegét
számok=[3,21,7,63,9,27]
összeg=[0]
for rész in számok:
    összeg=összeg+rész

print(összeg)

# lista elemeinek átlaga
átlag=None
átlag =összeg/len(számok)
print("az átlag", átlag)
