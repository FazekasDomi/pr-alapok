lista = ["alma","banán","cseresznye"]
print(len(lista))

lista1 = ["alma","banán","cseresznye"]
lista2 = [1,2,3,4]
lista3 =[True,False,False]


lista1 = ["alma",12,True]

lista5 = ["alma","banán","cseresznye"]
print(type(lista5))

lista = (("alma","banán","cseresznye"))
print(list(lista))

lista = ["alma","banán","cseresznye"]
print(lista[1])

lista = ["alma","banán","cseresznye"]
print(lista[-1])

lista = ["alma0","banán-1","cseresznye-2","narancs-3","kivi-4","szöllő-5","mango-6"]
print(lista[2:5])

lista = ["alma0","banán-1","cseresznye-2","narancs-3","kivi-4","szöllő-5","mango-6"]
print(lista[1:6])

lista = ["alma0","banán-1","cseresznye-2","narancs-3","kivi-4","szöllő-5","mango-6"]
print(lista[-4:-1])

lista = ["alma0","banán-1","cseresznye-2","narancs-3","kivi-4","szöllő-5","mango-6"]
if "banán-1" in lista:
    print("benne van")
    
lista = ["alma0","banán-1","cseresznye-2","narancs-3","kivi-4","szöllő-5","mango-6"]
if "banán-0" in lista:
    print("benne van")

lista = ["alma0","banán-1","cseresznye-2","narancs-3","kivi-4","szöllő-5","mango-6"]
if "banán" in lista:
    print("benne van")

lista = ["alma","banán","cseresznye"]
lista[1]=("kivi")
print(len(lista))

lista = ["alma","banán","cseresznye"]
lista[1]=("kivi","szilva")
print(len(lista))

lista = ["alma","banán","cseresznye"]
lista[1,2]=("kivi")
print(len(lista))
