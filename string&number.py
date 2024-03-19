a = 10
print(a)
a = 50
print(a)
a = a+20
print(a)
b = 6.5
print(type(b))
print(type(a))
#different numbers expression:#
print(10/10)
print(10//10)
print(2*3)
print(6%5) #it gives remainder#
print(2**3) #it is used to raise the power#
#declaring a variable#
#name of variable should not be start with capital letters and there should not be space insead of space we can use _#
#different symbols cannot be used#
#proper variable examples: 1.my_test 2.a 3.cow_name etc
my_salary = 10000 
monthly_savings = 2000
spends = my_salary-monthly_savings
print(spends)

#string#
my_string = "preeti"
print(my_string[1])
for i in my_string:
    print(i)
print(len("preeti"))    #len function is used to find the length of the string#
ind_string = "Hello, I am preeti"
print(ind_string[6])
print(ind_string[-1]) #indexing can be done from negative or from backside#
print(ind_string[2:5]) #string slicing#
print(ind_string[:])
print(ind_string[:5]) #stop index is upto 5 but not equal to 5#
print(ind_string[::2]) #string slicing is in form [start:stop:step]
#properties of string#
# my_name = "Preeti"
# my_name[0] = "T"
# print(my_name) #here,it will show errors because strings are imutable#
#instead of this strings can be concatinate#
my_name = "Preeti"
last_letters = my_name[1:]
print("D"+ last_letters)
print("2"+"3"+"4")
print(2+3+4)
letter = "p"
print(letter*5)
string = "Hello world"
b = string.replace("H","K")
print(b)
print(string.upper())
print(string.lower())
print(string.split())
r = 10/9
print(f"The result was {r}")
print(f"The result is {r:1.3f}")
