my_list = [1,2,3,4]
my_list = ["preeti","cat",1.5,2,600,4.4]
print(my_list)
print (len(my_list))

first_list = ["naina","bod","kriti",4,5]
print(first_list[1]) #indexing list
print(first_list[3:])  #slicing
final_list = my_list+first_list  #concatinate list#
print(final_list)
first_list[0] = 1   #no problem in reassignment like string#
print(first_list)
first_list.append("Bahubali") #append function is used to add item in list
print(first_list)
first_list.pop()
print(first_list)  #pop is used to  remove an item from list
print(first_list.pop(2)) #pop can be indexed
 
list = [10,5,11,3]
list.sort()   #sort function is used to sorting the list
print(list)
list.reverse()  #reverse function is used to reverse the list
print(list)
list.remove(5)    #remove the item from the list
print(list)
del list[0]        # del is used to remove item by using index
print(list)

#dictionaries#
vehicles = {"two wheel": "Bike","four wheel": "Car"}
a =vehicles["two wheel"]   #indexing
print(a)
vehicles["two wheel"] = "cycle"  #reassignment
print(vehicles)
a ={"name":"preeti","age":[10,20,19],"class":{"Bachelor":"3rd sem"}}  #indexing methods
print(a["name"])
print(a["age"][1])
print(a["class"]["Bachelor"])
a["roll no"]=10
print(a)
print(a.keys())
print(a.values())
print(a.items())

#tuples#they are immutable i.e elements inside the tuple cannot be reassingned#
a = (1,2,3,1,2)
print(a.count(1))
print(a.index(2))

#set#unoredered collection of unique elements#
a = {1,2,1,4,5,1,6,8}
print(a)
myset = set()
myset.add("preeti")
print(myset)
my_list = [1,1,1,2,2,2,5,4,3,6,77,7,77]
print(set(my_list))
a ="preeti"
print(a[::-1])