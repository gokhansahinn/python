x=5

result=5<x<10
print(result)
#Bütün ifadeleri yukarıda belirtilene göre ifade edilemektedir.
#bunun yerine
# and
#TRUE AND TRUE => TRUE
#TRUE AND FALSE => FALSE
# or
#TRUE OR TRUE => TRUE
#TRUE OR FALSE => TRUE
#FALSE OR FALSE => FALSE
# not 
#gibi ifadeler kullanılmakktadır. yukarıdak, örneği 
result= (5<x) and (x<10) 
print(result)
#################################################UYGULAMA################################################################
#1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
sayi=input('sayi giriniz: ')
if(int(sayi)>0 and int(sayi)<100):
    print(f'{sayi} 0-100 arasındadır.')
else:
    print('sayi aralikta değil')
#2- Girilen bir sayının pozitif çift sayı olupn olmadığını kontrol ediniz
sayi2=input('sayi giriniz: ')

if(int(sayi2)>0 and int(sayi2)%2==0):
   print(f'{sayi2} pozitif ve çift sayidir.')
else:
    print(f'{sayi2} negatif ve çift sayi değidir.')
#3- Email ve parola bilgileri ile giriş kontrolü yapınız.
#4- Girilen 3 sayıyı büyüklük olarak karşılaştırız.
sayi1=input('enter 1.number: ')
sayi2=input('enter 2.number: ')
sayi3=input('enter 3.number: ')
if(int(sayi1)>int(sayi2)):
    if(int(sayi1)>int(sayi3)):
        print(f'En büyük sayi{sayi1}')
    else:
        print(f'En büyük sayi {sayi3}')
else: 
    if(int(sayi2)>int(sayi3)):
        print(f'En büyük sayi{sayi2}')
    else:
        print(f'En büyük sayi {sayi3}')

#5- Kullanıcıdan 2 vize (%60) ve final notunu alıp ortalama hesaplayınız. Eğer ortalama
#50 ve üstündeyse geçti değilse kaldı yazdırın.
vize1=input('Enter 1. midterm grade: ')
vize2=input('Enter 2. midterm grade: ')
final=input('Enter final grade: ')
#      a-) Ortalama 50 olsa bile final notu en az 50 olmalıdır.
final_grade=int(vize1)*0.3+int(vize2)*0.3+int(final)*0.4
if(final_grade>=50 and int(final)>=50):
    print('PASS LESSON.')
else:
    print('FAILED LESSON.')
    
#      b-) Finalden  70 aldığında ortalamanın bir önemi olmasın.
if(int(final)>=70 or final_grade>=50):
    print('PASS EXAM.')
else: 
    print('FAILED EXAMS.')
#6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indexlerini hesaplayınız. 
#   Formül: (Kilo/ boy uzunluğunun karesi)
#   Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#   0-18.4    =>  Zayıf
#   18.5-24.9 =>  Normal
#   25-29.9   =>  Fazla Kilolu
#   30.0-34.9 =>  Şişman (Obez)
name=input('Enter name: ')
kilo=input('Enter kilogram of body: ')
boy=input('Enter boy(m): ')
index=float(kilo)/(float(boy)**2)
print('name')
if(index>0 and index<18.4):
    print(f'{index} ZAYIF.')
elif(index>18.5 and index<24.9):
    print(f'{index} NORMAL.')
elif(index>25.0 and index<29.9):
    print(f'{index} FAZLA KILOLU.')
elif(index>30 and index<34.9):
    print(f'{index} ŞİŞMAN.')
else:
    print('Its not SCALE.')

    








