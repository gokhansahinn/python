#global scope

from cgi import print_arguments


x='global x'

def function():
    x='local x'
    print(x)


function()
print(x)


#global değişken
name='Gökhan'

def change_name(new_name):
    #local değişken
    name=new_name
    print(name)

change_name('kader')
print(name)
################################################################
name='global string'

def greeting():                  #Değişkenkeri ilk önce localdeki değerlerini alıyor.Fonksiyon içinde fonksiyon olursa diğer
                                 #diğer fonksiyonun local değişkenini kullanır. 
    # name='Çınar'
    def hello():
        # name='ahmet'
        print('hello '+ name)
    hello()


greeting()