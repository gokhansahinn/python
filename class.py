#class
class Person:
    pass
    #class attributes
    #Her zaman kullanmıyacağımız attributesları class içersinde
    address = 'no information'
    #contructor(yapıcı method)  #objecten gelen değişkenleri atamak için
    def __init__(self,name,year):
        #object attributes
        #objectler tanımlandığında tanımlanmasını istediğim contructolar object attibuteslar tanımlanır.
        self.name =name
        self.year=year
        print('init objesi çalıştı. ')

    #methods


#object,intances
p1=Person('Gökhan',1997)  #person clasında p1 objesi tanımlanmış oldu. p1 objesi person attributes and methodlara ulaşabiliriz.
p2=Person('Mami',2000)

#updating
p1.name='HASAN'
p2.name='KIZIL'

print(f'p1 name: {p1.name} year: {p1.year} adress:{p1.address}')
print(f'p2 name: {p2.name} year: {p2.year} adress.{p2.address}')


print(p1)    #Bellekte bir adreste yer ayarların.her obje için ayrı adresler ayrılır.
print(p2)    