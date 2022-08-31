# 1-100 e kadar

x=1 

# while x <=100:
#     print(x)
#     x +=1
# print('sayma işlemi bitti. ')


while x<=100:
    if x%2==0:
        print(f'{x} çift sayıdır.')
    else: 
        print(f'{x} tek sayıdır.')
    x +=1
name='' #FALSE

while not name.strip(): #while koşulu turu olduğu sürece dönmekte
    name= input('isminizi giriniz: ')
print(f'Hello {name}')
###################UYGULAMA###################################################
sayilar=[1,3,5,7,9,12,19,21]
# 1: sayilar listesinde while ile ekrana yazdırın.
print('1.soru:')
x=0
while x<=len(sayilar)-1:
    print(sayilar[x])
    x +=1
# 2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları
#     ekrana yazdırınız.
print('2.soru: ')
# start_value=int(input('Başlangıc numarasını giriniz: '))
# last_value=int(input('bitişi değerini giriniz: '))
x=0
sayac=len(sayilar)
while x<=sayac+2-1:
    if(x==0):
        start_value=int(input('Başlangıc numarasını giriniz: '))
        sayilar.insert(x,start_value)
    elif(x==(sayac+2)-1):
        last_value=int(input('bitişi değerini giriniz: '))
        sayilar.insert(x,last_value)
    x +=1
y=0
while y<=len(sayilar)-1:
    if(sayilar[y] %2!=0):
       print(sayilar[y])
    y += 1
# 3: 1-100 arasındaki sayıları azalan şekilde yazdırın.
print('3.soru: ')
y=100
while y>0:
    print(y)
    y -=1
print('işlem bitti')
# 4: Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırınız.
print('4. Soru: ')
x=0
sayilar1=[1,2,3,4,6]
while x<5:
    sayilar1[x]=int(input(f'{x+1} . sayi giriniz: '))
    x +=1
sayilar1=sayilar1.sort()
print(sayilar1)



# # 5: Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayız.
#     **ürün sayısını kullanıcıya sorun.
#     **dicrionary listesi yapısı (name, pirce) şeklinde olsun .
#     **ürün ekleme işlemi bittiğinde ürünleri ekrandan while ile listeleyin.

