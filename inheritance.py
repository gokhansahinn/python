#inheritance(kalıtım): Miras alma

#Person => name, lastname, age, eat(), run(), drink()
#person classı için olan attritube'ların tekrar tanımlamak adına bu attritube'leri başka klaslarda kullabilmekteyiz. 
#temel class olacak.
#Student(Person),Teacher(Person)

from tokenize import PseudoExtras


class Person():
    def __init__(self,fname,lname):
        self.firstName=fname
        self.lastName=lname
        print('person created')
    def who_i_am(self):
        print('I am a person')
    def eat(self):
        print('I am eating')

class Student(Person):
    def __init__(self,fname,lname,student_ID):
        Person.__init__(self,fname,lname)
        self.studentNumber=student_ID
        print('Student Created. ')

    #override
    # def who_i_am(self):
    #     print('I am student')

class Teacher(Person):
    def __init__(self, fname, lname,branch):
        Person.__init__(self,fname,lname)
        self.branch=branch

    def who_i_am(self):
        print(f'I am teacher of {self.branch}')
        

p1=Person('Gökhan','Şahin')
s1=Student('Muammer','Şahin',123456)
t1=Teacher('Aydoğan','Savran','Embeded')


print(p1.firstName+ ' '+ p1.lastName)
print(s1.firstName+ ' '+ s1.lastName+' '+str(s1.studentNumber))
print(t1.firstName+ ' '+ t1.lastName+' '+t1.branch)



p1.who_i_am()
s1.who_i_am()
t1.who_i_am()
p1.eat()
s1.eat()

