def sayHello(name='user'): #eğer bir değişken atanmazsa default olarak user gelir.
    # print(f'Hello {name}')
    return 'Hello ' + name



# sayHello('Gökhan')
# sayHello()
msg=sayHello('Gökhan')
print(msg)

def total(num1,num2):
    return num1+num2

result=total(2,3)
print(result)

def yasHesaplama(today,dogumYili):
    return today-dogumYili


yasA=yasHesaplama(2022,1997)
yasB=yasHesaplama(2022,2000)

print(yasA,yasB)

def leftyearforretired(today=2022,dogumyili=1990,isim='username'):
    '''
    DOCSTRING: CALCULATE RETİRED AGE ACCORDING YOUR AGE
    INPUT:
    OUTPUT:
    '''
    yas=yasHesaplama(today,dogumyili)
    retiredage=65-yas
    if(retiredage>0):
        print(f'Sayin {isim}. Emekliğinize {retiredage} yiliniz kaldi. ')
    else:
        print(f'{isim} zaten emeklisiniz. ')



leftyearforretired(2022,1997,'Gökhan')
leftyearforretired(2022,1950,'Veli')

print(help(leftyearforretired))