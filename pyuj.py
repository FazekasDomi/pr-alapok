
print('Ez a program kiszámolja az átlagodat.')
print('Ha már nem akarsz több jegyet megadni, írj 0-át!')
print('--------------------------------------------')

darab = 0
osszeg = 0

erdemjegy = int(input('Add meg az első érdemjegyet: '))
while erdemjegy != 0:
    darab = darab + 1
    osszeg = osszeg + erdemjegy
erdemjegy = int(input('Add meg az következő érdemjegyet: '))
	
if darab != 0:
	      print('A jegyeid átlaga: ', osszeg / darab)
else:
	      print('Nem adtál meg egy jegyet sem!')
  

lista = [2, 5, 4, 8, 9, 11, 10, 12]

talalat = False
index = 0
while not talalat:
	if lista[index] % 3 == 0:
		        talalat = True
index = index + 1
print('A hárommal osztható szám indexe a listában: ', index-1)