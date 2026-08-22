a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    largest = a
    print("The largest number is:", largest)
elif b >= a and b >= c:
    largest = b 
    print("The largest number is:", largest)
else:
    largest = c
    print("The largest number is:", largest)