név =int(input ( 'mi a neved?' ))
szam =int (input ('hány éves vagy?'))
if szam < 1:
     print("csecsemő vagy", név)
else szam <6:
     print ("kisgyerek vagy", név)
else szam <12:
     print ("gyerek vagy", név)
else szam <16:
     print ("serdülő vagy", név)
else szam <25:
     print ("ifju vagy", név)
else szam <65:
     print ("felnött vagy", név)
else szam >=65:
     print ("nyugdijjas vagy", név)
#-----
