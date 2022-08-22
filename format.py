name='Muhammed'
last_name='S.A.V'
age='36'

print(1,'My name is {} {}'.format(name,last_name))
print(2,"My name is {0} {1}".format(name,last_name))
print(3,"My name is {1} {0}".format(name,last_name))

print(4,"My name is {n} {l}".format(n=name,l=last_name))
print(5,"My name is {} {}. I am {} years old. ".format(name,last_name,age))

print(f"My name is {name} {last_name}. I am {age} years old. ")
result=2/7

print("result= {}".format(result))
print("result= {r:1.3}".format(r=result)) #r:1.3 3-> 0'dan sonra 3 basamak alanacağının açıklaması.
print("result= {r:1.4}".format(r=result))