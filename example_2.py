"""
    daire alanı : pir^2
    daire cevresi : 2*pi*r
    * Yari capi verilen bir dairenin alani ve cevresini hesaplayiniz(r: 3.14)
"""
import math

# radius= input("Enter radius of circule: ")
radius= float(input("Enter radius of circule: "))
# radius2=float(radius)
dairenin_alani= math.pi*radius**2
dairenin_cevresi=2*math.pi*radius

print("dairenin alanı= {}".format(dairenin_alani))
print("dairenin cevresi= {}".format(dairenin_cevresi))