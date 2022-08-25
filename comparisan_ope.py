#username, password => database

#'Gökhanşahin', '123456'

from socket import if_indextoname


a,b,c,d=5,5,10,4

result= a==b #True
print(result)
result= a==c  #False
print(result)

username='Gökhanşahin'
password='12345'

result='gkhnshn'==username
print(result)
result='Gökhanşahin'==username
print(result)

result= a!=b
print(result)
result= a!=c
print(result)

result= a<c
print(result)
result= a>c
print(result)

result = a>=b
print(result)
result = a<=b
print(result)
#####################UYGULAMA##########################################################################
#1- Girilen 2 sayıdan hangi ikisi büyüktür?
first=input('enter 1. number: ')
second=input('enter 2. number: ')
if first>second:
    print(f'{first} sayisi {second} sayisinden büyüktür')
else:
    print(f'{second} sayisi {first} sayisinden büyüktür')

#2- kullanıcıdan 2 vize (%60) ve final notunu alıp ortalama hesaplayınız. Eğer ortalama
#   50 ve üstündeyse geçti değilse kaldı yazdırın
vize1=input('Enter 1. midterm grade: ')
vize2=input('Enter 2. midterm grade: ')
final=input('Enter final grade: ')
final_grade=int(vize1)*0.3+int(vize2)*0.3+int(final)*0.4
if final_grade >=50:
    print('PASS SUBJECT')
else:
    print('FAILED SUBJECT')
#3- Girilen sayının tek mi çift mi olduğunu yazdırın 
number=input('Enter number: ')
if(int(number)%2==0):
    print(f'{number} is odd ')
else:
    print(f'{number} is even')
#4- Girilen sayının negatif pozitif durumu yazdırın.
number1=input('Enter integer number: ')
if(int(number1) > 0):
    print(f'{number1} is positive')
else:
    print(f'{number1} is negative')

#5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz. 
#   (email: email@sadikturan.com parola: abc123)
email1='email@sadikturan.com'
password_1='abc123'
email=input('Enter your email:')
if(email==email1):
    print('Email is correct.')
    parola=input('Enter your password: ')
    if(parola==password_1):
        print('your password is correct. Confirm it.')
    else:
        print('Password is not correct.TRY AGAIN')
else:
    print('Your email are INVALID. ')
