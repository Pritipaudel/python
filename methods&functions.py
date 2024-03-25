#functions in python#
# def fun_name(name ):
#     print("Hello " + name)
# fun_name("Preeti")   

# #basic functions#
# def sum(num1,num2):
#     return num1+num2
# result = sum(4,5)
# print(f"The sum is {result}")

#function with logic:#

# def identify_number(num):
#     if num%2==0:
#         return "even number"
#     else:
#         return "odd number"
# result = identify_number(8)
# print(result)    

# def num_check(number):
#     return number%2==0
# res = num_check(5)
# print(res)

# def check_list(num_list):
#     for i in num_list:
#         if i %2==0:
#             return True
#         else:
#             pass
#     return False
# rest = check_list([1,2,5])  
# print(check_list([2,4,6]))
# print(rest)    

# even = []

# def check_even(num_list):
#     for number in num_list:
#         if number % 2 != 0:
#             even.append(number)
#     return even

# result_list = check_even([4, 5, 6, 7, 8])
# print(result_list)

# employee_data = [("rita",600),("gita",400),("nyka",500)]
# def employee_s(employee_data):
#     employee_of_month = ""
#     max_hours = 0
#     for name,hour in employee_data:
#         if hour>max_hours:
#             max_hours = hour
#             employee_of_month = name
#         else:
#             pass    
#     return(employee_of_month,max_hours)
# ret = employee_s(employee_data)
# print(ret) 


# from random import shuffle

# list_shuffle = [1, 2, 3, 4, 5, 6, 7]  # Corrected 67 to 6
# shuffle(list_shuffle)
# print(list_shuffle)

# #in fuunction#
# def list(list_shuffle):
#     shuffle(list_shuffle)
#     return list_shuffle
# value = list(list_shuffle)
# print(value)


#map function#
def addition(n):
    return n + n
 
# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))


def mapped(my_string):
    if len(my_string) %2 == 0:
        return my_string
    else:
        return my_string[1]
string_name = ["preeti","ram","sita"]
result = map(mapped,string_name)
print(tuple(result))

def check_even(num):
    if num%2==0:
        return num
numbers = [2,3,4,5,6,7,8,12,14]
res = list(filter(check_even,numbers))    
print(res)

#lambda function in map and filter#
a = list(filter(lambda num:num%2==0,numbers))
print(a)

b = tuple(filter(lambda my_string:len(my_string)%2==0,string_name))
print(b)

my_nums = [1, 2, 3, 4, 5]
square_num = tuple(map(lambda num: num ** 2, my_nums))
print(square_num)
print(my_nums)  # This will print the original list, [1, 2, 3, 4, 5]


#nested statement and scope@
name = "may I talk to you??"

def name_fun():
    name = "Preeti"
   
    def greet():
        print("Hello " + name)

    greet()  # Call greet() inside name_fun()

name_fun()  # Call name_fun()
