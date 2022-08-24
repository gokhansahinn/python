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
