#if-else statement#
# name = input("Enter your name:").lower()

# if name == "preeti":
#     print("Hello preeti!,how are you??")
# elif name == "prashanna":
#     print("Hello my handsome brother.")
# else:
#     print("May I know you??") 

#for loops#
my_list = ["preeti",20,4.5,"pushpa"]
for item in my_list:
    print(item)               

num = [4,8,10,3,5,7,6]
even = []
odd = []
for i in num:
    if i%2 == 0:
        even.append(i)
    
    else:
        odd.append(i)
print(even) 
print(odd)   

string = "hgdgdesghfhsg"
for i in string:
    print(i)

#tuple packing 
a = [(2,3),(4,5),(6,8)]
for a,b in a:
    print(a)
    print(b)  

a = [("gita",7,8),(1,2,3),(7,8,9)]
for a,b,c in a:
    print(a)   

a ={"one":1,"two":2,"three":3}
for i in a:
    print(i)   
    print(a[i])       
    

b ={"name":"Preeti","age":20,"height":5.2}
for item in b.items():
    print(item)
    
for key in b.keys():
    print(key)  

for value in b.values():
    print(value)    

#while loop#
x=0
while x<6:
    print(f"The value of x {x}")
    x = x+1
else:
    print(f"{x} is not less than 6") 

#break,continue,pass keyword#
x =[1,2,3]
for i in x:
    pass               #pass is used to remove the syntax error when loop is empty#
print("Hello")  

#break#
y = 0
while y<5:
    if y == 3:
        break
    y = y+1
    print(y)   

#continue#
string = "Nepal"
for i in  string:
    if i == "a":
        continue
    print(i)

 #range function#
for i in range(1,10,2):
    print(i)       
         
print(list(range(0,5)))

index_count = 0
my_string = "Hello"
for i in my_string:
    print(f"in index {index_count} there is {i}")
    index_count +=1

for item in  enumerate(my_string):   #enumerate function
    print(item)   


list1 = [1,2,3,4]
list2 = ["paudel","Jaisi","preeti"]
for item in zip(list1,list2):
     print(item)
    #  print(list(b))    
     
print("x" in [1,2,3,4] )    
print(1 in [1,2,3])    

print(min(list1))
print(max(list1))


#random module#

from random import randint
a = randint(0,100)
print(a)  


string1 = "mayalu"
list3  = []
for i in string1:
    list3.append(i)
print(list3)    

z = [x for x in range(1,5)]  
print(z)
    
b = [c**2 for c in range(1,12) if c%2==0]
print(b)   

celcius = [0,4,10,20]
farenhiet = [ (9/5*temp)+32 for temp in celcius  ]
print(farenhiet)
#this can be done also as#
farenhiet = []
for i in celcius:
    farenhiet.append((9/5*i)+32)
print(farenhiet)

sun = []
for i in [2,3,4]:
    for j in [12,13,14]:
        sun.append(i*j)
print(sun)             
    
    
    
    
    
    
    
    