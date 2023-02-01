lista = [1,2,3,4,5,6]
min=lista[0]
max=lista[0]
for szam in lista:
    if szam <min:
        min=szam
    if szam>max:
        max=szam

print("a lsita a listában",min)
print("a legnagyobb a listában",max)

