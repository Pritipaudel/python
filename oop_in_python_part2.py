from typing import Any


class Car:
    def __init__(self):
        self.wheels = 4

class Bike(Car):
    def __init__(self):
        super().__init__()
        self.wheels = 2

class Scooter(Bike):
    def __init__(self):
        super().__init__()
        self.wheels = 3
s = Scooter()  
print(s.wheels)    


#property decorator#
class student:
    def __init__(self,maths,phy,chem):
        self.math =maths
        self.physics = phy
        self.chem = chem
    @property
    def percentage(self):
        return (self.math+self.physics+self.chem)/3
        
s1 = student(55,88,95)
print(s1.percentage)
s1 = student(55,88,76)
print(s1.percentage)  

#polymorphism : having many form or operator overloading#
#polymoprphism is a case in which same operator have different meaning according to the context
print(1+2)
print("1"+"2")
print("hello"+"preeti")
print([1,2,3]+[4,5,6])
print((4,5,6)+(2,3,4))
a = {1,2,3}
a.add(4)
print(a)

#example:
# class complex:
#     def __init__(self,real,img):
#         self.real = real
#         self.img = img
#     def display(self):
#         print( self.real ,"i" "+" ,self.img,"j")   
#     def add(self,num2):
#         newreal = self.real+num2.real
#         newimg = self.img+num2.img
#         return complex(newreal,newimg)  

# num1 = complex(1,2)
# num1.display()
# num2 = complex(2,3)
# num2.display()
# result=num1.add(num2)
# result.display() 

# here, in above function we cannot directly add num1+ num2 so to do this we can use thunder function 
class complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    def display(self):
        print( self.real ,"i" "+" ,self.img,"j")   
    def __add__(self,num2):
        newreal = self.real+num2.real
        newimg = self.img+num2.img
        return complex(newreal,newimg)  

num1 = complex(1,2)
num1.display()
num2 = complex(2,3)
num2.display()
result=num1+num2
result.display() 


#practice_questions_of_OOP_
#define a circle class to createe a circle with raddius r using the constructor define an area() method
#of the class which calculate the area of the circle and define perimeter of the class that allowa 
#you to calculate the perimeter#


class Circle:
    def __init__(self,r):
        self.radius = r
    def Area(self):
        return (22/7) * self.radius**2
    def Perimeter(self):
        return 2*(22/7)*self.radius
cir1 = Circle(4)
print(cir1.Area())
print(cir1.Perimeter())     

#define a employee class with attributes role,department and salary and also define a function show details.
#create an engineer class that inherits property from emloyee and add attributes name and age.
class Employee:
    def __init__(self,role,department,salary):
        self.role = role
        self.department = department
        self.salary = salary
    def show_details(self):
        print("Role:",self.role)
        print("Department:",self.department)
        print("Salary:",self.salary)
class Engineer(Employee):
    def __init__(self,name,age,role,department,salary):
        super().__init__(role,department,salary)
        self.name= name
        self.age =age
    def showdetails(self):
        print("Name:",self.name)
        print("Age:",20)
        return super().show_details()
e1 = Engineer("preeti",20,"engineer","IT",100000)
print(e1.showdetails())    


#create a class order which stores item and its price. Use dunder function __gt__() to convey that
#order1>order2 if price of oreder 1>price of order2
class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price
    def __gt__(self,ord2):
        return self.price>ord2.price 
ord1 = Order("Papaya",100)
ord2 = Order("Apple",500)
print(ord1>ord2)   