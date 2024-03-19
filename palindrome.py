a = input("Enter a string")
b=""
for i in a:
    b = i+b
if a==b:
    print(a,"is palindrome string.")
else:
    print(a, "is not palindrome string.")      