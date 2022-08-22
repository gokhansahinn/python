list= [1,2,3,4]

tuple= (1.2,45,14)

print(type(list))
print(type(tuple))

# listede olduğu gibi tuple'da indexdeki değere ulaşabilmekteyiz.
#tuple değişkenlerin içerindeki elemanlar dışarıdan değiştirilemez.

print(list[2])
print(tuple[2])

print('listenin uzunluğu {}'.format(len(list)))
print('tuple uzunluğu {}'.format(len(tuple)))

#tuple değişkenler içindeki atama yapılır index girilip değişiklik yapılmaz.
list=['ayşe','fatma']
tuple=('veli','hüseyin','veli')
names=('haydar','mümtaz','halis')

tuple2=names+tuple
list[0]='hayriye'
# tuple[0]='hayriye'

print(list)
print(tuple)

print(tuple.count('veli'))
print(tuple.index('veli'))

print(tuple2)


