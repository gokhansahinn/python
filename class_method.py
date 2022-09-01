# class Person():
#     #class attributes
#     adress='no information'
#     #object attributes
#     def __init__(self,name,year):
#         self.name=name
#         self.birtday=year
#     #instance methods
#     def intro(self):
#         print('Hello There '+self.name)

#     def calculateAge(self):
#         return 2022-int(self.birtday)

# p1=Person('Gökhan','1997')
# p2=Person('Muammer','2000')

# p1.intro() 
# p2.intro()

class Circule():
    #class object attribute
    pi=3.14
    def __init__(self,radius):
        #object attribute
        self.radius=radius
    def calculateArea(self):
        return self.pi*(self.radius)**2
    def calculateCircumtance(self):
        return 2*self.pi*self.radius

c1=Circule(3)

print(f'C1 area: {c1.calculateArea()}')
print(f'C1 circumtance: {c1.calculateCircumtance()}')


# print(p1.calculateAge())
# print(p2.calculateAge())

