
import statistics
# 1-"BMW, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.

cars=['BMW', 'Mercedes', 'Opel', 'Mazda']
# 2- Liste kaç elemanlıdır.
print(1,cars)
print(2,len(cars))
# 3-Listenin ilk ve son elemanı nedir.
print(3,cars[0])
print(4,cars[len(cars)-1])
# 4- Mazda değerini Toyota ile değiştiriniz.
cars[len(cars)-1]='Toyota'
print(5,cars)
# 5- Mercedes listenin bir elemanımıdır? 
result= 'Mercedes' in cars
print(6,result)
# 6- Listenin -2 indeksindeki değeri nedir? 
print(7,cars[-2])
# 7- Listenin ilk 3 elemanını alının
print(8,cars[0:3])
# 8- Listenin son 2 elemanı yerine "Toyato" ve "Renault" değerlerini ekleyiniz.
cars[-2:]=['Toyota','Renault']
print(9,cars)
# 9- Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyiniz
cars=cars+['Audi','Nissan']
print(10,cars)
# 10- Listenin son elemanını silin.
del cars[-1]
print(11,cars)
# 11- Liste elemanlarını tersten yazdırınız.
print(12,cars[::-1])
# 12- Aşağıdaki verileri bir liste içinde saklayınız.
# studentA: Yiğit Bilgi 2010, (70,60,70) 
studentA=['Yiğit','Bilgi', 2010,[70,60,70]]
# studentB: Sena Turan 1999, (80,80,70)  
studentB=['Sena','Turan', 1999,[80,80,70]]
# studentC: Ahmet Turan 1998, (80,70,90) 
studentC=['Ahmet','Turan', 1998,[80,70,90]]
# 13- Liste elemanlarınu ekrana yazdırınız. 
print(13,studentA)
print(14,studentB)
print(15,studentC)
yaşA=2022-studentA[2]
not_ortalamaA=statistics.mean(studentA[3])
yaşB=2022-studentB[2]
not_ortalamaB=statistics.mean(studentB[3])
yaşC=2022-studentC[2]
not_ortalamaC=statistics.mean(studentC[3])
resultA= f"{studentA[0]} {studentA[1]} {yaşA} yaşında ve not ortalaması {not_ortalamaA}"
resultB= f"{studentB[0]} {studentB[1]} {yaşB} yaşında ve not ortalaması {not_ortalamaB}"
resultC= f"{studentC[0]} {studentC[1]} {yaşC} yaşında ve not ortalaması {not_ortalamaC}"
print(16,resultA)
print(17,resultB)
print(18,resultC)


