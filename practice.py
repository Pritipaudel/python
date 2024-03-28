# Use for, .split(), and if to create a Statement that will print out words that start with 's':

st = 'Print only the words that start with s in this sentence'
words = st.split()
print(words)
for word in words:
    if word[0] == "s":
        print(word)  

# Use range() to print all the even numbers from 0 to 10.
for i in range(0,11,2):
    print(i)  

# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
numbers = [x for x in range(1,51) if x%3==0]
print(numbers)          

# Go through the string below and if the length of a word is even print "even!"

st = 'Print every word in this sentence that has an even number of letters'
words = st.split()
for word in words:
    if len(word)%2==0:
        print(word)

# Write a program that prints the integers from 1 to 100.
#  But for multiples of three print "Fizz" instead of the number
# and for the multiples of five print "Buzz"
# For numbers which are multiples of both three and five print "FizzBuzz".        
        
for integer in range(1,101):
    if integer%3==0 and integer%5==0:
        print("fizzbuzz")
    elif integer%3 == 0:
        print("fizz")
    elif integer%5==0:
        print("Buzz")  
    else:
        print(integer) 


#  Use List Comprehension to create a list of the first letters of every word in the string below:

st = 'Create a list of the first letters of every word in this string'    
word = st.split()
new_list = [words[0] for words in word ]   
print(new_list)                

# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both 
# numbers are even, but returns the greater if one or both numbers are odd
# lesser_of_two_evens(2,4) --> 2
# lesser_of_two_evens(2,5) --> 5
def number_identify(a,b):
    if a%2 == 0 and b%2 ==0:
        return min(a,b)
    else:
         return max(a,b)
result = number_identify(4,6)
output = number_identify(3,5)
print(result)
print(output)    


# ANIMAL CRACKERS: Write a function takes a two-word string 
# and returns True if both words begin with same letter
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False
def identify(name):
    words = name.split()
    if words[0][0] == words[1][0]:
        return True
    else:
        return False

output = identify("Preeti Paudel")
print(output)


# MAKES TWENTY: Given two integers, return True if the sum of the integers
# is 20 or if one of the integers is 20. If not, return False
# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False

def makes_twenty(a,b):
    if a+b == 20:
        return True
    elif a == 20 or b==20:
        return True
    else:
        return False
outcome = makes_twenty(17,3)
print(outcome)    

# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
 
# old_macdonald('macdonald') --> MacDonald
# Note: 'macdonald'.capitalize() returns 'Macdonald'

def capitalize(name):
    if len(name)>=4:
        return name[0].upper()+name[1:3]+name[3].upper()+name[4:]
outcome = capitalize("preeti") 
print(outcome)  
#or
def changing(name):
    new_name = ""
    for i,char in  enumerate(name):
         if i ==0 or i == 3:
            new_name += char.upper()
         else:
             new_name += char
    return new_name
vt = changing("macdonalds")
print(vt)  
    

# MASTER YODA: Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'

def new_word(sentence):
    word = sentence.split()
    reversed_word = word[::-1]
    new_word =" ".join(reversed_word)
    return new_word
words = new_word("Hello I am preeti")
print( words )

# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False


def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
        else:
            return False
outcome = has_33([1,2,3,3])   
print(outcome)  

# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

def change_char(string):
    new_string = ""
    for i in string:
        new_string = new_string +i*3
    return new_string
val = change_char("preeti")   
print(val) 



# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, 
# return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.]
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19
def blackjack(a,b,c):
    a and b and c  in range(1,12)
    sum = a+b+c
    if sum<= 21:
        return sum
    elif sum>21 and a==11 or b== 11 or c==11:
        return sum-10
    else:
        return "BUST"
outcome = blackjack(9,9,9)
print(outcome)  


# SUMMER OF '69: Return the sum of the numbers in the array, 
# except ignore sections of numbers starting with a 6 and extending
# to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14

# Write a function that returns the number of prime numbers that exist up to and 
# including a given number
# count_primes(100) --> 25
# By convention, 0 and 1 are not prime.

def identify_prime(n):
    prime_count = 0
    if n < 2:
        return 0
    
    for i in range(2, n+1):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_count += 1
    
    return prime_count

prime = identify_prime(10)
print(prime)
   
