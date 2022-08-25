#Identity Operator: is 

x=y=[1,2,3]  #Bunlar aynı adrese sahiptir.
z=[1,2,3]    #Bu ise x ve y den ayrı bir adrese sahipdir.

print(x==y)
print(x==z)  #Eşit eşit operatörü sadece değişken içersindeki değerleri karşılaştır.

# is ise değişkenlerin adresslerini kontrol eder aynı ise True farklı ise False döner.

print(x is y)
print(x is z) #False dönmesini beklemekteyiz.
print(x is not z) #True Dönmesini beklemekteyiz
# Membership Operator: in
x=['apple','banana']
print('banana' in x)

y='Gökhan Şahin'
print('Ş' in y)# y string içinde Ş karakteri var mı ? 
print('Ş' not in y) # y string içinde Ş karakteri yok mu ? 