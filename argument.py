# def add(a,b):
#     return sum((a,b))
# print(add(10,20))

# def add(*params): #tek yıldız argumant olarak tuple geleceğini bildirmektedir.
#     print(params[0])
#     print(params[1])
#     return sum(params)


# print(add(10,20))
# print(add(10,20,30))
# print(add(10,20,30,40,10))





def displayUsers(**args):
    print(type(args))
    # print(args)
    for key,value in args.items():
        print('{} is {}'.format(key,value))
print('1.users: ')
displayUsers(name='Çınar',age=2,city='istanbul')
print('2.users: ')
displayUsers(name='ada',age=12,city='kocaeli',phone='123456')
print('3.users: ')
displayUsers(name='Yiğit',age=25,city='ankara',phone='123456',email='email@gmail.com')

def myFunc(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

myFunc(20,32,33,555,56,77,key1='KALEM',key2='DEFTERS',name='ali')
