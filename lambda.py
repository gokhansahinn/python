# def square(num):
#     return num**2

numbers=[1,3,5,9,10,4,44]

# result=map(square,numbers)

# print(result)

# result=list(map(square,numbers))
# print(result)

# for numbers in map(square,numbers):
#     print(numbers)

square=lambda num: num**2
result=list(map(lambda num:num**2,numbers))# map fonksiyonun görevi dizinin elemanlarını tek tek fonksiyona göndermek.
print(result)
result=list(map(square,numbers))
print(result)
result=square(3)
print(result)

def check_even(num): return num%2==0
check_even1=lambda num:num%2==0
result=list(filter(check_even,numbers))
print(result)
result=list(filter(lambda num:num%2==0,numbers))
print(result)
result=list(filter(check_even1,numbers))
print(result)
result=check_even1(4)
print(result)
