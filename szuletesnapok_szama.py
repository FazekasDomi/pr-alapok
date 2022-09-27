idei_év = 2022 # módosítva
születési_év = input('2006 ')
születési_év = int(születési_év)
volte = input('i')
szülinapok_száma = idei_év - születési_év - 1
if volte == 'i':
 szülinapok_száma = szülinapok_száma + 1
print('Utoljára a ', szülinapok_száma, '. születésnapodat ünnepelted.', sep='')
