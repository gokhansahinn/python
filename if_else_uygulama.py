#1- Kullanıcıdan isim yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz. Ehliyet alma koşulu en az 18
#ve eğitim durumu lise ya da üniversite olmalıdır.
isim=input('Enter your name: ')
yas=int(input('Enter your age: '))
egitim_durumu=input('Enter your status of school: ')
if(yas>18 and (egitim_durumu=='Lise' or egitim_durumu == 'Üniversite')):
    print('Ehliyet alabilirsiniz')
else:
    print('Ehliyet alamazsınız.')
# 2- Bir öğrencinin 2 yazılı 1 sözlü notunu alıp hesaplanan ortalmaya göre 
#     not aralığına karşılık gelen not bilgisini yazdırınız.
#     0-24   => 0
#     25-44  => 1
#     45-54  => 2
#     55-69  => 3
#     70-84  => 4
#     85-100 => 5
yazili1=int(input('1. yazilini notunuzu giriniz: '))
yazili2=int(input('2. yazilini notunuzu giriniz: '))
yazili3=int(input('3. yazilini notunuzu giriniz: '))
ort=(yazili1+yazili2+yazili3)/3
if(ort>=0 and ort<=24):
    print('notunuz 0')
elif(ort>=25 and ort<=44):
    print('Notunuz 1')
elif(ort>=45 and ort<=54):
    print('Notunuz 2')
elif(ort>=55 and ort<=69):
    print('Notunuz 3')
elif(ort>=70 and ort<=84):
    print('Notunuz 4')
else:
    print('Notunuz 5')
# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız.
#     1. Bakım => 1.yıl
#     2. Bakım => 2.yıl
#     3. Bakım => 3.yıl
today=2022
date_of_car=int(input('aracinizin trafiğe çikiş tarifini yaziniz: '))
year=today-date_of_car
if(year==1):
    print('1.Bakim')
elif(year==2):
    print('2. Bakim')
elif(year==3):
    print('3.bakim')
else:
    print('Bakim süresi dolmuştur.')