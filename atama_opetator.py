# x=5
# y=20
# z=12
#bunun yerine tek satırda atama da gerçekleştirilebilir.
from traceback import print_tb


x,y,z= 5,20,12
print(x,y,z)

x,y=y,x

print(x,y,z)



x += 5      #x=x+5
print(x,y,z)
x -= 5      #x=x-5
print(x,y,z)
x *=5       #x=x*5
print(x,y,z)
x /=5       #x=x/5
print(x,y,z)
x %=5       #x=x%5
print(x,y,z)
z //=5       #z=z//5  #tam bölme operatörü
print(x,y,z)
z **=5       #z=z**5
print(x,y,z)
values=1,2,3
print(type(values))
a,b,c=values
print(a,b,c)
##################################################################
variables1=1,2,3,4,5
k,l,*m=variables1  # * anlamı kalan list elemanları liste olarak * olan değişkene atama yapar.
print(k,l,m)
print(k,l,m[2])  # m dizisinin 2 elemanı yazdırmaktayız.
################################UYGULAMA#########################################

x,y,z=2,5,107
numbers=1,5,7,10,6

#1- kullanıcıdan aldığınız 2 sayısının çarpımı ile x,y,z toplamının farkı nedir?
first=input("enter 1.number: ")
second=input('enter 2.number: ')
result=(int(first)*int(second))-(x+y+z)
print(f'1.sonun cevabi: {result}')
#2- y'nin x e kalansız bölümünü hesaplayınız
y //=x
print(2,y)
print(f'2.sonun cevabi: {y}')
#3- (x,y,z) toplamının mod 3'ü nedir? 
sum=x+y+z
sum%=3
print(f'3.sonun cevabi: {sum}')
#4- y' nin x. kuvvetini hesaplayınız.
y**=x
print(f'4.sonun cevabi: {y}')
#5- x, *y , z = numbers işlemine göre z' nin küpü kaçtır? 
x, *y , z = numbers
z**=3
print(f'5.sonun cevabi: {x,y,z}')
#6- x, *y , z = numbers işlemine göre y'nin değerleri toplamı kaçtır?
sum_y=y[0]+y[1]+y[2]
print(f'6.sonun cevabi: {sum_y}')