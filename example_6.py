from io import BufferedRandom
from unicodedata import name


names = ['Ali','Yağmur','Hakan','Deniz']
years= [1998,2000,1998,1987]

#1- "Cenk" ismini listenin sonuna ekleyiniz.
names.insert(5,'Cenk')
print(1,names)
#2- "Sena" değerini listeninin başına ekleyiniz.
names.insert(0,'Sena')
print(2,names)
#3- "Deniz" ismini listeden siliniz.
names.remove('Deniz')
names.pop() #verilen indexteki değeri siler
print(3,names)
#4- "Deniz" isminin indeksi nedir?
index_deniz=names.index('Yağmur')
print(4,index_deniz) 
#5- "Ali" listenin bir elemanı mıdır ?
isALi= 'Ali' in names
print(5,isALi)
#6- Liste elemanlarını ters çevirin
names.reverse()
print(6,names)
#7- Liste elemanları alfabetik olarak sıralayanız.
names.sort()
print(7,names)
#8- years listesini rakamsal büyüklüğe göre sıralayınız.
years.sort()
print(8,years)
#9- str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz.
str  = "Chevrolet,Dacia"
list= str.split(',')
print(9,list)
#10- years dizisinin en büyük ve en küçük elemanı nedir ?
max_year=max(years)
min_year=min(years)
print(10,f'Max year {max_year} and Min year {min_year}')
#11- years dizisinde kaç tane 1998 değeri vardır ? 
count_1998= years.count(1998)
print(11,count_1998)
#12- years dizisinin tüm elemanlarını siliniz 
years.clear()
print(12,years)
#13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız. 
# Brand=[1,2,3]
# Numbers=[0,1,2]
# for x in Numbers:
#     Brand[x] = input(f'enter {x+1}.brand: ')
# print(13, Brand)
markalar=[]

marka=input('1. markayi gir: ')
markalar.append(marka)
marka=input('2. markayi gir: ')
markalar.append(marka)
marka=input('3. markayi gir: ')
markalar.append(marka)
print(13,markalar)