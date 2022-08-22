website = "http://www.sadikturan.com"
course= "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1- ' Hello Word ' karakterlerinin baş ve sondaki boşluk karakterlerini silin.
message= " Hello Word "
print(1,message.strip())
# 2- 'www.sadikturan.com' içindeki sadikturan bilgisi hariçindeki her karakteri silin. 
message= 'www.sadikturan.com'
print(2,message.strip('w.com')) #strip fonksiyonu içerine yazılan karakterleri silmektedir.
# 3- 'course' karakter dizisinin tüm karakterlerinin küçük harf yapın.
print(3,course.lower())

# 4- website içinde kaç tane a karakteri vardır? 
x=website.count('a')
y=website.count('www')
z=website.count('a',0,10)#0-10 string için dizi ifadesi belirtmektedir. yani 0-10 karakterlerinde kaç tane var.?
print(4,x)
print(5,y)
print(6,z)
# 5- website www ile başlayıp com ile bitiyor mu ? 
result= website.startswith('www')
print(7,result)
result= website.startswith('http')
print(8,result)
result=website.endswith('.com')
print(9,result)
# 6- website içinde '.com' ifadesi var mı?
result= website.find('com')
print(10,result)
result= website.find('a')# karakteri ilk nerede ise onun posizyonu geri dönmektedir.
print(11,result)
result= website.rfind('a')# karakterin en son nerede ise onun posisyonu geri dönmektedir.
print(12,result)
result= website.index('com')
print(13,result)
#7- course içindeki karakterlerin hepsi alfabetik mi ? 
result=course.isalpha()
print(14,result)
result='hello'.isalpha()
print(15,result)
result= course.isdigit()
print(16,result)
result='123'.isdigit()
print(17,result)
# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
result= 'Contents'
print(18,result.center(50))
print(19,result.center(50,'*'))
print(20,result.ljust(50,'*'))
print(21,result.rjust(50,'*'))
# 9- 'couse' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin
print(22,course.replace(' ','-'))
print(23,course.replace(' ','-',5))# ilk 5 karaktere kadar ' ' yerine '-' replace et
print(24,course.replace(' ','',5))
print(25,course.replace(' ','',2))
# 10- 'Hello Word' karakter dizisinin 'World' ifadesinin yerine 'There' olarak değiştirin
result= 'Hello Word'
print(26,result.replace('Word','There'))
# 11- 'Course' karakter dizisini boşluk karakterlerinden ayırın.
result=course.split()
print(27,result)
