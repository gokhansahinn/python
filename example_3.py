'''
website ="http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz(40 saat)"

print(len(website))
print(website[7:10])
print(website[len(website)-3:len(website)])

print(course[:15])
print(course[-1:15])

print(course[::-1])

s='12345'*5
print(s)
print(s[::5])
'''

name,surname, age, job='Gökhan','Şahin',25,'mühendis'
print(1,"Benim adım {} {}, Yaşım {} ve mesleğim {}.". format(name, surname, age, job))
print(2,f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}.")

#7. 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.

s='Hello world'

result=s[0:6]+'W'+s[7:11]
print(1,result)
result=s[0:6]+'W'+s[-4:]
print(2,result)
s.replace('w','W')
print(3,s)
#8. 'abc' ifadesini yan yana 3 defa yazdırın
a='abc'
print(4,a*3)








