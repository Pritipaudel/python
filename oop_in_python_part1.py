# creatiing class
class Student:
    name = "priti"
#creating object(also called instance)
s1=Student
print(s1.name)

class cars:
    color = "black"
    brand = "TESLA"
Car1 = cars()
print(Car1.color)
print(Car1.brand)    

#constructors#
class School:
    collage = "Padmakanya"  #class attribute
    #default constructor
    def __init__(self):
        pass
    #parametrized constructors
    def __init__(self,name ,marks):
        
        self.name = name    #instance attribute means its value is different for differents objects
        self.marks = marks
       

s1 = School("Preeti" ,88)
print(s1.name,s1.marks)
s2 = School("kajol",48)
print(s2.collage ,s2.name,s2.marks)



#attributes are the data such as name,marks and attributes are of two type:1.class 2.object#
#class atributes means whose value is same for different object

#methods are the function that belongs to object#
class office:
    def __init__(self,employee_name,post): #constructor#
        self.name = employee_name          #instance attributes
        self.post = post
    def introduction(self):   #methods#
        print(f"hello my name is {self.name} and I am in {self.post} position")
Em1 = office("Preeti","ML engineer")
print(Em1.name,Em1.post)        
Em1.introduction()   #accessing methods#

#problem to practice#
# create student class that takes name and marksof 3 subjects as argument in constructor 
# then create a method to print the average

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
        
    def average(self):
       sum = 0
       for i in self.marks:
           sum +=i
           average_marks = sum/3
       return average_marks   

s1 = Student("Preeti", [65, 75, 85])
print(s1.name,set( s1.marks)) 
averages_marks=s1.average()  
print(averages_marks) 


#staatic method is used when there is no boject in function than it can be use directly without self parameter
class hellobunny:
    @staticmethod
    def hellos():
        print("hello")
h1 = hellobunny()
h1.hellos()   


# Abstraction: hiding implementation details of the class and only showing essential feauters to user#
# Example:#
class car:
    def __init__(self):
        self.accelerator = False
        self.brk = False
        self.clutch = False
    def car_started(self):
        self.clutch = True
        self.accelerator = True
        print("Car started..")
c1 = car()
c1.car_started() 

# Encapsulation : wrapping up data into a single unit#

# Example #
class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.acc_no = acc
    def debit(self,amount):
        self.balance -= amount
        print(f"{amount} was credited")
        print(f"Total balance is {self.get_balance()}")
    def credit(self,amount):
        self.balance += amount
        print(f"{amount} was credited")
        print(f"Total balance is {self.get_balance()}")  
    def get_balance(self):
        return self.balance      
acc1 = Account(10000,101010203040)
acc1.debit(1000)
acc1.credit(2000) 
acc1.get_balance()   


#delete method#
# class student:
#     def intro(self,name,age):
#         self.name = name
#         self.age = age
# s1 = student()
# s1.intro("preeti",20)
# del s1.intro
# del s1.name    
# print(s1.age)
# print(s1.name)      

#private methods#
class Person:
    def __intro(self):
        self.name = "Preeti"   #its private private can be made using __
    def hello(self):
       self.__intro()    
p1 = Person() 
p1.hello()
print(p1.name)  


#inheritance: when one class derives the properties and method of another class(base/parent)
#example:#
class car():
    color = "black"
    @staticmethod
    def start():
        print("Car started")
    @staticmethod
    def stop():
        print("Car stopped")
class Toyatocar(car):
    def __init__(self,name):
        self.name = name
car1= Toyatocar("Tesla")
print(car1.start())
print(car1.name)
print(car1.color)
print(car1.stop())                    


#Types of inheritance#
#single inheritance: in which there is one base class and one derived class#
class car():
    color = "black"
    @staticmethod
    def start():
        print("Car started")
    @staticmethod
    def stop():
        print("Car stopped")
class Toyatocar(car):
    def __init__(self,name):
        self.name = name
car1= Toyatocar("Tesla")
print(car1.start())
print(car1.name)
print(car1.color)
print(car1.stop()) 

#Multilevel inheritance : one base class and two derived class#
class Car:
    @staticmethod
    def start():
        print("Car started")
    
    @staticmethod
    def stop():
        print("Car stopped")

class Toyatocar(Car):
    def __init__(self, brand):
        super().__init__()
        self.brand = brand

class Fortuner(Toyatocar):
    def __init__(self, brand, type):
        super().__init__(brand)        #super method which is used to access attributes of parent class to the base class
        self.type = type

car1 = Fortuner("Toyota", "Diesel")
car1.start()
car1.stop()

#Multiple inheritance: it inherits the property from multiple class to the base class#
class A:
    varA = "Welcome to  the section A"
class B:
    varB = "welcome to the section B"
class C(A,B):
    varC = "Welcome to the section C"
C1=  C()
print(C1.varA)
print(C1.varB)
print(C1.varC)

#class method#
class Person:
    name = "Preeti"
    def changename(self,name):
        # Person.name = name
        self.__class__.name = "Rahul"

p1 = Person()
p1.changename("Kritika")
print(p1.name)
print(Person.name)  