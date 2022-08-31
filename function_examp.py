# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız.
print('1. Soru: ')
def display(count, msg=''):
    x=0
    while x<count:
        print(msg)
        x+=1

msgUser=input('Can u write message please: ')
display(5,msgUser)
# 2- kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazınız.
print('2. Soru: ')

def liste(*args):
    mylist=[]
    for param in args:
        mylist.append(param)
    return mylist

print(liste('a','b','c',2,'kalem', 'silgi'))

# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulunuz.
print('3.Soru: ')
def asal(num1,num2):
    asalnum=[2]
    for x in range(num1,num2+1):
        # print(x)
        asalmi=True
        for y in range(2,x):
            # print(y)
            if(x % y==0):
                asalmi=False
        if(asalmi==True):
            asalnum.append(x)

    return asalnum


print(asal(3,12))
# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şekilde döndüren bir fonksiyon yazınız.
print('4. SORU: ')
def asal_tam(num1):
    tam_bol=[]
    for x in range(2,num1):
        if(num1%x==0):
            tam_bol.append(x)

    return tam_bol

num_asal=int(input('Enter asal sayi: '))

print(asal_tam(num_asal))


