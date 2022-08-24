#value type -> string, int, float
#bir değişkenin değişikliğini diğerine atarsan ve attığın değişkenin değerini değiştirirsen diğer değişken değişmez.

x=5
y=35

x=y
y=10
print(x,y)

#reference -> list,class 
# reference değişkenlerde atanan değerdeki değer değiştirilirse atanılan değişkendeki değer de değişir.
#iki list değikenni aynı adresi taşımaktadır.Birindeki veriyi diğerine eşitledikten sonra
# bundan dolayı birinde yapılan değişiklik diğerini etkilemektedir.

a=['apple','banana']
b=['apple', 'banana']

a=b

b[0]='watermelon'

print(a)
print(b)
