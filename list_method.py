numbers=[3,23,43,5,6,7,8,8,8]
letters=['a','b','k','l','s']

val_min= min(numbers)
val_max= max(numbers)
print(1,val_min)
print(2,val_max)
let_max=max(letters)
let_min=min(letters)
print(3,let_max)
print(4,let_min)
result= numbers[2:]
print(5,result)
result= numbers[3:6]
print(6,result)
result= numbers[::-1]
print(7,result)
result= numbers[:-4:-1]
print(8,result)
#tanımlamış listeler içindeki index değerleri değiştirilebilir.
numbers[4]=50
print(9,numbers)
numbers.append(65)
print(10,numbers)
numbers.insert(3,49) #3. indexten sonra bu karakter(int, string,etc) eklenmeketedir. 
print(11,numbers)
numbers1=numbers.pop()
print(12,numbers1)
numbers2=numbers.pop(0)
print(13,numbers2)
numbers3=numbers.remove(49)
print(14,numbers)
numbers.sort()
letters.sort()
print(15,numbers)
print(16,letters)
numbers.reverse()
print(17,numbers)
print(18,len(numbers))
print(19,len(letters))
print(20,numbers.count(8))
print(21,numbers.clear())