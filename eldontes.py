#van egx n elemü sorozat. van benne egy T tulajdonság. az algoritmusom megadja nekem van e a listában iylen T tulajdonságu elem.(igen vagy nem)
lista = [2, 5, 4, 8, 19, 11, 10, 13]
    
találat=False
index=0

while index < len(lista) and not talalat:
        if lista[index] % 3 == 0:
            talalat = True
        index = index + 1
