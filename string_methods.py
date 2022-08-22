message='hello There. My name is Gökhan Şahin'
message2=' hello There. My name is Gökhan Şahin'
message3=' hello/There/My/name/is/Gökhan/Şahin'
print(1,message.upper())
print(2,message.lower())
print(3,message.title())
print(4,message.capitalize())

print(5,message2.strip())  #başında ve sonunda boşluk varsa 
print(6,message2.split()) #split komutu içerisine yazılan karakterlere göre stringi ayarmaktadır.
print(7,message3.split('/')) # '/' olduğu noktalardan ayırmaktadır.
message4=message.split()
message4= '...'.join(message4) # dizinlerin arasına istenilen karakterileri yerleştirmektedir.
print(8,message4) 

print(9,message.find('Gökhan'))
print(10,message.find('kalem')) # eğer bu karakter yok ise -1 dönmekte

isdFound=message.startswith('h')  #Startwith komutu ile bir string içerisinde bu karakter bulunmakta mıdır bu kontrol edilmektedir. 
isdFound2=message.startswith('H') #Varsa TRUE yoksa FALSE dönmektedir. Büyük küçük harf olmasının bir önemi yoktur.
print(11,isdFound)
print(12,isdFound)

message5=message.replace('Gökhan','Muammer') #İlk indexdeki string bulup bunun yerine 2. indexdeki string yerleştirir.
print(13,message5)

message6=message.replace(' ','*').replace('ö','o').replace('Ş','S')
                
print(14,message6)


