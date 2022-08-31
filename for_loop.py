d= {"k1": 1, "k2": 2}
for x in d:
    print(x)
for x,y in d.items():
    print(x,y)

tuple=[(1,2),(1,3),(3,5),(5,7)]
for a,b in tuple:
    print(a,b)
for a,b in tuple:
    print(a)
############# UYGULAMA ########################
sayilar=[1,3,5,7,9,12,19,21]
# 1- Sayilar listesindeki hangi sayılar 3 katıdır?
print('1.SORU')
for num in sayilar:
    if(num%3==0):
        print(f'{num} is times of 3')
    else:
        print(f'{num} is not times of 3')
# 2- Sayilar listesindeki sayıların toplamı kaçtır?
print('2.SORU')
sum=0
for num in  sayilar:
    sum+=num
print(sum)
# 3- Sayilar listesindeki tek sayiların karesini alınız.
print('3.SORU')
m=0
for num in  sayilar:
    if(num%2!=0):
        print(f'{num} is square {num**2}')

sehirler = ['kocaeli', 'istanbul','ankara','izmir','rize']
# 4- Şehirlerin hangileri en fazla 5 karakterlidir.
print('4.SORU')
for sehir in sehirler:
    if(len(sehir)<=5):
        print(f'{sehir} en fazla 5 harflidir.')


urunler= [
    {'name': 'samsung S6','price':'3000'},
    {'name': 'samsung S7','price':'4000'},
    {'name': 'samsung S8','price':'5000'},
    {'name': 'samsung S9','price':'6000'},
    {'name': 'samsung S10','price':'7000'},
 ]
# 5- Ürünlerin fiyatları toplamı nedir? 
print('5.SORU')
total_fiyat=0
for urun in urunler:
    total_fiyat+=int(urun['price'])
print(total_fiyat)
# 6- Ürünlerin fiyatı en fazla 5000 olan ürünleri gösteriniz? 
print('6.SORU')
for urun in urunler:
    if(int(urun['price'])<=5000):
        print(urun['name']+ 'fiyatı 5000 ve düşüktür. ')
    else:
        print(urun['name']+ 'fiyatı 5000 den yüksektir.')