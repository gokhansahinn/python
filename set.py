fruits={'orange','apple','banana'} #set list 

#print(friuts[0])  #indekslenemez.

#elemanlarına ulaşmak için

for x in fruits:
    print(x)

#eğer set listeye eleman eklemek istersek. add methodunu kullanabiliriz.

fruits.add('cherry')
print(fruits)
#eğer set listeye birden fazla eklemek istersek bu sefer de update methodu kullanılır. 
#eğer eklenen eleman liste içersinde içerisinde mevcut ise bu listeye tekrar eklenmez.
fruits.update(['mango','grape','apple'])
print(fruits)
#eğer istenilen bir eleman silinebilmesi için remove methodu kullanılmaktadır.
fruits.remove('apple')
print(fruits)
fruits.discard('mango')
print(fruits)
fruits.clear()
print(fruits)